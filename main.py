'''
TicTacToe by Quantico
First Own Project w py
'''

playScreen = [" "] * 9

#functions

def showPlayScreeen():
    for i in range (0, 9, 3):
        print(" | ". join(playScreen[i:i+3]))
        if i < 6:
            print("--+---+--")

def winner(player):
    winCombinations = [
        (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)
    ]
    return any(all(playScreen[i] == player for i in combinations) for combinations in winCombinations)

def newMove(player):
    while True:
        move = input(f"Player {player}, choosing a Tile (1 - 9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            index = int(move) - 1
            if playScreen[index] == " ":
                playScreen[index] = player
                break
            else:
                print("This field is already taken, please choose another one")
        else:
            print("False input, please choose between 1 and 9")

def game():
    player = "X"
    showPlayScreeen()

    while True:
        newMove(player)
        showPlayScreeen()

        if winner(player):
            print(f"Player {player} has won!")
            break

        if " " not in playScreen:
            print("Tie")
            break

        player = "O" if player == "X" else "X"

game()