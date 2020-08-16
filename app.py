import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

# instatiate Flask application
app = Flask(__name__)

# import env.py 
if path.exists('env.py'):
    import env

# retrieve environment variables
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

# instatiate Mongo application
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
