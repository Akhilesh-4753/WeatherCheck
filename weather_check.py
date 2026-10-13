import requests

API_KEY = "7400e3e8e110d82f31c6ec4e4416632f"

url = "https://api.openweathermap.org/data/2.5/weather"

location = input("Enter city, district, or state name: ").strip()

if not location:
    print("Please enter a location.")

else:

    params = {
        "q": f"{location},IN",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print("\n=== Current Weather ===")
            print("Location:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Condition:", data["weather"][0]["description"].title())
            print("Wind speed:", data["wind"]["speed"], "m/s")

        else:
            print(data.get("message"))

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")
