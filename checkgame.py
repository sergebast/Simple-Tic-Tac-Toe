def get_cols(input_str):
    c = []
    i = 0
    while i < 3:
        c.append([input_str[k] for k in range(i, i + 7, 3)])
        i += 1
    return c


def combinations(input_str):
    return get_cols(input_str)\
           + [input_str[:3], input_str[3:6], input_str[-3:]]\
           + [[input_str[0], input_str[4], input_str[-1]],
              [input_str[2], input_str[4], input_str[6]]]


def counter_element(el, data):
    return len(list(filter(lambda x: x == el, data)))


def draw(data):
    if True not in [x == y == z for x, y, z in data]:
        print('Draw')
        return True
    else:
        return False


def wins(data):
    if ['X', 'X', 'X'] in data and ['O', 'O', 'O'] not in data:
        print('X wins')
        return True
    elif ['X', 'X', 'X'] not in data and ['O', 'O', 'O'] in data:
        print('O wins')
        return True
    else:
        return False


def impossible(data, input_str):
    if ['X', 'X', 'X'] in data and ['O', 'O', 'O'] in data:
        print('Impossible')
        return True
    else:
        el_x = counter_element('X', input_str)
        el_o = counter_element('O', input_str)
        if -2 >= (el_o - el_x) or (el_o - el_x) >= 2:
            print('Impossible')
            return True
        else:
            return False


def check(data, input_str):
    if counter_element('_', input_str) == 0:
        if not draw(data):
            wins(data)
    else:
        if not impossible(data):
            if not wins(data):
                print('Game not finished')
