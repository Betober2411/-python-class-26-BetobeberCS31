# Starting file for LAB 3-1
# CS31 Course
# Carlos Farias
# Date 08/14/2026

#============================================
#        The Miles Per Gallon program
#============================================
# Practice program: use a while loop.

# display a welcome message
print("=" * 44)
print("        The Miles Per Gallon program")
print("=" * 44)

choice = "y"
while choice == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    # validate the entries
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate the results324
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 2)
        cost_per_mile = round(total_gas_cost / miles_driven, 2)

        # display the entries and the results
        print("_" * 44)
        print(f"Miles Driven:              {miles_driven:.2f}")
        print(f"Gallons of Gas Used:       {gallons_used:.2f}")
        print(f"Cost Per Gallon:           ${cost_per_gallon:.2f}")
        print()
        print(f"Miles Per Gallon:          {mpg:.2f}")
        print(f"Total Gas Cost:            ${total_gas_cost:.2f}")
        print(f"Cost Per Mile:             ${cost_per_mile:.2f}")

    # ask the user whether to repeat
    print()
    choice = input("Get entries for another trip (y/n)? ").strip().lower()
    while choice not in ("y", "yes", "n", "no"):
        choice = input("Please enter 'y' or 'n': ").strip().lower()
    if choice == "yes":
        choice = "y"
    print()

print("Bye!")