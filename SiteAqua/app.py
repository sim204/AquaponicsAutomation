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

# premiere page html default
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')# le template "index.html" est dans le fichier "templates"

# deuxieme page html qui affiche les donnees du database
@app.route('/data')
def data():
    cursor = connection.cursor()
    cursor.execute("USE SensorData")
    cursor.execute("Select * From sensordata")
    matricedata = cursor.fetchall()
    return render_template('data.html', matricedata = matricedata)# data.html aura acces a la variable matricedata

if __name__ == "__main__":
    app.run(debug = True, host=address_ip)