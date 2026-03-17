import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from weather import get_coordinates

def analyze_cities(city_names_list):
    """
    Analyze temperature volatility for a list of cities over the last 30 days.

    Args:
        city_names_list (list): List of 3 city names.

    Returns:
        tuple: (DataFrame with city statistics, matplotlib figure object)
    """
    if len(city_names_list) != 3:
        raise ValueError("Exactly 3 cities must be provided.")

    all_data = []

    for city in city_names_list:
        lat, lon, city_name = get_coordinates(city)
        if not lat or not lon or not city_name:
            raise ValueError(f"Could not find coordinates for city: {city}")

        # Fetch historical temperature data
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&past_days=30&daily=temperature_2m_max"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract daily data
        dates = data['daily']['time']
        temps = data['daily']['temperature_2m_max']

        # Add to all_data
        for date, temp in zip(dates, temps):
            all_data.append({
                'date': date,
                'city': city_name,
                'temperature': temp
            })

    # Create DataFrame
    df = pd.DataFrame(all_data)
    df['date'] = pd.to_datetime(df['date'])

    # Calculate statistics
    stats = df.groupby('city')['temperature'].agg(['mean', 'std', 'min', 'max']).reset_index()
    stats = stats.rename(columns={
        'mean': 'mean_temp',
        'std': 'std_temp',
        'min': 'min_temp',
        'max': 'max_temp'
    })

    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='city', y='temperature', ax=ax)
    ax.set_title('Temperature Distribution Comparison (Last 30 Days)')
    ax.set_xlabel('City')
    ax.set_ylabel('Temperature (°C)')

    return stats, fig