# Starting file for LAB 7-1
# CS31 Course
# Carlos Farias
# Date 11/15/2026

import csv

FILENAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven

def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = []  # two-dimensional list: each row is [miles, gallons, mpg]

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trips.append([miles_driven, gallons_used, mpg])

        more = input("More entries? (y or n): ")

    # save data only after the user has finished entering values
    write_trips(trips)

    print("Bye!")

if __name__ == "__main__":
    main()