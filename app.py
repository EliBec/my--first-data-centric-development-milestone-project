import os
import requests
import time
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_googlemaps import GoogleMaps
from bson.objectid import ObjectId
from datetime import date

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
@app.route('/get_yardsales/', methods=["GET", "POST"])
def get_yardsales():
    #yardsales = mongo.db.yard_sales.find()
    categories = mongo.db.categories.find()

    # declare dictionary
    searchcriteriadict = {}

    if request.method == "POST":
        # if  form's returned value is not empty then add to dictionary /
        yardsale_cat = request.form.get('categorysearch').capitalize()
        if yardsale_cat != "":
            if yardsale_cat == "All":
                searchcriteriadict['category'] = {'$in': ['Estate', 'Garage', 'Community']}
            else:
                searchcriteriadict['category'] = yardsale_cat.capitalize()

        yardsale_date = request.form.get('datesearch')
        if yardsale_date != "":
            searchcriteriadict['date'] = yardsale_date


        # value in form "cityorzip" is either the zip code or city
        yardsale_cityorzip = request.form.get('cityorzipsearch')
        if yardsale_cityorzip != "":

            # check if there is matching document where form's value is equal to city. If found, then add to dictionary. Else, perform same search and action but for zip code

            if mongo.db.yard_sales.count_documents({'city': yardsale_cityorzip}) > 0:
                searchcriteriadict['city'] = yardsale_cityorzip

            else:
                if mongo.db.yard_sales.count_documents({'zip': yardsale_cityorzip})> 0:
                    searchcriteriadict['zip'] = yardsale_cityorzip

        yardsale_items = request.form.get('itemsearch').capitalize()

        if yardsale_items != "":
            searchcriteriadict['item_list'] = {'$in': [yardsale_items]}

        if searchcriteriadict != {}:
            search_results = mongo.db.yard_sales.find(searchcriteriadict)
            
            yardsales_count = mongo.db.yard_sales.count_documents(searchcriteriadict)

            return render_template('getyardsales.html', yardsales=search_results, categories=categories, google_key=google_key, yardsales_count=yardsales_count, mode="search")

        else:
            return render_template('getyardsales.html', yardsales_count=0, mode="search")

    else:

        today_date = date.today()
        today_str = today_date.strftime("%Y-%m-%d")

        yardsales = mongo.db.yard_sales.find({'date': today_str})

        yardsales_count = yardsales.count() 
        print('conteo' + str(yardsales_count))

        return render_template('getyardsales.html', yardsales=yardsales, categories=categories, google_key=google_key, yardsales_count=yardsales_count, mode="all")


# route for the Add Yard Sales page (addyardsales.html)
@app.route('/add_yardsales', methods=["GET", "POST"])
def add_yardsales():

    record_status=request.args.get('record_status')
    # print(record_status)

    countries = mongo.db.countries.find()

    return render_template('addyardsales.html', countries=countries, record_status=record_status)


# request addyardsales.html's form and insert it to the 'yard_sales' collection
@app.route('/insert_yardsale', methods=["GET", "POST"])
def insert_yardsale():
    # first find/fetch yard_sale collection object
    yardsales = mongo.db.yard_sales

    # retrieve address from form in addyardsales.html
    address_1 = request.form.get('address1')
    address_2 = request.form.get('address2')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')

    full_addr = address_1 + address_2 + " " + city + " " + state + " " + zip

    # pass in the address (to get_google_coord) for which google coordinates are fetched from API's JSON
    google_coor = get_google_coord(full_addr)
    # print(google_coor)

    addr_lat = google_coor[0]
    # print(addr_lat)

    addr_long = google_coor[1]
    # print(addr_long)

    itemlist_array = []
    itemlist_array = request.form.getlist('itemlist')

    itemlist_lwr = [i.capitalize() for i in itemlist_array]

    yardsales.insert_one({
            'seller_first_name': request.form.get('first_name'),
            'seller_last_name': request.form.get('last_name'),
            'seller_email': request.form.get('email'),
            'item_list': itemlist_lwr,
            'date': request.form.get('saledate'),
            'time': request.form.get('saletime'),
            'category': request.form.get('salecat').capitalize(),
            'address_1': request.form.get('address1'),
            'city': request.form.get('city'),
            'state': request.form.get('state'),
            'country_code': request.form.get('countrycode'),
            'zip': request.form.get('zip'),
            'lat': addr_lat,
            'long': addr_long
        })

    record_status = "added"

    #return redirect(url_for('get_yardsales', record_status=record_status))
    return redirect(url_for('add_yardsales', record_status=record_status))


