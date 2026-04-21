from flask import Flask
#Simple Flask app
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
    