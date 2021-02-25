# Project 2
ENGO 551

The purpose of this web application is to map building permits in Calgary. Users can select a date range and visualize the building permits issued.
The City of Calgary's Open Calgary API is used to pull permit data. The Leaflet API is used to construct the interactive map interface.

The leaflet marker cluster plug-in is used to group markers that are close together when the map is zoomed out. You can click on the clusters to
zoom closer. For multiple markers at the same location, the marker cluster plug-in uses spiderfying at the bottom zoom level to separate the markers.
Therefore, there is no need to use a separate spiderfy plug-in (since this is already done by default with marker clustering).

The date-picker widget used was adapted from Esri's Leaflet Time Ranges widget: https://esri.github.io/esri-leaflet/examples/visualizing-time-on-dynamic-map-layer.html

application.py - The python flask application. At the default route, it renders index.html to produce a map of Calgary with no markers. When passed
dates by the form widget, the dates route performs a request to get the API data for the given dates from the City of Calgary API. It then renders
index.html, passing the API data along with error messages if the "From" date is later than the "To" date, or if the selected dates produced no results.
It is also checked whether the "From" date selected is later than the current date. The "From" and "To" dates are also passed so the widget can display
the dates queried.

index.html - The interactive map webpage. A simple map is rendered centered at Calgary (Open Street Map + mapbox are used). The date picker widget is in
the top right corner of the page. The geojson data collected from the City of Calgary API is looped through to create markers and add them to clusters. A marker
can only be created if there is geometry data for the object. If dates are submitted using the widget, the page is refreshed with markers/marker clusters
displayed for the queried dates. A message is also displayed in the widget when a query has been performed. A message displays the queried dates if the search
was successful. An error message is displayed if the user entered a "From" date later than a "To" date. A message is also displayed if the selected dates
did not return any permits. An additional message is also shown if the user enters a "From" date in the future. The widget also stores the current search dates;
for the default route, today's date is displayed in both "From" and "To".

layout.html - The layout format for any html pages. Contains all header links as well as styling.

requirements.txt - contains requirements of what has to be installed to run the application.
