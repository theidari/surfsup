# ----------------------- Reflect Tables into SQLAlchemy ORM -----------------------
# ----------------- Python SQL toolkit and Object Relational Mapper ----------------
from package_1.helpers import *  #liberaries and functions
from package_1.constants import * # constants

station_location = gv.Dataset(station_df, kdims=["name"])
locs = station_location.to(gv.Points, ["longitude", "latitude"], ["station", "name", "elevation"])
(gts.OSM  * locs).opts(
    opts.Points(width=550,
    height=475,
    tools=['hover'],
    hover_fill_alpha=0.5,
    hover_fill_color='red',           
    marker='triangle_dot',
    size=15,
    alpha=0.8,
    muted_alpha=0.1,
    fill_color="r",
    line_color="black",    
    cmap="tab10",
    legend_position="right"))
plt.savefig("stationlocation.png",\
               dpi=300, bbox_inches='tight')