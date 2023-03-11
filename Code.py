#To connect with the mysql localhost server with the details
import mysql.connector
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password = "kishvip@1998",
        database = "todolist"
)
print(mydb)

#To create a cursor in my database
mycursor = mydb.cursor()


# Define endpoints for the API
@app.route('/users', methods=['GET', 'POST'])

def users():
    #To check whether need to get data from the database or update
  
    if request.method == 'GET':
        # Fetch the data from database to send to the front-end
        serial_number = request.json['id']
        data = mycursor.execute("SELECT * FROM todolist WHERE Serial_Number=",(serial_number))
        print(data)
        return jsonify(data)
      
    elif request.method == 'POST':
        # Insert data from the front-end into the database 
        serial_number = request.json['id']
        task = request.json['task']
        status = request.json['status']
        mycursor.execute('INSERT INTO todolist (serial_number, task, status) VALUES (%s, %s, %s)', (serial_number, task, status))
        mydb.commit()
        return jsonify({'message': 'task created'})

if(__name__ == "__main__"):
    app.run()
