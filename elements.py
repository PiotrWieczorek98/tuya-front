import datetime
from dateutil.relativedelta import relativedelta
import data_fetcher
import plotly.express as px
import pandas as pd
import streamlit as st
import utils

# Fetch data
power_usage_now = data_fetcher.fetch_power_usage_now()
energy_price_monthly = dict(data_fetcher.fetch_energy_price_monthly())
power_usage_hourly = data_fetcher.fetch_power_usage_hourly()
power_usage_monthly = data_fetcher.fetch_power_usage_monthly()
power_usage_yearly = data_fetcher.fetch_power_usage_yearly()

def show_current_power_usage():
    st.subheader("Power usage now:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current", f"{power_usage_now['current']} A")
    with col2:
        st.metric("Voltage", f"{power_usage_now['voltage']} V")
    with col3:
        st.metric("Power", f"{power_usage_now['power']} W")

def show_expected_power_cost():
    st.subheader("Expected cost:")

    cur_month = datetime.datetime.now().replace(day=1)
    prev_month = cur_month - relativedelta(months=1)
    cur_year = cur_month.replace(month=1)
    prev_year = cur_year - relativedelta(years=1)

    cost_cur_month = cost_prev_month = total_cost = 0
    for entry in power_usage_monthly:
        if entry["date"] == cur_month.strftime('%Y-%m-%d'):
            cost_cur_month = entry["cost"]
        elif entry["date"] == prev_month.strftime('%Y-%m-%d'):
            cost_prev_month = entry["cost"]
        total_cost += entry["cost"]

    cost_cur_year = cost_prev_year = 0
    for entry in power_usage_yearly:
        if entry["date"] == cur_year.strftime('%Y-%m-%d'):
            cost_cur_year = entry["cost"]
        elif entry["date"] == prev_year.strftime('%Y-%m-%d'):
            cost_prev_year = entry["cost"]

    col1, col2, col3 = st.columns(3)
    with col1:
        delta = f"{round(cost_cur_month - cost_prev_month, 2)} zł" if cost_prev_month else None
        st.metric("This month", f"{cost_cur_month} zł", delta, "inverse")
    with col2:
        delta = f"{round(cost_cur_year - cost_prev_year, 2)} zł" if cost_prev_year else None
        st.metric("This year", f"{cost_cur_year} zł", delta, "inverse")
    with col3:
        st.metric("Total", f"{round(total_cost, 2)} zł")

def show_power_usage_by_hour():
    data = [
        {
            "Date": utils.convert_datetime_to_local(entry["date"] + f" {entry['hour']}:00", '%Y-%m-%d %H:%M'),
            "Total Energy (Wh)": entry["energy_w"]
        }
        for entry in power_usage_hourly
    ]

    df = pd.DataFrame(data)
    fig = px.line(
        df,
        x="Date",
        y="Total Energy (Wh)",
        title="Power Usage Graph",
        markers=True,
        line_shape="spline"
    )
    fig.update_layout(xaxis_title="Date", yaxis_title="Total Energy (Wh)")
    st.plotly_chart(fig)