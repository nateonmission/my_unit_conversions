import os
import math
from fractions import Fraction
import tracemalloc

POUNDS_IN_STONE = 7
OUNCES_IN_POUNDS = 16

def menu():
    os.system('cls')
    print("***** US/Metric Conversions *****")
    print("1. Temperature")
    print("2. Short Distances (Feet/Inches & Meters)")
    print("3. Long Distances (Miles & Kilometers)")
    print("4. Weight (Stones/Pounds & Kilograms)") # TODO
    print("5. Volume (Cups/Pints/Gallons & Liters)") # TODO
    print("6. Speed (MPH & km/h") # TODO
    print("7. Energy (Calories & Joules)") #TODO
    print("")
    print("*****  *****")
    print("")
    print("")
    print("*****  *****")
    print("")
    print("***** Complex Calulations *****")
    print("XX. Gas USD/Gallon & EUR/Liter") #TODO
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
    elif response == "0":
        return 0
    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        return 1


def temp_convert():
    os.system('cls')
    print("***** F/C Conversion *****")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        response = input("enter your Fahrenheit temperature: ")
        c = (( float(response)-32)*5)/9
        print("")
        print(f"{response} F is {c} C")
    elif response == "2":
        response = input("enter your Celsius temperature: ")
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

def short_distance_convert():
    os.system('cls')
    print("***** Short Distance Conversion *****")
    print("1. Feet/Inches to Meters")
    print("2. Meters to Feet/Inches")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        feet = input("enter your Feet (enter 0 if there is none): ")
        inches = input("enter your Whole Inches (enter 0 if there is none): ")
        fraction = input("enter your Inch Fraction (enter 0 if there is none): ").split('/')
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
        feet = math.floor(total_in_inches / 12)
        total_inches = total_in_inches - (feet*12)
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

def long_distance_convert():
    os.system('cls')
    print("***** Short Distance Conversion *****")
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")
    print("")
    response = input("Please make a selection: ")
    if response == "1":
        miles = input("enter your Miles (enter 0 if there is none): ")
        fraction = input("enter your Fraction of a mile (enter 0 if there is none): ").split('/')
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
        stones = input("enter Stones (0 if not used): ")
        pounds = input("enter Pounds (0 if none): ")
        ounces = input("enter Ounces (0 if none): ")
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

    else:
        print("")
        print("Invalid input. please enter a number from the menu.")
        input("Press ENTER to continue.")
        temp_convert()
    print("")
    input("Press ENTER to continue.")
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