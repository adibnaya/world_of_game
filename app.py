import importlib


def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    while True:
        game_number = input("""Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")

        if game_number.isdigit() or (game_number.startswith('-') and game_number[1:].isdigit()):
            game_number = int(game_number)
            if 1 <= game_number <= 3:
                break
            else:
                print("Error: The number must be between 1 and 3. Please try again.")
        else:
            print("Error: Invalid input. Please enter a valid integer.")

    while True:
        difficulty = input("Select difficulty level (1-5): ")
        if difficulty.isdigit() or (difficulty.startswith('-') and difficulty[1:].isdigit()):
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                break
            else:
                print("Error: The number must be between 1 and 5. Please try again.")
        else:
            print("Error: Invalid input. Please enter a valid integer.")

    game_mapping = {
        1: 'memory_game',
        2: 'guess_game',
        3: 'currency_roulette'
    }

    selected_game = game_mapping[game_number]

    try:
        game_module = importlib.import_module(f'games.{selected_game}')
        result = game_module.play(difficulty)
        if result:
            print("You won!")
        else:
            print("You lost!")

    except ImportError:
        print(f"Error: Could not load the game '{selected_game}'. Please check if the file exists.")
    except AttributeError:
        print(f"Error: The game '{selected_game}' does not have a 'play' function.")
