import streamlit as st
import requests
import pandas as pd
from datetime import date

# Streamlit app title
st.title("SQLiteCloud Data Viewer")

# Inputs for start_date and end_date
start_date = st.date_input("Start Date", value=date(2022, 1, 1))
end_date = st.date_input("End Date", value=date(2022, 12, 31))

# API URL
api_url = "http://127.0.0.1:8000/data"

# Button to fetch data
if st.button("Fetch Data"):
    # Make a GET request to the FastAPI endpoint
    params = {"start_date": start_date.isoformat(), "end_date": end_date.isoformat()}
    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Display the data in a table
        st.write("Data from the API:")
        st.dataframe(df)
    else:
        st.error("Failed to fetch data from the API. Please check the dates and try again.")
