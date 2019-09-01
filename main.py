gridMatrix = [['*' for i in range(3)] for j in range(3)]

print("  0 1 2")

positions = []
for i in range(3):
    print(i, end=" ")
    for j in range(3):
        print(gridMatrix[i][j], end=" ")
        position = [i, j]
        positions.append(position)
    print("")

for i in range(9):
    print("Position "+str(i)+" : ("+str(positions[i][0])+", "+str(positions[i][1])+")")
print("\n")
player_one = input("choose icon for playing game (X/O) ? : ")
player_two = ''
print("Player 1 is playing "+player_one)
if player_one == 'X':
    player_two = 'O'
else:
    player_two = 'X'
print("Player 2 is playing "+player_two)

loop = 0
while 1:
    for i in range(3):
        for j in range(3):
            print(gridMatrix[i][j], end=" ")
        print("")
    if loop % 2 == 0:
        while 1:
            print("***Player 1 Turn***")
            p = int(input("Please select the position for insertion : "))

            row_index = positions[p][0]
            col_index = positions[p][1]
            # print(row_index, col_index, gridMatrix[row_index][col_index])
            flag = True
            for i in range(3):
                for j in range(3):
                    if i == row_index and j == col_index:
                        if gridMatrix[i][j] == '*':
                            gridMatrix[i][j] = player_one
                        else:
                            print("Invalid Input.....Input the correct position.....")
                            flag = False
                        break
            if flag:
                break
    else:
        while 1:
            print("***Player 2 Turn***")
            p = int(input("Please select the position for insertion : "))
            row_index = positions[p][0]
            col_index = positions[p][1]
            # print(row_index, col_index, gridMatrix[row_index][col_index])
            flag = True
            for i in range(3):
                for j in range(3):
                    if i == row_index and j == col_index:
                        if gridMatrix[i][j] == '*':
                            gridMatrix[i][j] = player_two
                        else:
                            print("Invalid Input.....Input the correct position.....")
                            flag = False
                        break
            if flag:
                break
    loop = loop + 1

    # win or lose condition
    row_win_X = ''
    row_win_O = ''
    col_win_X = ''
    col_win_O = ''
    diag_win_X = True
    diag_win_O = True

    k = 2
    rdiag_win_X = True
    rdiag_win_O = True
    for i in range(3):
        row_win_X = True
        row_win_O = True
        col_win_X = True
        col_win_O = True

        for j in range(3):
            if gridMatrix[i][j] != 'X':
                row_win_X = False
            if gridMatrix[i][j] != 'O':
                row_win_O = False
            if gridMatrix[j][i] != 'X':
                col_win_X = False
            if gridMatrix[j][i] != 'O':
                col_win_O = False
        # condition for diagonal
        if gridMatrix[i][i] != 'X':
            diag_win_X = False
        if gridMatrix[i][i] != 'O':
            diag_win_O = False
        # condition for another diagonal
        if gridMatrix[i][k] != 'X':
            rdiag_win_X = False
        if gridMatrix[i][k] != 'O':
            rdiag_win_O = False
        k = k-1
        if row_win_X or row_win_O or col_win_X or col_win_O:
            break

    if row_win_X or row_win_O or col_win_X or col_win_O or diag_win_X or diag_win_O or rdiag_win_X or rdiag_win_O:
        print("\n")
        for i in range(3):
            for j in range(3):
                print(gridMatrix[i][j], end=" ")
            print("")
        print("")
        if row_win_X:
            if player_one == 'X':
                print("********  Player 1 Win with X")
            else:
                print("********  Player 2 Win with X")
        elif row_win _O:
            if player_one == 'O':
                print("********  Player 1 Win with O")
            else:
                print("********  Player 2 Win with O")
        elif col_win_X:
            if player_one == 'X':
                print("********  Player 1 Win with X")
            else:
                print("********  Player 2 Win with X")
        elif col_win_O:
            if player_one == 'O':
                print("********  Player 1 Win with O")
            else:
                print("********  Player 2 Win with O")
        elif diag_win_X:
            if player_one == 'X':
                print("********  Player 1 Win with X")
            else:
                print("********  Player 2 Win with X")
        elif diag_win_O:
            if player_one == 'O':
                print("********  Player 1 Win with O")
            else:
                print("********  Player 2 Win with O")
        elif rdiag_win_X:
            if player_one == 'X':
                print("********  Player 1 Win with X")
            else:
                print("********  Player 2 Win with X")
        elif rdiag_win_O:
            if player_one == 'O':
                print("********  Player 1 Win with O")
            else:
                print("********  Player 2 Win with O")
        break

    # draw condition
    if loop > 8:
        print("\n ***** Match Tied *****")
        break
    print("\n")
