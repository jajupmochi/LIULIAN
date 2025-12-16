import streamlit as st
import requests
import json

API_BASE = "http://127.0.0.1:8000/api"

st.title("LIULIAN Reference Platform")

# Fetch plugin list
plugin_names = requests.get(f"{API_BASE}/visualize").json()  # 可调整为 /plugins endpoint
selected_plugin = st.selectbox("Select plugin", plugin_names)

st.header("Upload Data")
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])
if uploaded_file:
    data = json.load(uploaded_file)

st.header("Parameters")
params_input = st.text_area("JSON Parameters", "{}")
params = json.loads(params_input)

if st.button("Train"):
    resp = requests.post(f"{API_BASE}/train/{selected_plugin}", json={"data": data, "params": params})
    st.json(resp.json())

if st.button("Predict"):
    resp = requests.post(f"{API_BASE}/predict/{selected_plugin}", json={"data": data, "params": params})
    st.json(resp.json())

if st.button("Visualize"):
    results = {"dummy": "results"}  # replace with real prediction results
    resp = requests.get(f"{API_BASE}/visualize/{selected_plugin}", params={"results": json.dumps(results)})
    st.json(resp.json())
