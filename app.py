import os
import requests
import time
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
                searchcriteriadict['category'] = {'$in': ['Estate', 'Garage', 'Community']}
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


@app.route('/add_yardsales', methods=["GET", "POST"])
def add_yardsales():
    countries = mongo.db.countries.find()

    return render_template('addyardsales.html', countries=countries)


@app.route('/insert_yardsale', methods=["GET", "POST"])
def insert_yardsale():
    # first find/fetch yard_sale collection object
    yardsales = mongo.db.yard_sales

    # retrieve address from form 
    address_1 = request.form.get('address1')
    address_2 = request.form.get('address2')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')

    full_addr = address_1 +  address_2 + " " + city + " " + state + " " + zip

    google_coor = google_get_coord(full_addr)
    print(google_coor)
    #addr_long = google_get_goelong(full_addr)

    addr_lat = google_coor[0]
    print(addr_lat)

    addr_long = google_coor[1]
    print(addr_long)

    yardsales.insert_one({
            'seller_first_name': request.form.get('first_name'),
            'seller_last_name': request.form.get('last_name'),
            'seller_email': request.form.get('email'),
            'item_list': request.form.getlist('itemlist'),
            'date': request.form.get('saledate'),
            'time': request.form.get('saletime'),
            'category': request.form.get('saletype'),
            'address_1': request.form.get('address1'),
            'city': request.form.get('city'),
            'state': request.form.get('state'),
            'country_code': request.form.get('countrycode'),
            'zip': request.form.get('zip'),
            'lat': addr_lat,
            'long': addr_long
        })

    return redirect(url_for('get_yardsales'))


# getting coordinates
def google_get_goelat(full_addr):
    print(full_addr)
    # get coords for mapping
    search_payload = {"key": google_key, "query": full_addr}
    search_req = requests.get(googlemap_search_url, search_payload)
    # make sure the page is reachable
    # print(search_req.status_code)
    search_json = search_req.json()
    print(search_json)
    time.sleep(.3)
    latitude = search_json["results"][0]["geometry"]["location"]["lat"]
    print(latitude)

    return latitude


# getting coordinates
def google_get_coord(full_addr):

    #print(full_addr)
    # get coords for mapping
    search_payload = {"key": google_key, "query": full_addr}
    search_req = requests.get(googlemap_search_url, search_payload)
    # make sure the page is reachable
    # print(search_req.status_code)
    search_json = search_req.json()
    time.sleep(.3)
    latitude = search_json["results"][0]["geometry"]["location"]["lat"]
    longitude = search_json["results"][0]["geometry"]["location"]["lng"]  
    coordinates = [latitude, longitude,]
    print(coordinates)

    return coordinates


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
