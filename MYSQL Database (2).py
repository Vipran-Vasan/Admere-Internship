#To connect with the mysql localhost server with the details
import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "kishvip@1998",
        database = "todolist"
)
print(mydb)

#To create a cursor in my database
mycursor = mydb.cursor()

#This inserts columns which I want into my database (SHOWS SOME ERROR)
mycursor.execute("INSERT INTO todolist(Date VARCHAR(255), Time VARCHAR(255), Date_time_Object VARCHAR(255), Time_Object VARCHAR(255))")

#Defining a function of adding Values into the table
def add():
  add = "INSERT INTO todolist(Serial_Number, Task, Status, Date, Time, Date_time_Object, Time_Object)"
  val = "VALUES()"
  mycursor.execute(add,val)
  mydb.commit()

#Defining a function of removing Values from a row
def remove():
  Serial_Value = 1
  mycursor.execute("DELETE FROM todolist WHERE Serial_Number = Serial_Value")
  mydb.commit()

#Defining a function to edit Values from a row (INCOMPLETE)
def edit():
  edits = "Serial_Number==2"
  editing = "Serial_Number==1"
  mycursor.execute(Serial_Number, task = None, date = None, time = None, datetime_obj = None, time_obj = None, completed = None
  mydb.commit()
