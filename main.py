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
        print("***Player 1 Turn***")
        p = int(input("Please select the position for insertion : "))
        row_index = positions[p][0]
        col_index = positions[p][1]
        # print(row_index, col_index, gridMatrix[row_index][col_index])
        for i in range(3):
            for j in range(3):
                if i == row_index and j == col_index:
                    gridMatrix[i][j] = player_one
                    break
    else:
        print("***Player 2 Turn***")
        p = int(input("Please select the position for insertion : "))
        row_index = positions[p][0]
        col_index = positions[p][1]
        # print(row_index, col_index, gridMatrix[row_index][col_index])
        for i in range(3):
            for j in range(3):
                if i == row_index and j == col_index:
                    gridMatrix[i][j] = player_two
                    break
    loop = loop + 1