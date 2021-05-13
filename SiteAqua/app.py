from flask import Flask, render_template
import time
import mariadb

address_ip = "10.150.141.102" # address ip du raspberry pi

# connecter sur la database avec le python connector de mariadb
connection = mariadb.connect(
    user = "pi",
    password = "password",
    host = "127.0.0.1",
    port = 3306
)
cursor = connection.cursor()

# premiere page html default
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')# le template "index.html" est dans le fichier "templates"

# deuxieme page html qui affiche les donnees du database
@app.route('/data')
def data():
    cursor.execute("USE SensorData")

    cursor.execute("Select column_name from information_schema.columns where table_name='sensordata'")
    ligne1 = cursor.fetchall()

    cursor.execute("Select * From sensordata")
    matricedata = cursor.fetchall()
    return render_template('data.html', ligne1 = ligne1, matricedata = matricedata)# data.html aura acces aux variables ligne1 et matricedata

if __name__ == "__main__":
    app.run(debug = True, host=address_ip)