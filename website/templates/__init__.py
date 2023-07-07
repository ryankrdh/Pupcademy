from flask import Flask

def create_app():
    app = Flask(__name__) # initializing flask. 
    app.config['SECRET_KEY'] = 'asdf;lkj' # encrypts the cookies and session data

    return app
