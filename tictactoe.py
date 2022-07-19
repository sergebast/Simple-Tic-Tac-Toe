from checkgame import matrix


def game_table(m):
    print("---------")
    for x in m:
        print("|", " ".join(x), "|")
    print("---------")


s = list(input().strip())
my_matrix = matrix(s)
print("My_matrix", my_matrix)
game_table(my_matrix)

while True:
    try:
        i = input().split()
        a = int(i[0]) - 1
        b = int(i[1]) - 1
    except ValueError:
        print("You should enter numbers!")
    else:
        if 0 <= a < 3:
            if 0 <= b < 3:
                if my_matrix[a][b] == " " or my_matrix[a][b] == "_":
                    my_matrix[a][b] = 'X'
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("Coordinates should be from 1 to 3!")

game_table(my_matrix)
