# Инструкции виртуальной машины

# begin -- Начало описания функции <name> [0 0 <name> 0 0]
STR_BEGIN = 'begin'
COMMAND_BEGIN = 0

# end -- Конец описания функции [1 0 0 0 0]
STR_END = 'end'
COMMAND_END = 1

# call` -- Вызов функции <name> [2 0 <name> 0 0]
STR_CALL = 'call'
COMMAND_CALL = 2

# add -- Сложение двух операндов (резултат в первом) [3 <level1> <arg1> <level2> <arg2>]
#   здесь level -- кол-во разыменований до оператора, arg -- аргумент
STR_ADD = 'add'
COMMAND_ADD = 3

# sub -- Разность первого и второго операндов (результат в первом) [4 <level1> <arg1> <level2> <arg2>] --//--
STR_SUB = 'sub'
COMMAND_SUB = 4

# move -- Перезапись первого операнда вторым [5 <level1> <arg1> <level2> <arg2>] --//--
STR_MOVE = 'move'
COMMAND_MOVE = 5

# go -- Проход на <offset> инструкций вперед (если это возможно) [6 <level> <arg> 0 <offset>] --//--
STR_GO = 'go'
COMMAND_GO = 6

# pop -- Перемещение указателя стека вперед [7 0 0 0 0]
STR_POP = 'pop'
COMMAND_POP = 7

# push -- Запись операнда в стек [8 <level> <arg> 0 0] --//--
STR_PUSH = 'push'
COMMAND_PUSH = 8

# get -- Чтение ввода [9 <level> <arg> 0 0] --//--
STR_GET = 'get'
COMMAND_GET = 9

# put_str -- Вывод текста длины <len> начиная со смещения <offset> [10 <offset> <len> 0 0]
STR_PUT_STR = 'put_str'
COMMAND_PUT_STR = 10

# print -- Вывод операнда [11 <level> <arg> 0 0] --//--
STR_PRINT = 'print'
COMMAND_PRINT = 11

# exit -- Конец работы [12 0 0 0 0]
STR_EXIT = 'exit'
COMMAND_EXIT = 12

IP_INDEX = 0
SP_INDEX = 1

IP_OFFSET = 5

REGISTERS = {'ip': 0, 'sp': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7}

RE_REGISTERS = {0: 'ip', 1: 'sp', 2: 'a', 3: 'b', 4: 'c', 5: 'd', 6: 'e', 7: 'f'}
