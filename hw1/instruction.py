REGISTERS = {2: 'a', 3: 'b', 4: 'c'}
RE_REGISTERS = {'a': 2, 'b': 3, 'c': 4}

ADD = 'add'  # принятие 2 регистров, запись суммы в 1 из них
STR_ADD = 0

SUB = 'sub'  # принятие 1 регистра, откуда вычитается 1
STR_SUB = 7

PR = 'pr'    # вывод значения регистра на экран
STR_PR = 1

INIT = 'init'  # запись значения в регистр
STR_INIT = 2

GOTO = 'goto'   # принятие 2 регистров: флаг перехода и индекс строчки, на которую надо перейти, если флаг != 0
STR_GOTO = 3

SW = 'sw'   # оператор swap обмена регистров
STR_SW = 4

GET = 'get' # получение ввода пользователя
STR_GET = 5 # [5 <регистр> 0]

EXIT = 'exit'   # конец проги
STR_EXIT = 6

PUTSTR = 'putstr'   # вывести строку
STR_PUTSTR = 8