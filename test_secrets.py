import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_credentials"]["user"])
st.write("DB Name:", st.secrets["db_credentials"]["dbname"])
st.write("DB Host:", st.secrets["db_credentials"]["host"])
st.write("DB Port:", st.secrets["db_credentials"]["port"])
st.write("DB Password:", st.secrets["db_credentials"]["password"])


