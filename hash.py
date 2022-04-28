


class HashMap:
    def __init__(self):
        self.array=[None] * 64
    def hash_function(self, value):
        return len(value) - 1
    def add(self, string):
        offset = 0
        currentIndex = self.hash_function(string)
        while self.array[currentIndex] is not None or currentIndex == len(self.array):
            offset += 1
            currentIndex = self.hash_function(string) + offset
        self.array[currentIndex] = string
        return currentIndex
    def get(self, string):
        offset = 0
        currentIndex = self.hash_function(string)
        while self.array[currentIndex] != string:
            offset += 1
            currentIndex = self.hash_function(string) + offset
            if currentIndex == len(self.array):
                return False
        return currentIndex


mapa = HashMap()

data1 = "Сообщение номер один"
data2 = "Следующее сообщение"
data3 = "Сообщение которе не вставлено"

index1 = mapa.add(data1)
print(f"Значение \"{data1}\" было записано с хешкодом: \"{index1}\"")

index2 = mapa.add(data2)
print(f"Значение \"{data2}\" было записано с хешкодом: \"{index2}\"")

get_index2 = mapa.get(data2)
if not get_index2:
    print(f"Значение \"{data2}\" не найдено")
else:
    print(f"Значение \"{data2}\" найдено с хешкодом \"{get_index2}\"")

get_index3 = mapa.get(data3)
if not get_index3:
    print(f"Значение \"{data3}\" не найдено")

print(mapa.array)
print()


class ChainedHashMap:
    def __init__(self):
        self.array=[[] for i in range(64)]

    def hash_function(self, value):
        return len(value) - 1

    def add(self, string):
        _hash = self.hash_function(string)
        self.array[_hash].append(string)
        return _hash

    def get(self, string):
        _hash = self.hash_function(string)
        if len(self.array[_hash]) == 0: return False

        for i in range(len(self.array[_hash])):
            if self.array[_hash][i] == string: return i

        return False

cmapa = ChainedHashMap()
cmapa.add("Первая строка")
cmapa.add("Вторая строка")
cmapa.add("Третья строка")
cmapa.add("Четвёртая строка")

print(cmapa.array)

print()

class RandomReHash:
    def __init__(self):
        self.array = [None] * 999
    def hash_function(self, value):
        return len(value) - 1
    def add(self, string):
        from random import seed, random
        offset = 0
        currentIndex = self.hash_function(string)
        seed(currentIndex)
        _hash = int(str(random()).split('.')[1][0:3])
        while self.array[_hash] is not None:
            offset += 1
            currentIndex = self.hash_function(string) + offset
            seed(currentIndex)
            _hash = int(str(random()).split('.')[1][0:3])
            if currentIndex == len(self.array):
                return False
        self.array[_hash] = string
        return _hash
    def get(self, string):
        from random import seed, random
        offset = 0
        currentIndex = self.hash_function(string)
        seed(currentIndex)
        _hash = int(str(random()).split('.')[1][0:3])
        while self.array[_hash] != string:
            offset += 1
            currentIndex = self.hash_function(string) + offset
            seed(currentIndex)
            _hash = int(str(random()).split('.')[1][0:3])
            if currentIndex == len(self.array):
                return False
        return _hash


rmapa = RandomReHash()
print(rmapa.add("Строка"))
print(rmapa.add("Строка"))
print(rmapa.add("Строка"))
print(rmapa.add("Строка 2"))
print()
print(rmapa.get("Строка"))