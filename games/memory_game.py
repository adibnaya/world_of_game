import random
import time
import os


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    user_input = input(f"Enter a list of {difficulty} numbers separated by spaces: ")
    try:
        user_list = [int(num) for num in user_input.split()]
        if len(user_list) != difficulty:
            raise ValueError
        return user_list
    except ValueError:
        print("Invalid input. Please try again.")
        return get_list_from_user(difficulty)


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember the sequence of numbers:")
    print(sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_list = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_list)
