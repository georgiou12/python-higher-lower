import art
import random
from game_data import data
from replit import clear

choice = True
score = 0
first = random.choice(data)
while choice == True:
    print(art.logo)
    second = random.choice(data)
    while first == second:
        second = random.choice(data)
    print(
        f"Compare A: {first['name']}, a {first['description']} from {first['country']}."
    )
    print(art.vs)
    print(
        f"Against B: {second['name']}, a {second['description']} from {second['country']}."
    )

    guess = input("Who has more followers? Type 'A' or 'B': ")
    if first['follower_count'] > second['follower_count'] and guess == 'A':
        score += 1
        clear()
    elif first['follower_count'] < second['follower_count'] and guess == 'B':
        score += 1
        first = second
        clear()
    else:
        clear()
        print(art.logo)
        print(f"Sorry that's wrong. Final score: {score}")
        choice = False
