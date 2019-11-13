#poker

#Cards' deck. Randomly shuffled.
import random
deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
random.shuffle(deck)

#Variables
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
Space = " "

print("Texas hold \'em poker - Heads up challenge\n")
name = input("Player's name? ")

#Inserting cards to variables
for hands in range(2):
  myhand.append(deck.pop())
  Master.append(deck.pop())
for flopcards in range(3):
  Flop.append(deck.pop())
for turnrivercards in range(1):
  Turn.append(deck.pop())
  River.append(deck.pop())

#Gameplay formula
def poker_game(Cash_player = 10000, Cash_master = 10000, Pot = 0):

  Table1 = (f"{Newline*10}{Line*50}\nMaster's hand:\nCash: {Cash_master}$\n\n\nPot: {Pot}{Space*10}")
  Table2 = (f"\n\n\n{name}\'s hand: {myhand} \nCash: {Cash_player}$\n{Star*50}\n")
  BasicTable = (f"{Table1}{Table2}")
  FlopTable = (f"{Table1}{Flop}{Table2}")
  TurnTable = (f"{Table1}{Flop}  {Turn}{Table2}")
  RiverTable = (f"{Table1}{Flop}  {Turn}  {River}{Table2}")

  Gamestep = BasicTable, FlopTable, TurnTable, RiverTable
  for gamephase in range(len(Gamestep)):
    print(Gamestep[gamephase])
    Choice = input("Choose your action: Bet/Check/Fold - ")
    while Choice != "Check" and Choice != "Bet" and Choice != "Fold":
      Choice = input("Incorrect entry, try again: ")
    if Choice == "Check":
      print(Line*50)
      continue
    elif Choice == "Bet":
      betamount = int(input("Amount - "))
      print(Line*50)
      while betamount > Cash_player:
        if betamount == 0:
          continue
        betamount = int(input("Incorrect amount, try again: "))
      Cash_player = Cash_player - betamount
      Cash_master = Cash_master - betamount
      Pot = betamount + betamount
      continue
    elif Choice == "Fold":
      break
poker_game()
