# Starting file for LAB 2
# CS31 Course
# Carlos Farias
# Date 08/10/2026

# ============================================
#        THE GENERAL KNOWLEDGE QUIZ
# ============================================
# Practice program: if / elif / else statements

print("=" * 44)
print("        THE GENERAL KNOWLEDGE QUIZ")
print("=" * 44)

# Ask for the user's name and greet them
name = input("What is your name? ").strip()
print(f"\nHello, {name}! Ready to test your knowledge?")

# Ask if the user wants to take the quiz
choice = input("\nWould you like to take the quiz? (yes/no): ").strip().lower()

if choice == "yes" or choice == "y":
    # Counter for correct answers
    score = 0

    print(f"\nLet's go, {name}! Type A, B, C, or D for each question.\n")

    # ---------- Question 1 ----------
    print("1) Which war started in 1939 and ended in 1945?")
    print("   a. Vietnam War")
    print("   b. World War I")
    print("   c. World War II")
    print("   d. Civil War")
    answer1 = input("Choose A/B/C/D: ").strip().upper()
    if answer1 == "C":
        score += 1
        print("Correct! It was World War II.\n")
    else:
        print("Incorrect. The correct answer is C (World War II).\n")

    # ---------- Question 2 ----------
    print("2) What is the capital of France?")
    print("   a. Paris")
    print("   b. Madrid")
    print("   c. Rome")
    print("   d. Berlin")
    answer2 = input("Choose A/B/C/D: ").strip().upper()
    if answer2 == "A":
        score += 1
        print("Correct! The capital of France is Paris.\n")
    else:
        print("Incorrect. The correct answer is A (Paris).\n")

    # ---------- Question 3 ----------
    print("3) Which planet is known as the Red Planet?")
    print("   a. Venus")
    print("   b. Jupiter")
    print("   c. Saturn")
    print("   d. Mars")
    answer3 = input("Choose A/B/C/D: ").strip().upper()
    if answer3 == "D":
        score += 1
        print("Correct! Mars is the Red Planet.\n")
    else:
        print("Incorrect. The correct answer is D (Mars).\n")

    # ---------- Question 4 ----------
    print("4) What is the largest ocean on Earth?")
    print("   a. Atlantic Ocean")
    print("   b. Pacific Ocean")
    print("   c. Indian Ocean")
    print("   d. Arctic Ocean")
    answer4 = input("Choose A/B/C/D: ").strip().upper()
    if answer4 == "B":
        score += 1
        print("Correct! The Pacific Ocean is the largest.\n")
    else:
        print("Incorrect. The correct answer is B (Pacific Ocean).\n")

    # ---------- Question 5 ----------
    print("5) Who wrote the play Romeo and Juliet?")
    print("   a. Charles Dickens")
    print("   b. Mark Twain")
    print("   c. William Shakespeare")
    print("   d. Jane Austen")
    answer5 = input("Choose A/B/C/D: ").strip().upper()
    if answer5 == "C":
        score += 1
        print("Correct! William Shakespeare wrote it.\n")
    else:
        print("Incorrect. The correct answer is C (William Shakespeare).\n")

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

    print(f"\nThanks for playing, {name}. Goodbye!")

else:
    print(f"\nMaybe next time, {name}!")