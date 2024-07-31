import requests
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
URL = st.secrets.env["URL"]
AUTH_TOKEN = st.secrets.env["AUTH_TOKEN"]
HEADERS = {'content-type': 'application/json', 'Authorization': AUTH_TOKEN}

def response_handler(response: requests.Response):
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


def fetch_power_usage_now():
    response = requests.get(f"{URL}/api/power-usage/now", headers=HEADERS)
    return response_handler(response)

def fetch_power_usage_hourly():
    response = requests.get(f"{URL}/api/power-usage/hourly", headers=HEADERS)
    return response_handler(response)

def fetch_power_usage_monthly():
    response = requests.get(f"{URL}/api/power-usage/monthly", headers=HEADERS)
    return response_handler(response)

def fetch_power_usage_yearly():
    response = requests.get(f"{URL}/api/power-usage/yearly", headers=HEADERS)
    return response_handler(response)

def fetch_energy_price_for_day(date: datetime):
    response = requests.get(f"{URL}/api/energy-price/day", params={'date': date}, headers=HEADERS)
    return response_handler(response)

def fetch_energy_price_monthly():
    response = requests.get(f"{URL}/api/energy-price/monthly", headers=HEADERS)
    return response_handler(response)

