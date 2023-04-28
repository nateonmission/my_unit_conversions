# US/Metric Conversions
This python script is a menu-driven program that allows the user to convert units of temperature, distance, weight, volume, speed, and energy. It also has an option to calculate gas prices in USD/Gallon and EUR/Liter.

# Requirements
- Python 3.x
- requests module (install using "pip install requests")
- SECRETS.py file in the same directory containing exchange_api_key variable

# Usage
- Run the program by running python main.py in the terminal or command prompt.
- Select an option from the main menu.
- Follow the on-screen prompts to input the values to be converted.
- The converted value will be displayed on the screen.
- To exit, select "0" from the main menu.

# Menu Options
- Temperature (Fahrenheit/Celsius)
- Short Distances (Feet/Inches & Meters)
- Long Distances (Miles & Kilometers)
- Weight (Stones/Pounds & Kilograms)
- Volume (Cups/Pints/Gallons & Liters)
- Speed (MPH & km/h)
- Energy (Calories & Joules)
- Gas Prices (USD/Gallon & EUR/Liter)

# Constants
- INCHES_IN_FOOT = 12
- POUNDS_IN_STONE = 7
- OUNCES_IN_POUNDS = 16
- GRAMS_IN_OUNCES = 28.3495
- OUNCE_IN_GRAM = 0.03527
- KJ_IN_KCAL = 0.239
- KCAL_IN_KJ = 4.184
- GALLON_IN_LITER = 0.26417
- LITERS_IN_GALLON = 3.78541178
- ONE_BASE_UNIT = 1
- FUEL_CACHE = {}

# Note
The SECRETS.py file containing the exchange_api_key variable is not included in the repository for security reasons. Please make sure to create this file and store the variable in it for the gas prices conversion option to work.