# ------------------- folders and files name -------------------

lng          = "longitude"
lat          = "latitude"
time_length  = "12 month"         
tobs         = "Temperatures Observed"
station      = "Station"
freq         = "Frequency"
prcp         = "Precipitation"

# defining directories
db_path      = "sqlite:///../Resources/hawaii.sqlite"
output_url   = "../Output/"


# ---------------------------- plot ----------------------------
# map plot constants

width=550,
height=475,
tools=["hover"],
hover_fill_alpha=0.5,
hover_fill_color="red",           
marker="triangle_dot",
size=15,
alpha=0.8,
muted_alpha=0.1,
fill_color="r",
line_color="black",

# histogram constants
title_font_size  = 15
label_font_size  = 12
ticks_font_size  = 10
legend_font_size = 10
font_weight="bold"
plt_fig_higth = 10
plt_fig_width = 8
plt_color = "tab:blue"
legend_location = "best"

his_x_label= "Temperature"
his_y_label= "Frequency"

# line
line_x_label= "Date (yyyy-mm-dd)"
line_y_label= "Inches"
line_width = 1 



