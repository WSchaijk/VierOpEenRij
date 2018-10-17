rows = []
for rowIndex in range(6):
  rows.append(['.', '.', '.', '.', '.', '.', '.'])

availableSpaces = 42
playingPlayer = 1

def printBoard():
  for row in rows:
    for column in row:
      print(column, end="")
    print()

def makeAMove(player, column):
  if 0 < column < 8:
    for rowIndex in range(5, -1, -1):
      if rows[rowIndex][column - 1] == '.':
        if player == 1:
          rows[rowIndex][column - 1] = "X"
        else:
          rows[rowIndex][column - 1] = "O"
        return True
  return False


while availableSpaces > 0:
  printBoard()
  chosenColumn = input("Player {0}, please pick a row: ".format(playingPlayer))
  if chosenColumn.isnumeric():
    chosenColumn = int(chosenColumn)
    if makeAMove(playingPlayer, chosenColumn):
      if playingPlayer == 1:
        playingPlayer = 2
      else:
        playingPlayer = 1
    else:
      print("Je keuze klopt niet")