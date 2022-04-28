
size = 8
max_count = 8
orig_pole = [[0 for i in range(size)] for k in range(size)]

def is_spot_available(x, y, pole):
    if pole[y][x] != 0:
        return False
    for cur_y in range(size):
        if pole[cur_y][x] != 0:
            return False
    for cur_x in range(size):
        if pole[y][cur_x] != 0:
            return False

    if x < y:
        a = y - x
        for cur in range(size - a):
            if pole[cur + a][cur] != 0:
                return False
    elif x > y:
        a = x - y
        for cur in range(size - a):
            if pole[cur][cur + a] != 0:
                return False
    else:
        for c in range(size):
            if pole[c][c] != 0:
                return False

    return True

iter_count = 0
def set_new_figure(pole, depth):
    global iter_count
    iter_count += 1
    for x in range(size):
        if is_spot_available(x, depth, pole):
            newPole = [i[:] for i in pole]
            newPole[depth][x] = 8
            if depth == max_count - 1:
                return newPole
            elif depth + 1 == size:
                return False
            get = set_new_figure(newPole, depth + 1)
            if get:
                return get
    return False


final_pole = set_new_figure(orig_pole, 0)



if final_pole:
    white_cell = "███"
    black_cell = "░░░"
    for y in range(size):
        line = ""
        for x in range(size):
            if y % 2 == 0:
                line += white_cell if x % 2 == 0 else black_cell
            else:
                line += black_cell if x % 2 == 0 else white_cell

            if final_pole[y][x] != 0:
                line = line[:-2] + "♕" + line[-2 + 1:]

        print(line)
    print("Количество итераций: " + str(iter_count))
else:
    print("Решений не было найдено")
