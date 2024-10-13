import random
import freecurrencyapi
import os
from dotenv import load_dotenv

load_dotenv()

# Rename .env.example file to .env and add your API key from freecurrencyapi.com
API_KEY = os.getenv("API_KEY")


def get_exchange_rate():
    client = freecurrencyapi.Client(API_KEY)

    # Fetch the latest exchange rates for USD
    response = client.latest(base_currency='USD', currencies=['ILS'])

    # Return the exchange rate for USD to ILS
    return response['data']['ILS']


def get_money_interval(difficulty, usd_amount):
    exchange_rate = get_exchange_rate()
    converted_amount = usd_amount * exchange_rate
    allowed_diff = 10 - difficulty

    return converted_amount - allowed_diff, converted_amount + allowed_diff


def get_guess_from_user(usd_amount):
    guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
    return guess


def compare_results(interval, guess):
    lower_bound, upper_bound = interval
    return lower_bound <= guess <= upper_bound


def play(difficulty):
    usd_amount = random.randint(1, 100)
    interval = get_money_interval(difficulty, usd_amount)
    guess = get_guess_from_user(usd_amount)

    if compare_results(interval, guess):
        return True
    else:
        return False
