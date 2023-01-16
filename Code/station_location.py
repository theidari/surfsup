# --------------------------------------------------------------------------------------------------------
# --------------------------------------- Station Location Map Plot --------------------------------------
# --------------------------------------------------------------------------------------------------------
from package_1.helpers import *  #liberaries and functions
from package_1.orm import * # alchemy orm
from package_1.constants import * # constants

# initiate orm with database path
db = initiate_orm (db_path)
# orm config params
session        = db["session"]
reference      = db["reference"]
inspector      = db["inspector"]
engine         = db["engine"]
col_key        = db["key"]

# station query and number of colected data
station_activity=session.query( reference[1].station,\
                                reference[1].name,\
                                reference[1].latitude,\
                                reference[1].longitude,\
                                reference[1].elevation,\
                                func.count(reference[0].station)\
                                ).\
                                filter(reference[1].station == reference[0].station).\
                                group_by(reference[1].station).\
                                order_by(func.count(reference[0].station).desc()).\
                                all()
session.close()
# create station dataframe
station_df = pd.DataFrame(columns=SESSION_COLUMN_NAME)

for station_promps  in station_activity:
    a=pd.Series((item for item in station_promps),index=SESSION_COLUMN_NAME)
    station_df = station_df.append(a,ignore_index=True)

# export the station dataframe into a .csv
station_df.to_csv(output_url+"station_location_data.csv")

# station map plot
station_location(station_df, "name")
# --------------------------------------------------------------------------------------------------------
