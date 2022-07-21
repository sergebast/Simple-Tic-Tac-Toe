m = n = 3
step = 1
my_matrix = [['_'] * m for i in range(n)]


def game_table(_matrix):
    print("---------")
    for x in _matrix:
        print("|", " ".join(x), "|")
    print("---------")


def get_cols(_matrix):
    r = []
    for i in range(n):
        r.append([x[i] for x in _matrix])
    return r


def get_diagonal(_matrix):
    return [[_matrix[0][0], _matrix[1][1], _matrix[2][2]],
            [_matrix[0][2], _matrix[1][1], _matrix[2][0]]]


def combinations(_matrix):
    return get_cols(_matrix) \
           + get_diagonal(_matrix) \
           + _matrix


def user(_step):
    if _step % 2 == 0:
        return 'O'
    else:
        return 'X'


def counter_element(el, _matrix):
    return len([x for row in _matrix for x in row if x == el])


if __name__ == '__main__':

    game_table(my_matrix)

    while True:
        try:
            i = input().split()
            a = int(i[0]) - 1
            b = int(i[1]) - 1
        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
        else:
            if all([a >= 0, a < 3, b >= 0, b < 3]):
                if my_matrix[a][b] == " " or my_matrix[a][b] == "_":
                    my_matrix[a][b] = user(step)
                    game_table(my_matrix)
                    data = combinations(my_matrix)
                    if any([['X', 'X', 'X'] in data, ['O', 'O', 'O'] in data]):
                        print(user(step), 'wins')
                        break
                    elif counter_element('_', my_matrix) == 0:
                        print('Draw')
                        break
                    step += 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
