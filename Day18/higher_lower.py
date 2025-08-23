import random
import os
from time import sleep

# Sample dataset (you can expand this list or load from a file)
data = [
    {"name": "Cristiano Ronaldo", "follower_count": 630, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 530, "description": "Footballer", "country": "Argentina"},
    {"name": "Taylor Swift", "follower_count": 500, "description": "Singer", "country": "USA"},
    {"name": "Selena Gomez", "follower_count": 430, "description": "Singer/Actress", "country": "USA"},
    {"name": "Dwayne Johnson", "follower_count": 410, "description": "Actor/Wrestler", "country": "USA"},
    {"name": "Kylie Jenner", "follower_count": 420, "description": "Media personality", "country": "USA"},
    {"name": "MrBeast", "follower_count": 300, "description": "YouTuber", "country": "USA"},
    {"name": "Bill Gates", "follower_count": 40, "description": "Businessman", "country": "USA"},
    {"name": "Narendra Modi", "follower_count": 90, "description": "Prime Minister", "country": "India"},
    {"name": "Virat Kohli", "follower_count": 270, "description": "Cricketer", "country": "India"}
]

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Get random account from data
def get_random_account():
    return random.choice(data)

# Format account info for printing
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Check user's guess
def is_correct(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# ---------------- MAIN GAME LOOP ---------------- #

def play_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        # Prevent same person twice
        while account_a == account_b:
            account_b = get_random_account()

        clear_screen()
        print("🔼 Welcome to the Higher Lower Game! 🔽")
        print(f"🎯 Current score: {score}\n")

        print(f"A: {format_data(account_a)}")
        print("vs")
        print(f"B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_right = is_correct(guess, a_followers, b_followers)

        if is_right:
            score += 1
            print(f"\n✅ You're right! Current score: {score}")
            sleep(1.5)
        else:
            game_should_continue = False
            print(f"\n❌ Wrong! Final score: {score}")

# Ask to play again
while True:
    play_game()
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! Stay curious 💡")
        break
