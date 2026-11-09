#########################################################################
# Course: CS-31 Python Programming
# Project: Mad Libs or Insult/Compliment Story Generator
# Student: Carlos Farias
# Date 10/25/2026
#########################################################################
LINE = "=" * 56

def ask_yes_no(prompt):
    """Keep asking until the player enters y or n."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y" or answer == "n":
            return answer
        print("  Oops! Please enter y or n.")


def ask_number(prompt, low, high):
    """Keep asking until the player enters a whole number from low to high."""
    while True:
        text = input(prompt).strip()            # ``strip()`` removes spaces from both ends
        if text.lstrip("-").isdigit():          # ``lstrip("-")`` strips characters from the left side only. It lets negative numbers through the check
            value = int(text)                   # ``isdigit()`` It is only True if every character is a digit 0-9.
            if value >= low and value <= high:  # ``int(text)`` converts the string "7" into the number 7 for Ex.
                return value
            print(f"  That number must be between {low} and {high}.")
        else:
            print("  Please enter a whole number.")


def ask_word(prompt):
    """Keep asking until the player types something."""
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("  Don't leave it blank - be creative!")


def main():
    stories_created = 0

    print(LINE)
    print("   *** THE SILLY STORY MACHINE: A MAD LIBS GAME ***")
    print(LINE)

    play = ask_yes_no("\nWould you like to play (y/n)? ")
    if play == "n":
        print("\nMaybe next time. Goodbye!")
        return

    name = ask_word("\nFirst, what is your name? ")
    print(f"\nHello, {name}! Which story would you like to play?\n")

    while play == "y":
        print("   a. Result of today's game")            # History 1 Name
        print("   b. The Haunted Library\n")             # History 2 Name

        choice = input("What is your choice (a/b)? ").strip().lower()
        while choice != "a" and choice != "b":
            print("  Sorry, please choose a or b.")
            choice = input("What is your choice (a/b)? ").strip().lower()

        print("\nNow, let me get some information from you to make this")
        print("a fun story.\n")

        if choice == "a":
            friend = ask_word("1) What is the name of a friend? ")
            weekendday = ask_word("2) Give me a weekend day (Saturday/Sunday): ")
            dressed = ask_word("3) Give me a favorite color of sportswear: ")
            color = input("4) Choose a color (red/yellow): ").strip().lower()
            while color != "red" and color != "yellow":
              print("  Sorry, please choose red or yellow.")
              color = input("4) Choose a color card (red/yellow): ").strip().lower()
            grandstands = ask_number("5) Give me a number from 1 to 4: ", 1, 4)
            sport = ask_word("6) Give me the name of your favorite sport: ")
            coach_name = ask_word("7) Give me the name of your coach that you remember.: ")

            title = "Result of today's game"
            story = (
                f"It was a very sunny {weekendday}, and the stadium had {grandstands} "
                f"grandstands. {friend}'s team arrived late to the match. "
                f"The match started, and in the second half, "
                f"the referee dressed in {dressed}, gave me a {color} card, "
                f"So I got really upset. But then I was happy we won "
                f"The match. {friend} asked me why our team played in {color} "
                f"jerseys, and I replied that it was Coach "
                f"{coach_name}’s decision."
            )
        else:
            teacher = ask_word("1) Give me the name of a teacher or celebrity: ")
            color = ask_word("2) Give me a color: ")
            past_verb = ask_word("3) Give me a past-tense verb: ")
            body_part = ask_word("4) Give me a body part: ")
            age = ask_number("5) Give me a number from 1 to 100: ", 1, 100)
            animal = ask_word("6) Give me a type of animal: ")
            emotion = ask_word("7) Give me an emotion: ")
            sound = ask_word("8) Give me a sound (like BOOM or SPLAT): ")

            title = "The Haunted Library"
            story = (
                f"Late one night, you sneak into the library with "
                f"{teacher}. A {color} ghost floats out from behind the "
                f"shelves and {past_verb} right in front of you! "
                f"It taps your {body_part} and says it has been haunting "
                f"the library for {age} years. Suddenly a giant {animal} "
                f"crashes through the window with a loud {sound}. "
                f"Everyone feels {emotion}, but the ghost just laughs and "
                f"reads you a bedtime story."
            )

        print(f"\n{name}, here is your story:\n")
        print(LINE)
        print(f"   {title}")
        print(LINE)

        # Wrap the story so it looks neat on screen
        words = story.split()                       # ``split()`` breaks a string into a list of words. The loop builds a line word by word and starts a new line before it passes about 54 characters.
        current = ""
        for word in words:
            if len(current) + len(word) + 1 > 54:
                print("  " + current)
                current = word
            elif current == "":
                current = word
            else:
                current = current + " " + word
        print("  " + current)
        print(LINE)

        stories_created += 1
        if stories_created == 1:
            print(f"\nYou have created {stories_created} story.")
        else:
            print(f"\nYou have created {stories_created} stories.")

        play = ask_yes_no("Would you like to play again (y/n)? ")
        if play == "y":
            print(f"\nGreat, {name}! Which story would you like this time?\n")

    print(f"\nThanks for playing, {name}! You made {stories_created} "
          f"story/stories. Goodbye!")


main()