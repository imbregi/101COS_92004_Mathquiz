import random

# Initialise variables
correct = 0
incorrect = 0


# Styles
class Styles:
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"
    bold_underline = "\033[1m\033[4m"


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


# Define the instructions
def instructions():
    print(f"{Styles.bold_underline}Instructions{Styles.reset}")


# Generate numbers and answer for multiplication
def gen_multi():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ans = a * b
    return a, b, ans


print("Welcome to Multiplication Quiz")
want_instructions = string_checker("Would you like to read the instructions?")
if want_instructions == "yes":
    instructions()


# Game :D
while True:
    a, b, ans = gen_multi()
    print(f"\nWhat is {a} * {b}")
    print(ans)
    user_ans = input("Your answer: ")
    user_ans = int(user_ans)

    if user_ans == ans:
        correct += 1
        print(f"You were {Styles.green}correct!{Styles.reset}")
    else:
        incorrect += 1
        print(f"{Styles.red}Incorrect{Styles.reset}. The correct answer was {Styles.green}{ans}{Styles.reset}")
    print(Styles.green, correct, Styles.red,  incorrect, Styles.reset)
