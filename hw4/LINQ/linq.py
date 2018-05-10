import re


class My_Linq:
    def __init__(self, d):
        self.data = d

    def Select(self, func):
        res = (func(item) for item in self.data)
        return My_Linq(res)

    def Flatten(self):
        res = (item for items in self.data for item in items)
        return My_Linq(res)

    def Where(self, pred):
        res = (item for item in self.data if pred(item))
        return My_Linq(res)

    def Take(self, k):
        res = []
        for i in range(k):
            res.append(next(self.data))
        return My_Linq(res)

    def GroupBy(self, key):
        res = {}
        for item in self.data:
            k = key(item)
            if k not in res.keys():
                res[k] = []
            res[k].append(item)
        res = res.items()
        return My_Linq(res)

    def OrderBy(self, key):
        res = (sorted(self.data, key=key))
        return My_Linq(res)

    def ToList(self):
        return list(self.data)


# Задача 1
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

task1 = My_Linq(fibonacci())
print(task1.
      Where(lambda item : item % 3 == 0).
      Select(lambda item: item if item % 2 == 1 else item * item).
      Take(5).
      ToList())


# Задача 2
def spliting(string):
    res = re.split(r"[;,.?!:—\s]", string)
    res = filter(lambda item: item != '', res)
    return res

with open("task2.txt", 'r') as f:
    print(My_Linq(f.readlines()).
          Select(spliting).
          Flatten().
          GroupBy(lambda x: x).
          Select(lambda pair: (len(pair[1]), pair[0])).
          OrderBy(lambda pair : -pair[0]).
          ToList())
