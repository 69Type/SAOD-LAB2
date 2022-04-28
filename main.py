
import random
import math
import time
from time import sleep



# Генератор упорядоченых случайных чисел
def random_array_generator(count, _min=-100, _max=100):
    return sorted([random.randrange(_min, _max) for i in range(count)])


# Функция бинарного поиска
def binary_search(array, item):
    array_length = len(array)
    cur_index = array_length // 2
    start_index = 0
    end_index = array_length - 1

    while array[cur_index] != item:

        if end_index < 0 or start_index < 0 or start_index == end_index:
            return -1

        if item > array[cur_index]:
            start_index = cur_index + 1
        else:
            end_index = cur_index - 1

        cur_index = (end_index - start_index)  // 2 + start_index

    return cur_index




# Класс бинарного дерева
class BinaryTree:
    def __init__(self, first, index):
        self.tree = [[first, index], [], []]

    def add(self, number, index):
        parent = self.tree
        while len(parent) > 0:
            parent = parent[1 if parent[0][0] > number else 2]
        parent.extend([[number, index], [], []])

    def find_index(self, number):
        parent = self.tree
        while len(parent) > 0:
            if parent[0][0] == number:
                return parent[0][1]
            parent = parent[1 if parent[0][0] > number else 2]
        return -1

# def binary_tree_search(array, number):
#     tree = BinaryTree(array[0], 0)
#     for i in range(1, len(array)):
#         tree.add(array[i], i)
#
#     return tree.find_index(number)


# def binary_tree_search(array, number):
#     # Формирование дерева
#     tree = [[array[0], 0], [], []]
#     for i in range(1, len(array)):
#         sub_array = tree
#         while len(sub_array) > 0:
#             sub_array = sub_array[1 if sub_array[0][0] > number else 2]
#         sub_array.extend([[array[i], i], [], []])
#
#     # Сам поиск
#     while len(tree) > 0:
#         if tree[0][0] == number:
#             return tree[0][1]
#         tree = tree[1 if tree[0][0] > number else 2]

def create_binary_tree(array):
    tree = [[array[0], 0], [], []]
    for i in range(1, len(array)):
        sub_array = tree
        while len(sub_array) > 0:
            sub_array = sub_array[1 if sub_array[0][0] > array[i] else 2]
        sub_array.extend([[array[i], i], [], []])
    return tree

def tree_search(tree, number):
    while len(tree) > 0:
        if tree[0][0] == number:
            return tree[0][1]
        tree = tree[1 if tree[0][0] > number else 2]


def fib_search(array, number):
    size = len(array)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while f2 > 1:
        index = min(start + f0, size - 1)
        if array[index] < number:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > number:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if f1 and (array[size - 1] == number):
        return size - 1

    return -1




def interpolation_search(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and lys[low] <= val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1




def native_search(array, val):
    return array.index(val)

def count_time(func, count, *args):
    t = 0
    for i in range(count):
        start = time.time()
        func(*args)
        t += time.time() - start
    return t / count


count = 100000
random_array = random_array_generator(count, 0)
random_index = random.randrange(0, count)

print()

print("Binary search: " + str(count_time(binary_search, 1, random_array, random_array[random_index])))

print("Fibonacci search: " + str(count_time(fib_search, 1, random_array, random_array[random_index])))

print("Interpolation search: " + str(count_time(interpolation_search, 1, random_array, random_array[random_index])))

print("Native search: " + str(count_time(native_search, 1, random_array, random_array[random_index])))

print()


one = [i for i in range(100000)]

print("Interpolation search in random array: " + str(count_time(interpolation_search, 1000000, random_array, random_array[random_index])))
print("Interpolation search in single dif array: " + str(count_time(interpolation_search, 1000000, one, one[random_index])))
print()

random_array = random_array_generator(1000, 0)
tree = create_binary_tree(random_array)
print("Binary tree search: " + str(count_time(tree_search, 1, tree, random_index)))
