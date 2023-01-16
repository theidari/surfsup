# --------------------------------------------------------------------------------------------------------
# --------------------------------------------- Climate APP ----------------------------------------------
# --------------------------------------------------------------------------------------------------------

from package_1.helpers import *  #liberaries and functions
from package_1.orm import * # alchemy orm
from package_1.constants import * # constants

# 1. flask Setup-----------------------------------------------------------------------------------------/
# a-1) import Flask
from flask import Flask, jsonify, render_template

# b-1) create an app, being sure to pass __name__ and insert .html folder
app = Flask(__name__,template_folder="./package_2")

# c-1) initiate orm with database path
db = initiate_orm (db_path) 

# d-1) orm config params
session        = db["session"]
reference      = db["reference"]
inspector      = db["inspector"]
engine         = db["engine"]
col_key        = db["key"]
# -------------------------------------------------------------------------------------------------------/

# 2. define a route -------------------------------------------------------------------------------------/
# a-2) define a homepage route (user hits the / route)
@app.route("/")
def homepage():
    print("Server received request for 'Home' page...")
    return render_template ("homepage.html")

# b-2) define a precipitation route (user hits the /api/v1.0/precipitation route)
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    # create our session (link) from Python to the DB
    session
    # find the most recent date in the data set.
    measurement_query=session.query(reference[0].date, reference[0].prcp).all()
    recent_date=measurement_query[-1][0]
    # find 1 year ago date(calculate the date one year from the last date in data set.)
    year_ago=(dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    # perform a query to retrieve the data and precipitation scores and sort data
    recent_year=session.query(reference[0].date, reference[0].prcp)\
                                .filter(reference[0].date >= year_ago)\
                                .order_by(reference[0].date).all()
    session.close()
    # convert the query results to a dictionary using date as the key and prcp as the value.
    all_precipication = []
    for date, prcp in recent_year:
        if prcp != None:
            precip_dict = {}
            precip_dict[date] = prcp
            all_precipication.append(precip_dict)

    # return the JSON representation of dictionary.
    return jsonify(all_precipication)

# c-2) define a stations route (user hits the /api/v1.0/stations route)
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    # create our session (link) from Python to the DB
    session
    # query for stations.
    station_activity=session.query(reference[1].station,\
                                   reference[1].name,\
                                   reference[1].latitude,\
                                   reference[1].longitude,\
                                   reference[1].elevation,\
                                   func.count(reference[0].station))\
                                    .filter(reference[1].station == reference[0].station)\
                                    .group_by(reference[1].station)\
                                    .order_by(func.count(reference[0].station).desc())\
                                    .all()
    session.close()

    # convert the query results to a dictionary.
    all_stations                                 = []
    for query in station_activity:
        station_dict                             = {}
        station_dict["station"]                  = query[0]
        station_dict["name"]                     = query[1]
        station_dict["latitude"]                 = query[2]
        station_dict["longitude"]                = query[3]
        station_dict["elevation"]                = query[4]
        station_dict["Number of Colected Data"]  = query[5]
        all_stations.append(station_dict)

    # return the JSON representation of dictionary.
    return jsonify(all_stations)

# d-2) define a stations route (user hits the /api/v1.0/tobs route)
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'Temprature Observation' page...")
    # create our session (link) from Python to the DB
    session
    # find the most recent date in the data set.
    measurement_query=session.query(reference[0].date, reference[0].prcp).all()
    recent_date=measurement_query[-1][0]
    # find 1 year ago date(Calculate the date one year from the last date in data set.)
    year_ago=(dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    # perform a query to retrieve the data and temprature for most active station
    station_activity=session.query(reference[1].station,\
                                   reference[1].name,\
                                   func.count(reference[0].station))\
                                    .filter(reference[1].station == reference[0].station)\
                                    .group_by(reference[1].station)\
                                    .order_by(func.count(reference[0].station).desc())\
                                    .all()
    # most active station
    most_active_station=station_activity[0]
    # query to retrive data for most active station in last year
    temperature_observation = session.query(reference[0].date,\
                                            reference[0].tobs)\
                                            .filter(reference[0].date >= year_ago,\
                                                    reference[0].station == most_active_station[0])\
                                            .all()
    session.close()

    # convert the query results to a dictionary.
    all_temperatures = [{"Most Active Station":most_active_station[0]},]
    for date, temp in temperature_observation:
        if temp != None:
            temp_dict = {}
            temp_dict[date] = temp
            all_temperatures.append(temp_dict)
            
    # return the JSON representation of dictionary.
    return jsonify(all_temperatures)

# e-2) define a date route (user hits the /api/v1.0/<start> or /api/v1.0/<start>/<end> route)
@app.route("/api/v1.0/<start>") 
@app.route("/api/v1.0/<start>/<end>")
def temp_query(start,end=""):
    print("Server received request for 'Date' page...")
    # create our session (link) from Python to the DB
    session
    # query for route
    if end != "":
        active_station_temp=session.query(func.min(reference[0].tobs),\
                                          func.max(reference[0].tobs),\
                                          func.avg(reference[0].tobs))\
                                            .filter(reference[0].date >= start)\
                                            .filter(reference[0].date <= end)\
                                            .all()
    else: 
        active_station_temp=session.query(func.min(reference[0].tobs),\
                                          func.max(reference[0].tobs),\
                                          func.avg(reference[0].tobs))\
                                            .filter(reference[0].date >= start)\
                                            .all()

    session.close()
    
    # convert the query results to a list.
    temperature_list = []
    active_station_temp == False
    for min_temp, avg_temp, max_temp in active_station_temp:
        if min_temp == None or avg_temp == None or max_temp == None:
            active_station_temp = True
        temperature_list.append(min_temp)
        temperature_list.append(avg_temp)
        temperature_list.append(max_temp)
    
    # return the JSON representation or alert page.
    if  active_station_temp == True:
        return f"No temperature data found for the range!"
    else:
        return jsonify(temperature_list)
# -------------------------------------------------------------------------------------------------------/

# 2. open browser and run app ---------------------------------------------------------------------------/
def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1,open_browser).start()
    app.run(debug=True)
# -------------------------------------------------------------------------------------------------------/


