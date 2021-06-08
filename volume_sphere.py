#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 8, 2021
# This program uses user defined functions to calculate the volume of a sphere

import math


def calculate(operator, num_int):
    result = float(-1)
    if operator == "volume":
        result = 4/3*math.pi*(num_int**3)
    elif operator == "area":
        result = 4*math.pi*num_int
    else:
        result = float(-1)
    return result


def main():
    while True:
        # ask the user whether they wish to have the volume or area
        quantity = input("Please type in whether you'd like to calculate the"
                          " volume or the area (type 'volume' or 'area'): ")

        # these two function asks for the radius from the user
        if (quantity == "volume"):
            print("Today, we will calculate the volume of a sphere")
            print("")
            while True:
                radius_from_user_string = input("Enter the radius"
                                                " of a sphere (cm): ")

    # make sure if the user types anything but an integer, it's not valid
                try:
                    radius_from_user_int = float(radius_from_user_string)
                    print("")
                    if (radius_from_user_int <= 0):
                        print("{} is not a"
                              " positive number". format(radius_from_user_int))
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number")

            results = calculate(quantity, radius_from_user_int)
            print("The volume is {:.2f} cm^3". format(results))
        elif (quantity == "area"):
            print("Today, we will calculate the area of a sphere")
            print("")
            while True:
                radius_from_user_string = input("Enter the radius"
                                                " of a sphere (cm): ")

    # make sure if the user types anything but an integer, it's not valid
                try:
                    radius_from_user_int = float(radius_from_user_string)
                    print("")
                    if (radius_from_user_int <= 0):
                        print("{} is not a"
                              " positive number". format(radius_from_user_int))
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number")

            results = calculate(quantity, radius_from_user_int)
            print("The area is {:.2f} cm^2". format(results))
        else:
            print("Invalid Input")
            continue


if __name__ == "__main__":
    main()
