# import required libraries 
import streamlit as st  # type: ignore
from datetime import datetime
from zoneinfo import ZoneInfo

# List of  avilable timezones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Europe/Paris",
    "America/New_York", 
    "Europe/Berlin",
    "Asia/Tokyo",
    "Europe/London",
    "Australia/Sydney",
    "Asia/Dubai",
    "Europe/Hong_Kong",
    "Asia/Kolkata"  
]

# App Title
st.title("⏰ Time Zone App 🎉")

# Creat a multiselected widget for selected timexones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default =["UTC","Asia/Karachi"])

# Display the selected timezones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    
    # Get and format current time for each selected timezones with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%S %p")
    
    # Display the current time for each selected timezone
    st.write(f"{tz}: {current_time}") 

# Create a subheader for converting time between timezones
st.subheader("Convert Time Between Timezones")

# Create a time input widget for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# Create a selectbox for selecting the timezone to convert from 
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# Create a selectbox for selecting the timezone to convert from the current timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create a button to trigger the time conversion
if st.button("Convert Time"):
    
    # combine the current time with the selected timezone
    dt = datetime.combine(datetime.today(), current_time,tzinfo=ZoneInfo(from_tz))
    
    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%S %p")
    
    # Display the converted time 
    st.success(f"Converted Time in {to_tz}: {converted_time}")