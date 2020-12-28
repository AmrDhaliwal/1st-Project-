#Install replit in the terminal using pip.
#Install typing_extensions using pip.
#Install art.py using pip.

from replit import clear
from art import*
Auction = text2art("Quiet Auction")
print(Auction)

bids = {}
bids_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bids_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()


