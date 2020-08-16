import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_googlemaps import GoogleMaps
from bson.objectid import ObjectId

# instatiate Flask application
app = Flask(__name__)

# Initialize the extension
GoogleMaps(app)

# import env.py 
if path.exists('env.py'):
    import env

# retrieve environment variables
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

app.config['GOOGLEMAPS_API_KEY'] = os.environ.get('GOOGLEMAPS_API_KEY')
googlemap_search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
googlemap_details_url = "https://maps.googleapis.com/maps/api/place/details/json"
google_key = app.config['GOOGLEMAPS_API_KEY']


# instatiate Mongo application
mongo = PyMongo(app)


@app.route("/")
@app.route('/get_yardsales',  methods=["GET", "POST"])
def get_yardsales():
    yardsales = mongo.db.yard_sales.find() 
    categories = mongo.db.categories.find()

    # declare dictionary
    searchcriteriadict = {}

    if request.method == "POST":
        # if  form's returned value is not empty then add to dictionary /
        yardsale_cat = request.form.get('categorysearch')
        if yardsale_cat != "":
            if yardsale_cat == "All":
                searchcriteriadict['category'] = {'$in': ['Estate', 'Local', 'Community']}
            else:
                searchcriteriadict['category'] = yardsale_cat

        yardsale_date = request.form.get('datesearch')
        if yardsale_date != "":
            searchcriteriadict['date'] = yardsale_date

        # value in form "cityorzip" is either the zip code or city
        yardsale_cityorzip = request.form.get('cityorzipsearch')
        if yardsale_cityorzip != "":
            # check if there is matching document where form's value is equal to city. If no document is found, then add to dictionary. Otherwise,perform same search and action but for zip
            if mongo.db.yard_sales.find({'city': yardsale_cityorzip}).count() > 0:
                searchcriteriadict['city'] = yardsale_cityorzip
            else:
                if mongo.db.yard_sales.find({'zip': yardsale_cityorzip}).count() > 0:
                    searchcriteriadict['zip'] = yardsale_cityorzip


        yardsale_items = request.form.get('itemsearch')
        if yardsale_items != "":
            searchcriteriadict['item_list'] = {'$in': [yardsale_items]}
         
        search_results = mongo.db.yard_sales.find(searchcriteriadict)

        return render_template('getyardsales.html', yardsales=search_results, categories=categories, google_key= google_key)

    else:
        return render_template('getyardsales.html', yardsales=yardsales, categories=categories, google_key= google_key)


@app.route('/add_yardsales')
def add_yardsales():
    countries = mongo.db.countries.find() 
    return render_template('addyardsales.html', countries=countries)


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
