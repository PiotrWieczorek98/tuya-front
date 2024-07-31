import streamlit as st
from streamlit_autorefresh import st_autorefresh
from auth import authorize
import elements

# Streamlit app title
st.title("🖥️ PC Power Consumption")
count = st_autorefresh(interval=10000, key="refresher")
# if not authorize():
#     st.stop()

#----------------
elements.show_current_power_usage()
elements.show_expected_power_cost()
elements.show_power_usage_by_hour()
#----------------

