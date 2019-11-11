#poker

import random
deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
random.shuffle(deck)

name = input("Zaidejo vardas? ")
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

print(name,"is holding:",myhand)
print("Master is holding:",Master)
print("Flop: ",Flop)
print("Turn: ",Turn)
print("River: ",River)
