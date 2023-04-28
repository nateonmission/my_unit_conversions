import os
import math
from fractions import Fraction
import tracemalloc
import requests
import json

from SECRETS import exchange_api_key

INCHES_IN_FOOT = 12
POUNDS_IN_STONE = 7
OUNCES_IN_POUNDS = 16
GRAMS_IN_OUNCES = 28.3495
OUNCE_IN_GRAM = 0.03527
KJ_IN_KCAL = 0.239
KCAL_IN_KJ = 4.184
GALLON_IN_LITER = 0.26417
LITERS_IN_GALLON = 3.78541178
ONE_BASE_UNIT = 1
FUEL_CACHE = {}

def menu():
    os.system('cls')
    print("***** US/Metric Conversions *****")
    print("1. Temperature")
    print("2. Short Distances (Feet/Inches & Meters)")
    print("3. Long Distances (Miles & Kilometers)")
    print("4. Weight (Stones/Pounds & Kilograms)") 
    print("5. Volume (Cups/Pints/Gallons & Liters)") # TODO
    print("6. Speed (MPH & km/h") # TODO
    print("7. Energy (Calories & Joules)")
    print("")
    print("*****  *****")
    print("")
    print("")
    print("*****  *****")
    print("")
    print("***** Complex Calulations *****")
    print("10. Gas USD/Gallon & EUR/Liter")
    print("0. Exit")
    response = input("Please make a selection: ")
    if response == "1":
        temp_convert()
    elif response == "2":
        short_distance_convert()
    elif response == "3":
        long_distance_convert()
    elif response == "4":
        weight_convert()
    elif response == "7":
        energy_convert()
    elif response == "10":
        gas_price_convert()
    elif response == "0":
        return 0
    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        return 1

# 1
def temp_convert():
    os.system('cls')
    print("***** F/C Conversion *****")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        response = input("Enter your Fahrenheit temperature: ")
        c = (( float(response)-32)*5)/9
        print("")
        print(f"{response} F is {c} C")
    elif response == "2":
        response = input("Enter your Celsius temperature: ")
        f = ((float(response)*(9/5))+32)
        print("")
        print(f"{response} C is {f} F")
    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
    return 0

# 2
def short_distance_convert():
    os.system('cls')
    print("***** Short Distance Conversion *****")
    print("1. Feet/Inches to Meters")
    print("2. Meters to Feet/Inches")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        feet = input("Enter your Feet (enter 0 if there is none): ")
        inches = input("Enter your Whole Inches (enter 0 if there is none): ")
        fraction = input("Enter your Inch Fraction (enter 0 if there is none): ").split('/')
        if len(fraction) > 1:
            decimal_inch = float(fraction[0])/float(fraction[1])
        else:
            decimal_inch = 0

        meters = round((float(feet) * 0.3048) + ((float(inches) + decimal_inch) * 0.0254),3)
        print("")
        print(f"{feet}' {inches}\" is {meters} m")

    elif response == "2":
        meters = input("enter your distance/length in meters: ")
        total_in_inches = float(meters) / 0.0254
        feet = math.floor(total_in_inches / INCHES_IN_FOOT)
        total_inches = total_in_inches - (feet * INCHES_IN_FOOT)
        int_inches = int(total_inches) 
        fraction_inch = str(Fraction(round((total_inches - int_inches)/0.125)*0.125).limit_denominator())

        print("")
        print(f"{meters} m is {feet} ft {int(int_inches)} {fraction_inch} ins ")

    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
    return 0

# 3
def long_distance_convert():
    os.system('cls')
    print("***** Short Distance Conversion *****")
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        miles = input("Enter your Miles (enter 0 if there is none): ")
        fraction = input("Enter your Fraction of a mile (enter 0 if there is none): ").split('/')
        if len(fraction) > 1:
            str_fraction = f" and {fraction[0]}/{fraction[1]} miles"
        else:
            str_fraction = " miles"
        if len(fraction) > 1:
            decimal_of_mile = float(fraction[0])/float(fraction[1])
        else:
            decimal_of_mile = 0
        decimal_mile = int(miles) + decimal_of_mile

        kilometers = round((float(decimal_mile) * 1.609344),3)
        print("")
        print(f"{miles}{str_fraction} is {kilometers} km")

    elif response == "2":
        kilometers = input("enter your distance/length in kilometers: ")
        decimal_miles = float(kilometers) * 0.6213711
        decimal_of_miles = decimal_miles - int(decimal_miles)
        fraction_miles = Fraction(round((decimal_of_miles)/0.125)*0.125).limit_denominator()
        str_fraction_miles = str(fraction_miles)
        
        if fraction_miles < 0.125:
            str_fraction = ""
        else:
            str_fraction = f"and {str_fraction_miles} "

        print("")
        print(f"{kilometers} km is {int(decimal_miles)} {str_fraction}miles ")

    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
    return 0

