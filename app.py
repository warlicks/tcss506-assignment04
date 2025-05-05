#!/usr/bin/env python3
#make a flask hello world app
from flask import Flask, render_template, request, session, redirect, url_for
import os

from api.fetch_data import fetch_tripadvisor_data
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
@app.route('/')
def index():
    session['city'] = 'Tacoma'
    session['state'] = 'WA'
    if request.method == 'GET':
        if request.args.get('city'):
            session['city'] = request.args.get('city')
        if request.args.get('state'):
            session['state'] = request.args.get('state')
        
    # Create a data object with business information
    location_data = fetch_tripadvisor_data(session['city'], session['state'], "restaurants", use_cache_only=True)
    location_data.extend(fetch_tripadvisor_data(session['city'], session['state'], "hotels", use_cache_only=True))
    location_data.extend(fetch_tripadvisor_data(session['city'], session['state'], "attractions", use_cache_only=True))
    return render_template('index.html', city=session['city'], state=session['state'], location_data=location_data)

@app.route("/about")
def about():
    message = """This is a demo flask application that collects travel data from TripAdvisor. It was created as a part of the TCSS 506 Course."""
    return render_template('about.html', message=message, author="Sean Warlick")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
