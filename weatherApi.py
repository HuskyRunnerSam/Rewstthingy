import requests

def get_weather(api_key, zip_code, units):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "zip": zip_code,
        "appid": api_key,
        "units": units,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data.get("main", {}).get("temp")
        condition = weather_data.get("weather", [{}])[0].get("description")

        unit_label = "Celsius" if units == "metric" else "Fahrenheit"
        return f"The current temperature in {zip_code} is {temperature}° {unit_label}. {condition.capitalize()}."
    else:
        return f"Failed to retrieve weather data. Status code: {response.status_code}"

def main():
    while True:
        print("Welcome to the Weather App!")
        name = input("What's your name? ")
        zip_code = input("Please enter your zip code: ")

        unit_choice = input("Enter 'f' for Fahrenheit or 'c' for Celsius: ").lower()
        while unit_choice not in ['f', 'c']:
            unit_choice = input("Invalid choice. Enter 'f' for Fahrenheit or 'c' for Celsius: ").lower()

        units = "imperial" if unit_choice == 'f' else "metric"

        # Ideally we would not store the API key in plain text
        api_key = "0ebd3595629f989f2bf8e2a953b1c052"

        weather_info = get_weather(api_key, zip_code, units)
        print(f"Hello, {name}! {weather_info}")

        exit_choice = input("Do you want to exit? (yes/no): ").lower()
        if exit_choice == 'yes':
            print("Goodbye! Thank you for using the Weather App.")
            break

if __name__ == "__main__":
    main()