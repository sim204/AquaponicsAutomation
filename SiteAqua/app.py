from flask import Flask, render_template, request
from datetime import datetime
import time
import mariadb
import socket

address_ip = "10.150.132.42"# address ip du raspberry pi
app = Flask(__name__)


date = [""]
# premiere page html default
@app.route('/', methods = ['POST', 'GET'])
def index():
    form_data_date = request.form.get("Field1_name")
    date[0] = form_data_date
    return render_template('index.html', form_data = form_data_date)

# deuxieme page html qui affiche les donnees du database
@app.route('/data')
def data():
    # connecter sur la database avec le python connector de mariadb
    connection = mariadb.connect(
        user = "pi",
        password = "password",
        host = "127.0.0.1",
        port = 3306
    )
    cursor = connection.cursor()
    cursor.execute("USE SensorData")
    cursor.execute("Select column_name from information_schema.columns where table_name='sensordata'")
    ligne1 = cursor.fetchall()
    
    cursor.execute(f"Select * From sensordata WHERE TimeStamp >= '{date[0]}'")
    matricedata = cursor.fetchall()
    matricedata.reverse()
    
    cursor.close()
    connection.close()
    return render_template('data.html', ligne1 = ligne1, matricedata = matricedata)

if __name__ == "__main__":
    app.run(debug = True, host=address_ip)
