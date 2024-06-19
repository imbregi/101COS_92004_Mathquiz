import random

# Initialise variables
correct = [0]
incorrect = [0]

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
def instruction():
    print('''
**** Instructions ****

Do something
and then do something else
etc
    ''')

# Generate numbers and answer for multiplication
def gen_multi():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ans = a * b
    return a, b, ans

# Game :D
while True:
    a, b, ans = gen_multi()
    print(f"What is {a} * {b}")
    user_ans = input("Your answer: ")
    user_ans = int(user_ans)

    if user_ans == ans:
        correct += 1
    elif user_ans != ans:
        incorrect += 1
        