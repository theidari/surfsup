<img src="https://raw.githubusercontent.com/theidari/surfsup/main/DesignIMG/surfsupheadertra.png" width="900px">
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp Honolulu, on the island of Oahu’s south shore, is capital of Hawaii and gateway to the U.S. island chain. The Waikiki neighborhood is its center for dining, nightlife and shopping, famed for its iconic crescent beach backed by palms and high-rise hotels, with volcanic Diamond Head crater looming in the distance. Sites relating to the World War II attack on Pearl Harbor include the USS Arizona Memorial.</br></br>

<img src="https://raw.githubusercontent.com/theidari/surfsup/main/DesignIMG/subheaderPOet.png" width="900px">
 
 <h4>Objective</h4> 
 This project used a Python and SQLAlchemy to make climate analysis
This project is broken down into two deliverable parts, `Analyze and Explore the Climate Data` and `VacationPy`.</br>

<h4>Methods, Software and Attribution:</h4>
In this project for preveting replication and following DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code making package folder was used. package_1 contains constants, helper (libraries, variables and functions), and orm connector files. package_2 contains javascript, CSS, and HTML files that used for .app interface.
<img src="https://raw.githubusercontent.com/theidari/surfsup/main/DesignIMG/subheaderHTert.png" width="900px"><br></br>
 - The <b>SQLAlchemy ORM</b> file available in /Code/package_1 folder makes Jupyter Notebook database connection (<a herf="https://github.com/theidari/surfsup/blob/main/Code/package_1/orm.py">link<a>)<br></br>
<img src="https://raw.githubusercontent.com/theidari/surfsup/main/DesignIMG/subheaderREert.png" width="900px">
<h4> Part 1: Analyze and Explore the Climate Data </h4>
 - <b>Precipitation Analysis</b><br></br>
 Date <b>2017-08-23</b> was found as last date. Result of creating a query that collects only the date and precipitation for the last year and sorting the data, shows in <a herf="https://github.com/theidari/surfsup/blob/main/Output/prcp_last_year_data.csv">PRCP Last Year</a>, and figure [1]. statistics for the precipitation data was performed by Pandas summary statistic, and showed.
 <h6 align="center"> Fig [1] Precipitation in Honolulu 2016-2017 </h6>
<p align="center">
<img src="https://raw.githubusercontent.com/theidari/surfsup/main/Output/Precipitation_in_Honolulu%2CHI_from_2016-08-23_to_2017-08-23.png" width="600px">
</p>

 - <b>Station Analysis</b>
 <h6 align="right"> Fig [2] Station Location&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp </h6>
<img align="right" src="https://raw.githubusercontent.com/theidari/surfsup/main/Output/All_Map_Modif.png" width="400px"><b> 9 </b> stations found (<a herf="https://github.com/theidari/surfsup/blob/main/Code/station_location.py">figure [2]</a>) after created a query to calculate the total number of stations and most active station list. <a herf="https://github.com/theidari/surfsup/blob/main/Output/station_location_data.csv">the station location data</a> shows this list with number of data collected for each station. after sorted in descending order station <ins>WAIHEE 837.5, HI US</ins> with code of <ins>USC00519281</ins> has the highest data number with amount of <b>2772</b> data.
For this station lowest temperature is <b>54.0 F</b>, highest temperature is <b>85.0 F</b>, and average temperature is <b>71.66 F</b>.<br></br><br></br><br></br>
 A query created to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations in 12 bins. output of this query is available in <a herf="https://github.com/theidari/surfsup/blob/main/Output/most_active_temp.csv">Most Active Station Data</a> and figure [3]
 
<h6 align="center"> Fig [3] Temprature Observation in Honolulu 2016-2017 </h6>
<p align="center">
<img src="https://raw.githubusercontent.com/theidari/surfsup/main/Output/Temperatures%20Observed_at_USC00519281_in_12%20month.png" width="600px">
</p>

<p align="clear">
<h4> Part 2: Design Climate App </h4>
A Flask API was designed based on the developed queries. Figure 3 shows how the climate app works: 
</p>

<img src="https://raw.githubusercontent.com/theidari/surfsup/main/DesignIMG/subheaderREFert.png" width="900px">

<sup>[1]</sup> Trilogy Education Services, a <a href="https://2u.com/">2U, Inc.</a> brand.</br>
<sup>[2]</sup>Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1


<p align="right">
<a href="https://github.com/theidari/surfsup#objective"><sup>TOP PAGE</sup></a>
</P>
