# Starting file for LAB 6-1
# CS31 Course
# Carlos Farias
# Date 11/05/2026

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print()

def get_scores():
    scores = []  # Initialize empty list to hold test scores
    while True:
        score = input("Enter test score: ")
        if score.lower() == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)  # Append valid score to list
            else:
                print(
                    "Test score must be from 0 through 100. "
                    + "Score discarded. Try again."
                )

def process_scores(scores):
    if not scores:
        print("No scores were entered.")
        return

    # Total scores using a for loop
    score_total = 0
    for score in scores:
        score_total += score

    # Calculate number of scores and average
    count = len(scores)
    average = round(score_total / count)

    # Calculate Lowest and Highest scores
    low_score = min(scores)
    high_score = max(scores)

    # Calculate Median score
    sorted_scores = sorted(scores)
    if count % 2 == 1:
        # Odd number of scores: pick exact middle element
        median_score = sorted_scores[count // 2]
    else:
        # Even number of scores: average of the two middle elements
        middle1 = sorted_scores[(count // 2) - 1]
        middle2 = sorted_scores[count // 2]
        median_score = (middle1 + middle2) / 2

    # Format and display all statistical results
    print()
    print("Total:           ", score_total)
    print("Number of Scores:", count)
    print("Average Score:   ", average)
    print("Low Score:       ", low_score)
    print("High Score:      ", high_score)
    print("Median Score:    ", median_score)

def main():
    display_welcome()

    # Store returned scores list in a variable (Instruction 3)
    scores = get_scores()

    # Pass the scores list to process_scores() (Instruction 3)
    process_scores(scores)

    print()
    print("Bye!")

if __name__ == "__main__":
    main()