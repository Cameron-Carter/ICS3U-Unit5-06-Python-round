#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program rounds a number

import string


def round_number(number):
    # Changes rounding by reference

    # Process and output
    number[0] = number[0] * (10 ** number[1]) + 0.5
    number[0] = int(number[0])
    number[0] = number[0] * (10 ** (-1 * number[1]))

    return 0;


def main():
    # This function calls format_address

    number_as_list = []
    # Input
    input_number = input("Enter a number to round: ")
    input_decimals = input("Enter how many decimal places to round to: ")

    # Process and output
    try:
        number_float = float(input_number)
        decimals_integer = int(input_decimals)
        if decimals_integer >= 0:
            number_as_list.append(number_float)
            number_as_list.append(decimals_integer)

            # Call round_number
            round_number(number_as_list)
            print("The rounded number is {}".format(number_as_list[0]))
        else:
            print("Invalid input.")
    except Exception:
        print("Invalid input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
