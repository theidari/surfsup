# ----------------------- Reflect Tables into SQLAlchemy ORM -----------------------
# ----------------- Python SQL toolkit and Object Relational Mapper ----------------
from package_1.helpers import *  #liberaries and functions
from package_1.constants import * # constants

station_location = gv.Dataset(station_df, kdims=["name"])
locs = station_location.to(gv.Points, [lng, lat], ["station", "elevation"])
locs_plot=(gts.OSM  * locs).opts(
    opts.Points(
    width=550,
    height=500,
    tools=['hover'],
    marker='triangle_dot',
    size=15,
    fill_color="r", 
    fill_alpha=0.5,
    line_color="black",    
    line_alpha=0.8
    ))
gv.save(locs_plot, '..\Output\out.html')
