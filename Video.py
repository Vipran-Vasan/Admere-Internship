import mysql.connector
from flask import Flask, Response

app = Flask(__name__)

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='root',
    password='kishvip@1998',
    host='127.0.0.1',
    database='videos'
)
print(mydb)

#To create a cursor in the database
mycursor = mydb.cursor()

#To specify a URL route for flask using <video_id> as a variable placeholder
@app.route('/videos/<video_id>')


def get_video(video_id):

    # Retrieve the video data from the database
    query = 'SELECT data FROM videos WHERE id = %s'

    #Creating parameters for selecting the video from the database
    params = (video_id,)
    mycursor.execute(query, params)

    #To fetch the video from one column of the database specified in the parameters
    video_data = mycursor.fetchone()[0]

    #Return the video data as a Flask response where the data is indicated as mp4 
    return Response(video_data, mimetype='video/mp4')

#The module used to start the Flask Application Server
if __name__ == '__main__':
    app.run()
