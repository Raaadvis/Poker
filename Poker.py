#poker

import random
deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]

random.shuffle(deck)


Cash_player = 10000
Cash_master = 10000
Pot = 0
betamount = 0
callamount = 0
myhand = []
Master = []
Flop = []
Turn = []
River = []
Newline = "\n"
Star = "*"
Line = "_"


print("Texas hold \'em poker - Heads up challenge\n")
name = input("Player's name? ")


for hands in range(2):
  myhand.append(deck.pop())
  Master.append(deck.pop())
for flopcards in range(3):
  Flop.append(deck.pop())
for turnrivercards in range(1):
  Turn.append(deck.pop())
  River.append(deck.pop())


Table = (f"{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
print(Table)


Choice1 = input("Choose your action: Bet/Check/Fold - ")
if Choice1 == "Check":
  print(f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  \n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
elif Choice1 == "Bet":
  betamount1 = int(input("Amount - "))
  betamount =  betamount1
  callamount = betamount1
  Cash_player = Cash_player - betamount
  Cash_master = Cash_master - callamount
  Pot = betamount + callamount
  if betamount1 > Cash_player:
    print(f"\nYou can\'t bet more than you have, stupid face.\n{Line*50}")
  if betamount1 <= Cash_player:
    print(f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  \n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
Choice2 = input("Choose your action: Bet/Check/Fold - ")
if Choice2 == "Check":
  print(f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  {Turn}\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
elif Choice2 == "Bet":
  betamount2 = int(input("Amount - "))
  callamount = betamount2
  betamount = betamount2
  Cash_player = Cash_player - betamount
  Cash_master = Cash_master - callamount
  Pot = Pot + betamount + callamount
  if betamount2 > Cash_player:
    print(f"\nYou can\'t bet more than you have, stupid face.\n{Line*50}")
  if betamount2 <= Cash_player:
    print(f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  {Turn} \n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
Choice3 = input("Choose your action: Bet/Check/Fold - ")
if Choice3 == "Check":
  print(f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  {Turn}  {River}\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
elif Choice3 == "Bet":
  betamount3 = int(input("Amount - "))
  callamount = betamount3
  betamount = betamount3
  Cash_player = Cash_player - betamount
  Cash_master = Cash_master - callamount
  Pot = Pot + betamount + callamount
  if betamount3 > Cash_player:
    print(f"\nYou can\'t bet more than you have, stupid face.\n{Line*50}")
  if betamount3 <= Cash_player:
    print(f"{Newline*10}{Line*50}\nMaster's hand:{Master}\nCash: {Cash_master}$\n\n\nPot: {Pot}             {Flop}  {Turn}   {River}\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
else:
  print("Check your spelling")
