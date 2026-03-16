import requests

def get_weather(city_name):
    # 1. Coordinates for Alcorcón, Madrid (as an example)
    # In a real app, you'd use a Geocoding API to turn 'city_name' into these numbers
    lat, lon = 40.35, -3.82 
    
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
        
        print(f"🌡️  Current temperature in {city_name}: {temp}°C")
        print(f"💨 Wind speed: {wind} km/h")

    except Exception as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    city = input("Enter a city to check (Default: Alcorcón): ") or "Alcorcón"
    get_weather(city)