import psycopg2
import streamlit as st

conn = psycopg2.connect(host = st.secrets["db_credentials"]["host"],
                        port = st.secrets["db_credentials"]["port"],
                        database = st.secrets["db_credentials"]["dbname"],
                        user = st.secrets["db_credentials"]["user"],
                        password = st.secrets["db_credentials"]["password"]

)

cursor = conn.cursor()



