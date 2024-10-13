import random


def play(difficulty):
    number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(number, guess)


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"Guess a number between 0 and {difficulty}: "))


def compare_results(number, guess):
    return number == guess
