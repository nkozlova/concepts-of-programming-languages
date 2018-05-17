import re


class My_Linq:
    def __init__(self, d):
        self.data = d

    def Select(self, func):
        '''
        Select – применение некоторой операции к каждому элементу последовательности;
        '''
        res = (func(item) for item in self.data)
        return My_Linq(res)

    def Flatten(self):
        '''
        Flatten – выпрямление последовательности последовательностей в плоскую последовательность;
        '''
        res = (item for items in self.data for item in items)
        return My_Linq(res)

    def Where(self, pred):
        '''
        Where – фильтрация последовательности по некоторому предикату;
        '''
        res = (item for item in self.data if pred(item))
        return My_Linq(res)

    def Take(self, k):
        '''
        Take – взять первые k элементов из последовательности;
        '''
        res = (next(self.data) for i in range(k))
        return My_Linq(res)

    def GroupBy(self, key):
        '''
        GroupBy – сгруппировать элементы по заданному ключу.
        В результате должна получиться последовательность пар
        <ключ, последовательность соответствующих этому ключу элементов>.
        Аналогично обычному LINQ ключом может быть функция от элементов;
        '''
        res = {}
        for item in self.data:
            k = key(item)
            if k not in res.keys():
                res[k] = []
            res[k].append(item)
        res = res.items()
        return My_Linq(res)

    def OrderBy(self, key):
        '''
        OrderBy – отсортировать элементы по заданному ключу – функции от элементов;
        '''
        res = (sorted(self.data, key=key))
        return My_Linq(res)

    def ToList(self):
        '''
        ToList – положить все элементы последовательности в список.
        '''
        return list(self.data)


# Задача 1
'''
Реализовать бесконечный поток чисел Фибоначчи,
выбрать из них только делящиеся на 3,
возвести в квадрат каждое четное и
взять первые пять полученных чисел.
'''


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
'''
Реализовать Word Count для некоторого текстового файла.
Нужно разбить строки файла по пробелу и для каждого полученного токена посчитать число его появлений в данном файле.
Токены и их частоты должны быть выведены отсортированными по частоте.
'''


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
