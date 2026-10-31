# Starting file for LAB 5-1
# CS31 Course
# Carlos Farias
# Date 10/30/2026

import nameformat

def main():
    # Program title
    nameformat.hello_world()
    print("Welcome to the Name Format module program")
    print()

    # Ask for first/last name
    firstName = input("What is your first name? ").strip()
    lastName = input("What is your last name? ").strip()
    print()

    # Menu system
    while True:
        print("* * MENU * *")
        print("1 - Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - View Documentation")
        print("5 - Exit Program")
        choice = input("What would you like to do? ").strip()
        print()

        if choice == "1":
            nameformat.sayHello(firstName)

        elif choice == "2":
            nameformat.fullName(firstName, lastName)

        elif choice == "3":
            nameformat.lastNameFirst(firstName, lastName)

        elif choice == "4":
            nameformat.documentation()

        elif choice == "5":
            print("Thank you for using our program.")
            break

        else:
            print("Sorry, invalid input. Please try again.")
            print()


# If started as the main module, call the main function
if __name__ == "__main__":
    main()