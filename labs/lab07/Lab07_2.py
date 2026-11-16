# Starting file for LAB 7-2
# CS31 Course
# Carlos Farias
# Date 11/15/2026

import csv

FILENAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return miles_driven

def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas used:\t"))) <= 0:
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def format_number(value):
    # show 225.0 as 225, but keep 18.5 and 13.24 as they are
    return str(int(value)) if value.is_integer() else str(value)

def read_trips():
    trips = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip blank lines
                    trips.append([float(row[0]), float(row[1]), float(row[2])])
    except FileNotFoundError:
        pass  # no file yet, so start with an empty list
    return trips

def write_trips(trips):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def list_trips(trips):
    print(f"{'Distance':<12}{'Gallons':<11}{'MPG'}")
    for trip in trips:
        miles, gallons, mpg = trip
        print(f"{format_number(miles):<12}{format_number(gallons):<11}{format_number(mpg)}")
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon Program")
    print()

    # load existing trips and display them before asking for new input
    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trips.append([miles_driven, gallons_used, mpg])
        write_trips(trips)  # save after every entry

        list_trips(trips)

        more = input("More entries? (y or n): ")

    print("Bye!")

if __name__ == "__main__":
    main()