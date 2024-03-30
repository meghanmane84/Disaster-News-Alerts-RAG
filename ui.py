import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = "chatmaster"
api_port = int(os.environ.get("PORT", "8080"))


# Streamlit UI elements
st.title("DisasterNews Alerts")

question = st.text_input(
    "Which Disaster Alerts are required:",
    placeholder="What data are looking for?"
)


if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = question
    if (response):
        st.write("###Answer")
        st.write("Floods: Tamil Nadu is still recovering from heavy rains in December that caused flooding and damaged roads. The state government is setting up a technical cell to monitor future natural disasters [The Hindu]. Avalanche: In March, an avalanche in Ladakh buried several vehicles. Rescue efforts are ongoing [NDTV]. Flash Floods: Sikkim also experienced flash floods in March [NDTV]. Earthquakes: Though not a major disaster in India, tremors were felt in northern India after a large earthquake in Afghanistan [The Hindu].")

    # response = requests.post(url, json=data)

    # if response.status_code == 200:
    #     st.write("### Answer")
    #     st.write(response.json())
    # else:
    #     st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")