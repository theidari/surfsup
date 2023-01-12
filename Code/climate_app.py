from package_1.helpers import *  #liberaries and functions
from package_1.orm import * # alchemy orm
from package_1.constants import * # constants
# 1. import Flask
from flask import Flask, jsonify, render_template
from threading import Timer
import webbrowser

# 2. Create an app, being sure to pass __name__
app = Flask(__name__,template_folder='./package_2' )


# 3. Define what to do when a user hits the index route
@app.route("/")
def homepage():
    print("Server received request for 'Home' page...")
    return render_template ("homepage.html")
db = initiate_orm (db_path)
#orm config params
session        = db["session"]
reference      = db["reference"]
inspector      = db["inspector"]
engine         = db["engine"]
col_key        = db["key"]
# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """precipitation analysis"""
    # Find the most recent date in the data set.
    measurement_query=session.query(reference[0].date, reference[0].prcp).all()
    recent_date=measurement_query[-1][0]
    # Find 1 year ago date(Calculate the date one year from the last date in data set.)
    year_ago=(dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
   # Perform a query to retrieve the data and precipitation scores and sort data
    recent_year=session.query(reference[0].date, reference[0].prcp).filter(reference[0].date >= year_ago).\
        order_by(reference[0].date).all()
    # Perform a query to retrieve the data and precipitation scores.
    session.close()
    # Convert the query results to a dictionary using date as the key and prcp as the value.
    all_precipication = []
    for date, prcp in recent_year:
        if prcp != None:
            precip_dict = {}
            precip_dict[date] = prcp
            all_precipication.append(precip_dict)

    # Return the JSON representation of dictionary.
    return jsonify(all_precipication)

@app.route("/api/v1.0/<start>")
def start(start):
    if start=="api/v1.0/2015-06-03":
        A=2023
    return (
        f"newpage"
        )

def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1,open_browser).start()
    app.run(debug=True)


