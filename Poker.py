#poker

import random
deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
random.shuffle(deck)

name = input("Player's name? ")
Cash_player = 10000
Cash_master = 10000
myhand = []
Master = []
Flop = []
Turn = []
River = []

for hands in range(2):
  myhand.append(deck.pop())
  Master.append(deck.pop())
for flopcards in range(3):
  Flop.append(deck.pop())
for turnrivercards in range(1):
  Turn.append(deck.pop())
  River.append(deck.pop())

print("\n*****************************************************\n")
print(f"{name} is holding: {myhand} \nCash left: {Cash_player}$")
print("\n____________________________________________________________\n")

Choice1 = input("Choose your action: Bet/Check/Fold - ")
if Choice1 == "Check":
    print("Flop:", Flop)
if Choice1 == "Bet":
    amount = int(input("Amount - "))
    if amount >= Cash_player:
        print("You can\'t bet more than you have, stupid face.")
    if amount <= Cash_player:
        Cash_left = Cash_player - amount 
        print("Cash left - ", Cash_left)
#print("Flop:", Flop, "Turn:", Turn, "River:", River)
