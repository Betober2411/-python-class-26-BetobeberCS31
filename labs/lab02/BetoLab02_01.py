# Starting file for LAB 2
# CS31 Course
# Carlos Farias
# Date 08/10/2026

# ============================================
#        THE QUICK MATH QUIZ CHALLENGE
# ============================================
# Practice program: if / elif / else statements

print("=" * 44)
print("        THE QUICK MATH QUIZ CHALLENGE")
print("=" * 44)

# Ask for the user's name and greet them
name = input("What is your name? ").strip()
print(f"\nWelcome, {name}! Let's see how sharp your math skills are.")

# Ask if the user wants to take the quiz
choice = input("\nWould you like to take the quiz? (yes/no): ").strip().lower()

if choice == "yes" or choice == "y":
    # Counter for correct answers
    score = 0

    print(f"\nGreat, {name}! Enter your answers as NUMBERS only (example: 10).\n")

    # ---------- Question 1 ----------
    print("1) What is 5 + 5?")
    answer1 = float(input("Your answer: "))
    if answer1 == 10:
        score += 1
        print("Correct! 5 + 5 = 10\n")
    else:
        print("Incorrect. The correct answer is 10.\n")

    # ---------- Question 2 ----------
    print("2) What is 10 x 15?")
    answer2 = float(input("Your answer: "))
    if answer2 == 150:
        score += 1
        print("Correct! 10 x 15 = 150\n")
    else:
        print("Incorrect. The correct answer is 150.\n")

    # ---------- Question 3 ----------
    print("3) What is 30 / 3?")
    answer3 = float(input("Your answer: "))
    if answer3 == 10:
        score += 1
        print("Correct! 30 / 3 = 10\n")
    else:
        print("Incorrect. The correct answer is 10.\n")

    # ---------- Question 4 ----------
    print("4) What is 1500 / 10?")
    answer4 = float(input("Your answer: "))
    if answer4 == 150:
        score += 1
        print("Correct! 1500 / 10 = 150\n")
    else:
        print("Incorrect. The correct answer is 150.\n")

    # ---------- Question 5 ----------
    print("5) What is 33 * 11?")
    answer5 = float(input("Your answer: "))
    if answer5 == 363:
        score += 1
        print("Correct! 33 * 11 = 363\n")
    else:
        print("Incorrect. The correct answer is 363.\n")

    # ---------- Final score ----------
    print("=" * 44)
    print(f"{name}, your final score is {score}/5")
    print("=" * 44)

    # Personalized feedback
    if score == 5:
        print("Amazing job! You're a rockstar.")
    elif score == 4:
        print("Great job! Almost 100%.")
    elif score == 2 or score == 3:
        print("Keep studying!")
    else:
        print("Maybe this isn't your main area of interest?")

    print(f"\nThanks for playing, {name}. See you next time!")

else:
    print(f"\nMaybe next time, {name}!")