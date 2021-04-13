import random


def find_number():
    """Execute game of finding number."""
    lower_limit, upper_limit = 1, 30
    random_int = random.randint(lower_limit, upper_limit)

    num_of_guesses = 0

    while True:
        user_guess = input("Your guess (int), or 'exit':")
        if user_guess == "exit":
            print("Exiting...")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"Please use ints. Your input: {user_guess}.")
            continue

        print(f"Your guess {user_guess}.")
        num_of_guesses += 1
        if user_guess == random_int:
            print("Your guess is exactly right.")
            break
        if user_guess > random_int:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    result_text = f"Thanks for playing! You tried {num_of_guesses} times."
    print(result_text)

    file = open("find_number_guess.txt", mode="a")
    print(result_text, file=file)
    file.close()
