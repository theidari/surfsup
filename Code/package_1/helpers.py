# All libraries, variables and functions are defined in this fil
# --------------------------------------------------------------
# libraries

# a) main dependencies and setup
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import datetime as dt

# b) python SQL toolkit and Object Relational Mapper (ORM)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# c) plotting
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
