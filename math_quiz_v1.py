import random

# Initialise variables
correct = 0
incorrect = 0
rounds_played = 0


# Adds styles/colours
class Styles:
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"
    reset = "\033[0m"
    headline = "\033[1m\033[4m\033[94m"


# String checker
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Make sure input is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if input is on the list
            if item == user_response:
                return item

            # Check if input is the same as first letter of an item on list
            elif user_response == item[0]:
                return item

        # print error if input is invalid
        print(error)
        print()


# Checks if input is an integer bigger than 0
def int_checker(question):
    while True:

        error = f"{Styles.red}Please enter an integer that is 1 or higher{Styles.reset}"

        to_check = input(question)

        if to_check == "xxx":
            return "exit"

        try:
            response = int(to_check)

            # Checks if integer is greater than or equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Define the instructions
def instructions():
    print(f"{Styles.headline}Instructions{Styles.reset}"
          f"\n {Styles.blue}You will be asked multiplication questions and input the correct answer. To exit at "
          f"anytime just type 'xxx'" + Styles.reset)


# Generate numbers and answer for multiplication
def gen_multi():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ans = a * b
    return a, b, ans


# Asks user if they want to read the instructions
print(Styles.red + f"XXX {Styles.blue}Welcome to Multiplication Quiz {Styles.red}XXX" + Styles.reset)
want_instructions = string_checker("Would you like to read the instructions?")
if want_instructions == "yes":
    instructions()

# Game :D
begin = string_checker("Would you like to begin?")
if begin == "yes":
    while True:
        # Asks user math question
        a, b, ans = gen_multi()
        print(f"\nWhat is {a} * {b}")
        print(ans)
        user_ans = int_checker("Your answer: ")

        # Checks for exit code
        if user_ans == "exit":
            print("Exit")
            break
        else:
            user_ans = int(user_ans)

        # Check if user_ans is correct
        if user_ans == ans:
            correct += 1
            print(f"You were {Styles.green}correct!{Styles.reset}")
        else:
            incorrect += 1
            print(f"You were {Styles.red}Incorrect{Styles.reset}. The correct answer was {Styles.green}{ans}{Styles.reset}")
        rounds_played += 1
        print(Styles.green, correct, Styles.red, incorrect, Styles.reset, rounds_played)

    # Stats (calc and print)
    if rounds_played > 0:
        percent_correct = correct / rounds_played * 100
        percent_incorrect = 100 - percent_correct
        # Round numbers to 2 decimal points
        percent_correct_rounded = round(percent_correct, 2)
        percent_incorrect_rounded = round(percent_incorrect, 2)
        want_stats = string_checker("Do you want to see your stats?")
        if want_stats == "yes":
            print(f"{Styles.green}Correct: {percent_correct_rounded}%\n{Styles.red}Incorrect: {percent_incorrect_rounded}%" + Styles.reset)
