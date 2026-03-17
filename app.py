import streamlit as st
import requests
import random
import weather
import analytics

def main():
    st.title("🌤️ Weather Dashboard")
    
    tab1, tab2 = st.tabs(["Current Weather", "Volatility Analytics"])
    
    with tab1:
        st.header("Current Weather")
        
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
                
                # Fake temperature trend for next 5 hours
                st.subheader("📈 Temperature Trend (Next 5 Hours)")
                hours = [f"{i+1}:00" for i in range(5)]
                # Generate fake temperatures around current temp
                temps = [temp + random.uniform(-3, 3) for _ in range(5)]
                
                # Create data for chart
                chart_data = {"Hour": hours, "Temperature (°C)": temps}
                st.line_chart(chart_data)
            else:
                st.error("Could not fetch weather data. Please check the city name and try again.")
    
    with tab2:
        st.header("Regional Volatility Analysis")
        
        cities_input = st.text_input("Enter 3 cities (comma-separated)", value="New York, London, Tokyo")
        
        if st.button("Analyze Volatility"):
            try:
                city_list = [city.strip() for city in cities_input.split(",")]
                if len(city_list) != 3:
                    st.error("Please enter exactly 3 cities separated by commas.")
                else:
                    stats_df, fig = analytics.analyze_cities(city_list)
                    
                    st.subheader("Temperature Statistics")
                    st.dataframe(stats_df)
                    
                    st.subheader("Temperature Distribution Comparison")
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()