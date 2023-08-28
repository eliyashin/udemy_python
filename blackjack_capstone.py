#!/usr/bin/env python3
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(userscore, computerscore):
    if userscore > 21 and computerscore > 21:
        return "You went over! You lose."
    if userscore == computerscore:
        return "Draw"
    elif computerscore == 0:
        return "Lose, opponent has blackjack"
    elif userscore == 0:
        return "Win with a blackjack"
    elif userscore > 21:
        return "You went over, You lose"
    elif computerscore > 21:
        return "Opponent went over, you win!"
    elif userscore > computerscore:
        return "You win"
    else:
        return "You lose"
    

usercards = []
computercards = []
gameover = False

for _ in range(2):
    usercards.append(deal_card())
    computercards.append(deal_card())

while not gameover:
    userscore = calculate_score(usercards)
    computerscore = calculate_score(computercards)
    print(f" Your cards: {usercards}, current score: {userscore}")
    print(f" Computer's first card: {computercards [0]}")

    if userscore == 0 or computerscore == 0 or userscore > 21:
        gameover = True
    else:
        user_shoulddeal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_shoulddeal == "y":
            usercards.append(deal_card)
        else:
            gameover = True

while computerscore != 0 and computerscore < 17:
    computercards.append(deal_card())
    computerscore = calculate_score(computercards)
    
print(compare(userscore, computerscore))
