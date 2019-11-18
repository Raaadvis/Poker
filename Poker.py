#poker

#Cards' deck. Randomly shuffled.

Cash_master = 10000
Cash_player = 10000
gamewon = False
print("Texas hold \'em poker - Heads up challenge!\n")
name = input("Player's name? ")

while gamewon == False:

  import random
  deck = ["2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
  random.shuffle(deck)

  #Variables
  Pot = 0
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

  #Inserting cards to variables
  for cards1 in range(1):
    Turn.append(deck.pop())
    River.append(deck.pop())
  for cards2 in range(2):
    myhand.append(deck.pop())
    Master.append(deck.pop())
  for cards3 in range(3):
    Flop.append(deck.pop())

  Table = (f"{Newline*10}{Line}\n\n{name} hand: {myhand}\n\n*Cards: ")
  BasicTable = (f"{Table}")
  FlopTable = (f"{Table}{Flop}")
  TurnTable = (f"{Table}{Flop} {Turn}")
  RiverTable = (f"{Table}{Flop} {Turn} {River}")

  Gamestep = BasicTable, FlopTable, TurnTable, RiverTable
  for gamephase in range(len(Gamestep)):
    print(Gamestep[gamephase], "\n")
    print(f"Cash {name}: ", Cash_player)
    print("Pot: ", Pot)
    print("Cash computer: ", Cash_master)
    Choice = input("\nChoose your action: Bet/Check/Fold - ")
    while Choice != "Check" and Choice != "Bet" and Choice != "Fold":
      Choice = input("Incorrect entry, try again: \nChoose your action: Bet/Check/Fold - ")
    if Choice == "Check":
      print(Line)
      continue
    elif Choice == "Bet":
      betamount = int(input("Bet amount - "))
      print(Line)
      while betamount > Cash_player and betamount > Cash_master:
        betamount = int(input("Incorrect amount, try again: "))
        if betamount == 0:
          continue
      Pot += betamount*2
      Cash_player -= betamount
      Cash_master -= betamount
      continue
    elif Choice == "Fold" or gamephase == 3:
      print(Line, RiverTable)
      break
  print(f"Computer\'s hand: {Master}\n{Line}")
  winner = input(f"Who is the winner, Split/Master/{name}? - ")
  while winner != "Split" and winner != "Master" and winner != name:
    winner = input(f"Incorrect entry, try again: \nWho is the winner, Split/Master/{name}? - ")
  if winner == "Split":
    Cash_player += Pot /2
    Cash_master += Pot /2
  elif winner == "Master":
    Cash_master += Pot
  elif winner == name:
    Cash_player += Pot
  Pot = 0
  if Cash_player <= 0 or Cash_master <= 0:
    gamewon = True
