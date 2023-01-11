# All libraries, variables and functions are defined in this fil
# --------------------------------------------------------------
# libraries
from package_1.constants import * # constants
# a) main dependencies and setup
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import datetime as dt

# b) plotting
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import hvplot.pandas
import geoviews as gv
import geoviews.feature as gf
from geoviews import dim, opts
import geoviews.tile_sources as gts
gv.extension('bokeh')


# function definition
# station location plotting function (map)
def station_location(df, kdims): #df = DataFrame #variable column
    station_location = gv.Dataset(df, kdims=[kdims])
    locs = station_location.to(gv.Points, [lng, lat], ["station", "elevation"])
    locs_plot=(gts.OSM  * locs).opts(
        opts.Points(
        width=550,
        height=500,
        tools=['hover'],
        marker='triangle_dot',
        size=15,
        fill_color="red", 
        fill_alpha=0.5,
        line_color="black",    
        line_alpha=0.8
        ))
    gv.save(locs_plot, output_url+'station_location.html')
    return locs_plot

# histogram plot
def histogram (df, bins, location):
    # plot size
    plt.figure(figsize=(plt_fig_higth,plt_fig_width))
    # plot main describtion
    plt.hist(np.array(df), color = plt_color, bins=bins)
    # ticks definitions
    plt.yticks(size=ticks_font_size)
    plt.xticks(size=ticks_font_size)
    # labels definitions
    plt.xlabel(his_x_label,fontsize=label_font_size)
    plt.ylabel(his_y_label,fontsize=label_font_size)
    # title definitions
    plt.title(tobs+" at "+location+" in "+time_length, fontsize=title_font_size, fontweight = font_weight, pad=+20)
    # legend definitions
    plt.legend([tobs], loc = legend_location, fontsize=legend_font_size)
    # plt save
    plt.savefig(output_url+tobs+"_at_"+location+"_in_"+time_length+".png",dpi=300, bbox_inches='tight')
    return plt.show()

#line graph
def line (df,date_in,date_out, location):
    # data length
    length=len(df.index)
    # plot size
    plt.figure(figsize=(plt_fig_higth,plt_fig_width))
    # plot main describtion
    plt.plot(df, color = plt_color, linewidth=line_width)
    # ticks definitions
    plt.xticks(np.arange(0,length,50), rotation = 90, rotation_mode = 'anchor',ha = 'right', fontsize=ticks_font_size)
    plt.yticks(fontsize=ticks_font_size)
    # lim definitions
    plt.xlim(date_in,date_out)
    # label definitions
    plt.xlabel(line_x_label, fontsize=label_font_size)
    plt.ylabel(line_y_label, fontsize=label_font_size)
    # title definitions
    plt.title(prcp+" in "+location+" from "+date_in+" to "+date_out, fontsize=title_font_size, fontweight = font_weight, pad=+20)
    # legend definitions
    plt.legend([prcp], loc = legend_location, fontsize=legend_font_size)
    # plt save
    plt.savefig(output_url+prcp+"_in_"+location+"_from_"+date_in+"_to_"+date_out+".png",dpi=300, bbox_inches='tight')
    return plt.show()