# 4
def weight_convert():
    os.system('cls')
    print("***** Weight Conversion *****")
    print("1. Stone/Pounds/Onces to Kilograms")
    print("2. Kilograms to Stone/Pounds/Onces")
    print("3. Ounces to Grams") # TODO
    print("4. Grams to Onces") # TODO
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        stones = input("Enter Stones (0 if not used): ")
        pounds = input("Enter Pounds (0 if none): ")
        ounces = input("Enter Ounces (0 if none): ")
        decimal_pounds = int(pounds) + int(stones)*7 + int(ounces)*0.0625
        kg = round(decimal_pounds * 0.45359, 3)
        if float(stones) > 0:
            str_stones = f"{stones} Stones"
        else:
            str_stones = ""
        if float(pounds) > 0:
            str_pounds = f"{pounds} Pounds"
        else:
            str_pounds = ""
        if float(ounces) > 0:
            str_ounces = f"{ounces} Ounces "
        else:
            str_ounces = ""
        print("")
        print(f"{str_stones} {str_pounds} {str_ounces}is {kg} kg ")

    elif response == "2":
        kilograms = input("enter kilograms: ")
        decimal_pounds = float(kilograms) * 2.20452
        display_decimal_pounds = round(decimal_pounds,2)
        int_total_pounds = int(decimal_pounds)
        decimal_of_pounds = decimal_pounds - int_total_pounds
        ounces = round(decimal_of_pounds * 0.0625,2)
        stones = int(decimal_pounds/POUNDS_IN_STONE)
        pounds_after_stones = int_total_pounds - (stones * POUNDS_IN_STONE)
        
        print(f"Given {kilograms} kg,")
        print(f"you have {stones} stones, {pounds_after_stones} pounds, {ounces} ounces")
        print("or")
        print(f"you have {int_total_pounds} pounds {ounces} ounces")
        print("or")
        print(f"you have {display_decimal_pounds} pounds.")

    elif response == "3":
        ounces = input("Enter Ounces (0 if none): ")   
        grams = round(int(ounces) * GRAMS_IN_OUNCES, 3)
        print(f"{ounces} ounces is {grams} grams")

    elif response == "4":
        grams = input("Enter Grams (0 if none): ")
        ounces = round(int(grams) * OUNCE_IN_GRAM, 3)
        print(f"{grams} grams is {ounces} ounces")

    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
    return 0

# 5
def volume_convert():
    pass

# 6 
def speed_conver():
    pass

# 7
def energy_convert():
    os.system('cls')
    print("***** Energy Conversion *****")
    print("")
    print("-- Calories and Joules (both with capital letters) are actually 1000 calories and joules.")
    print("-- Technically Calories and Joules are kilocalories (kcals) and kilojoules (kJ)")
    print("")
    print("1. Kcals to kJ")
    print("2. kJ to Kcals")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        Kcals = input("Enter your Kcals amount: ")
        kJ = round(float(Kcals) * KCAL_IN_KJ, 3)
        print("")
        print(f"{Kcals} Kcals is {kJ} kJ")
    elif response == "2":
        kJ = input("Enter your kJ amount: ")
        Kcals = round(float(kJ) * KJ_IN_KCAL, 3)
        print("")
        print(f"{kJ} kJ is {Kcals} Kcals")
    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
    return 0

def _get_rates(params: dict = {"base": "USD", "symbols": "EUR,GBP,CAD,AUD,MXN"}):
    global FUEL_CACHE
    url = 'https://api.apilayer.com/exchangerates_data/latest'
    payload = {}
    headers = {"apikey": exchange_api_key}
    params = params
    if 'USD' in FUEL_CACHE:
        return FUEL_CACHE
    else:
        res = requests.request("GET", url, params = params, headers = headers, data = payload)
        data = json.loads(res.text)
        if data['success'] == True:
            FUEL_CACHE = data['rates']
            rates = data['rates']
            return rates
        else:
            return {"status": "ERROR"}


# XX
def gas_price_convert():
    os.system('cls')
    print("***** Money/Unit Conversion *****")
    print("")
    print("1. USD per Gal to GBP/CAD/AUD/MXN per liter")
    print("2. from GBP/L to others")
    print("3. from CAD/L to others")
    print("4. from AUD/L to others")
    print("5. from MXN/L to others")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        rates = _get_rates()
        USD_per_gallon = input("How much does a gallon of gas cost, in USD? ")
        os.system('cls')
        for currency, rate_per_dollar in rates.items():
            price_per_liter = round(float(USD_per_gallon) * GALLON_IN_LITER / (ONE_BASE_UNIT / rate_per_dollar), 2)
            print(f"${float(USD_per_gallon)} per gallon is {price_per_liter} {currency} per liter")
        input("Press ENTER to continue....")
        return 0

    elif response == "2":
        base_currency = "GBP"
    elif response == "3":
        base_currency = "CAD"
    elif response == "4":
        base_currency = "AUD"
    elif response == "5":
        base_currency = "MXN"

    params = {"base": base_currency, "symbols": "AUD,CAD,EUR,GBP,MXN,USD"}
    rates = _get_rates(params)
    rate_per_dollar = rates['USD']
    cost_per_litre = input(f"How much does a litre of petrol cost, in {base_currency}? ")
    dollars_per_gallon = round(float(cost_per_litre) * LITERS_IN_GALLON * rate_per_dollar, 2)
    os.system('cls')
    print(f"{float(cost_per_litre)} / litre is {dollars_per_gallon} USD per gallon")

    for currency, x_rate in rates.items():
        if currency == base_currency:
            continue
        else:
            currency_per_liter = round(float(cost_per_litre) / ( ONE_BASE_UNIT / x_rate), 2)
            print(f"{float(cost_per_litre)} / litre is {currency_per_liter} {currency} per liter")

    # print(data)
    input("Press ENTER to continue....")
    return 0


def main():
    again = True
    while again:
        return_value = menu()
        if return_value == 0:
            again = False
    print("Goodbye!")
    return 0

if __name__ == "__main__":
    tracemalloc.start()
    main()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()