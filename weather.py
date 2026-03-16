import requests

def get_coordinates(city_name):
    # The Geocoding Endpoint
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Return latitude, longitude and name (if found)
    if "results" in data:
        result = data["results"][0]
        return result["latitude"], result["longitude"], result["name"]
    else:
        return None, None, None
    
def get_weather(city_name):
    # 1. Get Coordinates (Latitude and Longitude)
    lat, lon, city = get_coordinates(city_name)
    if not lat or not lon or not city:
        print(f"❌ City not found: {city_name}")
        return

    # 2. The Endpoint (The URL we 'call')
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        # 3. The Request
        response = requests.get(url)
        
        # 4. Error Handling (The 'Defensive' Mindset)
        response.raise_for_status() 
        
        # 5. Parsing JSON (Modern Python dictionaries)
        data = response.json()
        temp = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']
        
        print(f"🌡️  Current temperature in {city}: {temp}°C")
        print(f"💨 Wind speed: {wind} km/h")

    except Exception as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    city = input("Enter a city to check: ")
    get_weather(city)