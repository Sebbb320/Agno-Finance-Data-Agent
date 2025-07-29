import streamlit as st
import os

st.title("Hello Railway!")
st.write("If you can see this, the deployment is working!")
st.write("Port:", os.getenv("PORT", "8501"))
st.write("Environment:", os.getenv("RUNTIME_ENV", "production")) 