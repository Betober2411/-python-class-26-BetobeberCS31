# Starting file for LAB 6-2
# CS31 Course
# Carlos Farias
# Date 11/05/2026

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            # movie[2] is the new price column.
            # :.2f keeps two decimal places (e.g. 9.95, 14.95).
            print(f"{i}. {movie[0]} ({movie[1]}) $ {movie[2]:.2f}")
        print()
 
def is_price(text):
    # A price is valid if it is digits with at most one decimal point,
    # such as "14.95" or "15". Removing one "." and checking isdigit()
    # does this without try/except.
    return text.replace(".", "", 1).isdigit()
 
def add(movie_list):
    name = input("Name: ")
 
    # Keep asking until the year is made of digits only.
    while True:
        year = input("Year: ")
        if year.isdigit():
            year = int(year)
            break
        else:
            print("Invalid year. Please enter a whole number.")
 
    # prompt for the price and store it as the 3rd column.
    while True:
        price = input("Price: ")
        if is_price(price):
            price = float(price)
            break
        else:
            print("Invalid price. Please enter a number.")
 
    movie = [name, year, price]          # now a 3-column row
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")

 
def delete(movie_list):
    text = input("Number: ")
    if not text.isdigit():
        print("Invalid movie number.\n")
        return
    number = int(text)
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie[0]} was deleted.\n")
 
def find(movie_list):
    # find movies by year.
    text = input("Year: ")
    if not text.isdigit():
        print("Invalid year.\n")
        return
    year = int(text)
 
    found = False
    for movie in movie_list:
        if movie[1] == year:             # compare against the year column
            print(f"{movie[0]} was released in {movie[1]}.")
            found = True
    if not found:
        print(f"No movies were released in {year}.")
    print()
 
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("find - Find movies by a year")   # new menu item
    print("exit - Exit program")
    print()

 
def main():
    # each starting movie now includes a price as the 3rd item.
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954, 5.59],
                  ["Cat on a Hot Tin Roof", 1958, 7.95]]
    display_menu()
 
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "find":   # new command
            find(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
  
if __name__ == "__main__":
    main()