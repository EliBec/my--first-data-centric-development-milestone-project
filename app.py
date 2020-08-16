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
@app.route('/get_yardsales',  methods=["GET", "POST"])
def get_yardsales():
    yardsales = mongo.db.yard_sales.find()
    categories = mongo.db.categories.find()

    return render_template('getyardsales.html', yardsales=yardsales, categories=categories)


@app.route('/add_yardsales')
def add_yardsales():
    return render_template('addyardsales.html')


@app.route('/updatedelete_yardsales')
def updatedelete_yardsales():
    return render_template('updatedeleteyardsales.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