# getting coordinates
def get_google_coord(full_addr):
    search_payload = {"key": google_key, "query": full_addr}
    search_req = requests.get(googlemap_search_url, search_payload)
    search_json = search_req.json()
    time.sleep(.3)
    latitude = search_json["results"][0]["geometry"]["location"]["lat"]
    longitude = search_json["results"][0]["geometry"]["location"]["lng"]  
    coordinates = [latitude, longitude]
    print(coordinates)

    return coordinates

# rout to page updatedeleteyardsales.html
@app.route('/updatedelete_yardsales', methods=["GET", "POST"])
def updatedelete_yardsales():

    # declare dictionary
    searchdict = {}

    if request.method == "POST":
        # if  form's returned value is not empty then add to dictionary
        yardsale_date = request.form.get('datesearch')
        if yardsale_date != "":
            searchdict['date'] = yardsale_date

        yardsale_fname = request.form.get('fnamesearch')
        if yardsale_fname != "":
            searchdict['seller_first_name'] = yardsale_fname

        yardsale_lname = request.form.get('lnamesearch')
        if yardsale_lname != "":
            searchdict['seller_last_name'] = yardsale_lname

        search_results = mongo.db.yard_sales.find(searchdict)

        return render_template('updatedeleteyardsales.html', yardsales=search_results, google_key= google_key)

    else:
        return render_template('updatedeleteyardsales.html')


# rout to get countries and yardsale data (using record id) and send to updatedsale.html
@app.route('/update_yardsale/<yardsale_id>/<record_status>')
def update_yardsale(yardsale_id, record_status):
    countries = mongo.db.countries.find()
    # fetch yardsale based on its id key
    yardsale_upd = mongo.db.yard_sales.find_one({'_id': ObjectId(yardsale_id)})
    return render_template('updateyardsale.html', countries=countries, yardsale_upd=yardsale_upd, google_key= google_key, record_status=record_status)



# route tosave updated changes to the database's yard_sales collection
@app.route('/save_yardsale/<yardsale_id>/<record_status>', methods=["GET", "POST"])
def save_yardsale(yardsale_id, record_status):
    yardsales = mongo.db.yard_sales

    # retrieve address from form in addyardsales.html
    address_1 = request.form.get('address1')
    address_2 = request.form.get('address2')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')

    full_addr = address_1 + address_2 + " " + city + " " + state + " " + zip

    # pass in the address (to get_google_coord) for which google coordinates are fetch from API's JSON
    google_coor = get_google_coord(full_addr)
    print(google_coor)

    addr_lat = google_coor[0]
    print(addr_lat)

    addr_long = google_coor[1]
    print(addr_long)

    yardsales.update({'_id': ObjectId(yardsale_id)},
                     {
                        'seller_first_name': request.form.get('first_name'),
                        'seller_last_name': request.form.get('last_name'),
                        'seller_email': request.form.get('email'),
                        'item_list': request.form.getlist('itemlist'),
                        'date': request.form.get('saledate'),
                        'time': request.form.get('saletime'),
                        'category': request.form.get('salecat').capitalize(),
                        'address_1': request.form.get('address1'),
                        'city': request.form.get('city'),
                        'state': request.form.get('state'),
                        'country_code': request.form.get('countrycode'),
                        'zip': request.form.get('zip'),
                        'lat': addr_lat,
                        'long': addr_long
                     })

    record_status = 'updated'

    return render_template('updatedeleteyardsales.html', record_status=record_status)


# route to delete yardsale record from colletion
@app.route('/delete_yardsale/<yardsale_id>/<record_status>')
def delete_yardsale(yardsale_id, record_status):
    mongo.db.yard_sales.remove({'_id':ObjectId(yardsale_id)})

    record_status = 'deleted'
    return render_template('updatedeleteyardsales.html', record_status=record_status)


# About us page route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact us page route
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


# 404 error page route
@app.errorhandler(404)
def page_error(error):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
