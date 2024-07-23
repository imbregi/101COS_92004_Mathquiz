import random

# Initialize variables
correct = 0
incorrect = 0
rounds_played = 0


# Checks if input is an integer bigger than 0
def int_checker(question):
    while True:
        to_check = input(question)
        response = int(to_check)
        return response


# Generate numbers and answer for multiplication
def gen_multi():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ans = a * b
    return a, b, ans


def auto_ans():
    user_ans = random.randint(1, 2)
    return user_ans


# Game :D
begin = int_checker("How many rounds?")
if begin != "xxx":  # Ensure the user did not input 'xxx'
    while rounds_played < begin:
        # Generate numbers and answer
        a, b, ans = gen_multi()
        user_ans = auto_ans()

        # Check if user_ans is correct
        if user_ans == 1:
            correct += 1
        elif user_ans == 2:
            incorrect += 1
        rounds_played += 1

    # Stats (calc and print)
    if rounds_played > 0:
        print("// Stats //")
        percent_correct = (correct / rounds_played) * 100
        percent_incorrect = 100 - percent_correct
        # Round numbers to 2 decimal points
        percent_correct_rounded = round(percent_correct, 2)
        percent_incorrect_rounded = round(percent_incorrect, 2)
        # Print stats
        print(f"Correct: {percent_correct_rounded}%\nIncorrect: {percent_incorrect_rounded}%")

input("Press Enter to exit...")
