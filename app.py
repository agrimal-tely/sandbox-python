import streamlit as st
import requests
import random
import weather

def main():
    st.title("🌤️ Weather Dashboard")
    
    with st.sidebar:
        st.header("Location Input")
        city = st.text_input("City Name", value="New York")
    
    if st.button("Get Weather"):
        temp, wind = weather.get_weather(city)
        
        if temp is not None and wind is not None:
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("🌡️ Temperature", f"{temp}°C")
            
            with col2:
                st.metric("💨 Wind Speed", f"{wind} km/h")
        else:
            st.error("Could not fetch weather data. Please check the city name and try again.")
if __name__ == "__main__":
    main()