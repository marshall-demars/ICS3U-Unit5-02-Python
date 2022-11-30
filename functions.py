#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program calculates area of triangle using functions


def area(base, height):
    # This function calculates the area of a triangle

    # Process
    area = (base * height) / 2

    # Output
    print("\nThe area of the triangle is {0} cm².".format(area))

    print("\nDone.")


def main():
    # This function gets user inputs and does try catch

    # Input
    base_as_string = input("Enter the base length of the triangle (cm): ")
    height_as_string = input("Enter the height of the triangle (cm): ")
    try:
        base_as_int = int(base_as_string)
        height_as_int = int(height_as_string)

        # Call functions
        area(base_as_int, height_as_int)

    except Exception:
        print("\nInvalid Input.")


if __name__ == "__main__":
    main()
