#!/usr/bin/env python3
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
biddingfinished = False

def find_highestbidder(biddingrecord):
    highestbid = 0
    winner = ""
    for bidder in biddingrecord:
        bidamount = biddingrecord[bidder]
        if bidamount > highestbid:
            highestbid = bidamount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestbid}")


while not biddingfinished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    shouldcontinue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if shouldcontinue == "no":
        biddingfinished = True
        find_highestbidder(bids)
    elif shouldcontinue == "yes":
        clear_screen() 