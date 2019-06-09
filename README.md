# Verde
## PDX Code guild project
For my capstone project, I am developing a Web application that allows user to look at green house emission from energy industry across United states. The user can then create charts to compare emission over years, emission from different states, emission with respect to fuel source etc. I sourced the data I used from a  repository Data.gov. (https://catalog.data.gov/dataset/energy-related-environmental-data) . The project will be developed in a python-based web-framework, Django. For user interaction, I will be using HTML, CSS, and Javascript. For plot development I will be using Plot.ly 
## Functionality
The home page will give the user some general information about what green house gases are, what is the importance of monitoring them and hat are the usual sources of greenhouses. The home page will also have Data button which will take the user to a page where we describe what type of data we have and how we can visualize them.
For example, if the user wants to compare emission of SO2 from the state of Hawaii, He/She can First select the state, then How many years he wants to compare, the greenhouse gas type, and the type of chart he/she wants. After the map is generated, the user can export it as a pdf
A sample Drop down menu 
State (AK to WY)	No of years (1994-2016	Greenhouse Gas	Type of chart
		SO2	
		CO2	
		NOx	

Another option is to compare emission from different states and provide a thematic map showing the amount of emission per state.
## Data Model
The data I need to store are State, Year range, Type of gas, and chart type.

