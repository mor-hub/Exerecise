from random import randint
from flask import Flask
app = Flask(__name__)


# accessed via <HOST>:<PORT>/content_file
@app.route("/content")
def content_file():
    read_users = open("Lesson3_part2.py")
    user_list = read_users.readlines()
    read_users.close()
    print(user_list)
    return {'content_file': user_list}, 200 # status code


# accessed via <HOST>:<PORT>/content_file
@app.route("/content")
def content_file():
    from PIL import Image

    img = Image.open(r"C:\Users\mor\shana_tova.png")
    img.show()
    return {'content_file': user_list}, 200 # status code


# accessed via <HOST>:<PORT>/register
@app.route("/register")
def register_into_file():
    read_users = open("words.txt", 'w')
    read_users.write(("hello" + '\n'))
    return 'success ', 201 # status code


# using default
@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_user(user_name = 'no one'):
    return 'Hello ' + user_name, 200 # status code


# accessed via <HOST>:<PORT>/welcome
@app.route("/welcome")
def welcome():
    return "<H1 id='welcome'>Welcome!</H1>", 200 # status code

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=30000)