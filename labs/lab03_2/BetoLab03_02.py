# Starting file for LAB 3-2
# CS31 Course
# Carlos Farias
# Date 08/14/2026

#============================================
#        The Test Scores application
#============================================
# Practice program: use a nested while loop.

# display a welcome message
print("=" * 44)
print("        The Test Scores application")
print("=" * 44)

choice = "y"
while choice == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("===============================")

    # initialize variables for this set
    counter = 0
    score_total = 0

    # inner loop: collect the scores for one set
    while True:
        entry = input("Enter test score: ").strip().lower()

        # check FIRST if the input equals "end"
        if entry == "end":
            break
        else:
            # otherwise convert to int and validate
            try:
                test_score = int(entry)
            except ValueError:
                print("Please enter a whole number from 0 through 100, or 'end'.")
                continue

            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. "
                      "Score discarded. Try again.")

    # display the results for the set that just finished
    print("===============================")
    if counter > 0:
        average_score = round(score_total / counter)
        print(f"Total Score: {score_total}")
        print(f"Average Score: {average_score}")
    else:
        print("No scores were entered for this set.")

    # ask whether to enter another set
    print()
    choice = input("Enter another set of test scores (y/n)? ").strip().lower()
    while choice not in ("y", "yes", "n", "no"):
        choice = input("Please enter 'y' or 'n': ").strip().lower()
    if choice == "yes":
        choice = "y"
    print()

print("Bye!")