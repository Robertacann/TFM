import streamlit as st
import requests

st.title("Consulta API Amazon - RapidAPI")

url = "https://real-time-amazon-data.p.rapidapi.com/search"

querystring = {
    "category_id": "281407",
    "country": "US",
    "brand": "SAMSUNG",
    "page": "1"
}

headers = {
    "X-RapidAPI-Key": "3f83c08e43mshe4004567e170a7ap1fbb64jsn81b327923d54",
    "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    st.success("Datos obtenidos correctamente")
    st.json(data) 
else:
    st.error(f"Error: {response.status_code}")
    st.text(response.text)
