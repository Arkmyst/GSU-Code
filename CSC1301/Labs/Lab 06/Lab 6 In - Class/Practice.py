def main():

    print("")
    print("Please Enter “X” or “O” with a space in between each in this format --> X O X - OR - X O O")


    row1_input = input("ROW0> ")
    row1_input = row1_input.split()

    row2_input = input("ROW1> ")
    row2_input = row2_input.split()

    row3_input = input("ROW2> ")
    row3_input = row3_input.split()

    TicTacData = [row1_input,row2_input,row3_input]
    results = []
    for x in TicTacData:
        results.append(x)

    for i in range(len(results)):
        #If win in Horizontal
        if results[i] == ['X', 'X', 'X']:
            print("X IS GOOD IN HORIZONTAL")

        if results[i] == ['O', 'O', 'O']:
            print("O IS GOOD IN HORIZONTAL")

        #If win in Vertical
    i = 1
    RowScan = 0
    xVert = 0
    oVert = 0
    xHori = 0
    oHori = 0
    xDiag = 0
    oDiag = 0
    Row0 = row1_input
    Row1 = row2_input
    Row2 = row3_input
    while i == 1:

        if Row0[RowScan] == "X" and Row0[RowScan] == Row1[RowScan] and Row1[RowScan] == Row2[RowScan]:
            xVert = 1

        if Row0[RowScan] == "O" and Row0[RowScan] == Row1[RowScan] and Row1[RowScan] == Row2[RowScan]:
            oVert = 1

            RowScan += 1

        if RowScan == 3:
            i = 0

            i = 1


        RowScan = 0

        LongString = [Row0[0], Row0[1], Row0[2], Row1[0], Row1[1], Row1[2], Row2[0], Row2[1],Row2[2]]

main()
