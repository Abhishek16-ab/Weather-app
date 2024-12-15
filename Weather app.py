import requests
import json
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# User inputs city name
city = input("Enter the name of the city: ")
# Replace YOUR_API_KEY with the API key you obtained from WeatherAPI
url = f"https://api.weatherapi.com/v1/current.json?key=46b10c7ed4d54d599fb63950241512&q={city}"

# Make the API request
response = requests.get(url)
data = json.loads(response.text)

# Extract weather information
temperature = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]

# Print the weather information
print(f"The current temperature in {city} is {temperature}°C with {condition}.")

# Use text-to-speech to announce the weather
engine.say(f"The current temperature in {city} is {temperature} degrees Celsius with {condition}.")
engine.runAndWait()
