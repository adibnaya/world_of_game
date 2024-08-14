def welcome():
    username = input("Enter your username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def start_play():
    while True:
        try:
            game_number = int(input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"""))
            if 1 <= game_number <= 3:
                break
            else:
                print("Error: The number must be between 1 and 3. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    while True:
        try:
            difficulty = int(input("Select difficulty level (1-5): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Error: The number must be between 1 and 5. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


