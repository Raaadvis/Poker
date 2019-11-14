#poker

#Cards' deck. Randomly shuffled.
import random
deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
random.shuffle(deck)

#Variables
betamount = 0
callamount = 0
myhand = []
Master = []
Flop = []
Turn = []
River = []
Newline = "\n"
Star = "*"*50
Line = "_"*50
Space = " "

print("Texas hold \'em poker - Heads up challenge\n")
name = input("Player's name? ")

#Inserting cards to variables
for cards1 in range(1):
  Turn.append(deck.pop())
  River.append(deck.pop())
for cards2 in range(2):
  myhand.append(deck.pop())
  Master.append(deck.pop())
for cards3 in range(3):
  Flop.append(deck.pop())

#Gameplay formula
def poker_game(Cash_player = 10000, Cash_master = 10000, Pot = 0):

  Table1 = (f"{Newline*10}{Line}\nMaster's cash: {Cash_master}$\n\n\nPot: {Pot}{Space*10}")
  Table2 = (f"\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star}\n")
  BasicTable = (f"{Table1}{Table2}")
  FlopTable = (f"{Table1}{Flop}{Table2}")
  TurnTable = (f"{Table1}{Flop} {Turn}{Table2}")
  RiverTable = (f"{Table1}{Flop} {Turn} {River}{Table2}")

  Gamestep = BasicTable, FlopTable, TurnTable, RiverTable
  for gamephase in range(len(Gamestep)):
    print(Gamestep[gamephase])
    Choice = input("Choose your action: Bet/Check/Fold - ")
    while Choice != "Check" and Choice != "Bet" and Choice != "Fold":
      Choice = input("Incorrect entry, try again: ")
    if Choice == "Check":
      print(Line)
      continue
    elif Choice == "Bet":
      global betamount
      betamount = int(input("Amount - "))
      print(Line)
      while betamount > Cash_player:
        betamount = int(input("Incorrect amount, try again: "))
        if betamount == 0:
          continue
      Cash_player = Cash_player - betamount
      Cash_master = Cash_master - betamount
      Pot = betamount + betamount
      print(Cash_player)
      print(Pot)
      continue
    elif Choice == "Fold" or gamephase == 3:
      print(Line, RiverTable)
      break
  print(f"\nMaster\'s hand: {Master}\n{Line}")
poker_game()
