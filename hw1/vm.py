import sys
import numpy as np
import help as h


class MemoryVM:
    def __init__(self, size):
        self.memory = np.zeros(size, dtype=np.int32)

    def get(self, address):
        return self.memory[address]

    def set(self, address, val):
        self.memory[address] = val


class Interpreter:
    def __init__(self, mem, off):
        self.memory = mem
        self.offset = off
        self.function_start_point = {}
        self.function_of_get = False

    def run(self):
        while True:
            command = self.memory.get(self.ip())
            level1 = self.memory.get(self.ip() + 1)
            arg1 = self.memory.get(self.ip() + 2)
            level2 = self.memory.get(self.ip() + 3)
            arg2 = self.memory.get(self.ip() + 4)

            if not self.descriptor(command, level1, arg1, level2, arg2):
                return

    def descriptor(self, command, level1, arg1, level2, arg2):
        if self.function_of_get and command != h.COMMAND_END:
            self.next()
            return True

        elif command == h.COMMAND_BEGIN:
            self.next()
            self.function_of_get = True
            self.function_start_point[arg1] = self.ip()
            return True

        elif command == h.COMMAND_END:
            self.next()
            self.function_of_get = False
            return True

        elif command == h.COMMAND_CALL:
            self.next()
            self.push(0, self.ip())
            self.move(1, h.IP_INDEX, 0, self.function_start_point[arg1])
            return True

        elif command == h.COMMAND_ADD:
            self.next()
            self.add(level1, arg1, level2, arg2)
            return True

        elif command == h.COMMAND_SUB:
            self.next()
            self.sub(level1, arg1, level2, arg2)
            return True

        elif command == h.COMMAND_MOVE:
            self.next()
            self.move(level1, arg1, level2, arg2)
            return True

        elif command == h.COMMAND_GO:
            self.next()
            if self.dereference(level1, arg1) != level2:
                self.add(1, h.IP_INDEX, 0, (arg2 - 1) * h.IP_OFFSET)
            return True

        elif command == h.COMMAND_POP:
            self.next()
            self.memory.set(self.sp(), 0)
            self.add(1, h.SP_INDEX, 0, 1)
            return True

        elif command == h.COMMAND_PUSH:
            self.next()
            self.push(level1, arg1)
            return True

        elif command == h.COMMAND_GET:
            self.next()
            value = input()
            self.memory.set(self.dereference(level1 - 1, arg1), value)
            return True

        elif command == h.COMMAND_PUT_STR:
            self.next()
            string = ''
            for i in range(arg1):
                string += chr(self.memory.get(len(h.REGISTERS) + self.offset + level1 + i))
            print(string)
            return True

        elif command == h.COMMAND_PRINT:
            self.next()
            print(self.dereference(level1, arg1))
            return True

        elif command == h.COMMAND_EXIT:
            return False

        else:
            return False

    def ip(self):
        return self.memory.get(h.IP_INDEX)

    def sp(self):
        return self.memory.get(h.SP_INDEX)

    def next(self):
        self.memory.set(h.IP_INDEX, self.ip() + h.IP_OFFSET)

    def dereference(self, level, value):
        for i in range(level):
            value = self.memory.get(value)
        return value

    def add(self, level1, arg1, level2, arg2):
        value = self.dereference(level1, arg1) + self.dereference(level2, arg2)
        self.memory.set(self.dereference(level1 - 1, arg1), value)

    def move(self, level1, arg1, level2, arg2):
        value = self.dereference(level2, arg2)
        self.memory.set(self.dereference(level1 - 1, arg1), value)

    def push(self, level1, arg1):
        self.sub(1, h.SP_INDEX, 0, 1)
        self.move(2, h.SP_INDEX, level1, arg1)

    def sub(self, level1, arg1, level2, arg2):
        value = self.dereference(level1, arg1) - self.dereference(level2, arg2)
        self.memory.set(self.dereference(level1 - 1, arg1), value)


if len(sys.argv) > 1:
    memory = MemoryVM(500)
    memory.set(h.IP_INDEX, len(h.REGISTERS) + 1)
    memory.set(h.SP_INDEX, 500)

    bytecode = np.fromfile(sys.argv[1], dtype=np.int32)[::2]

    for i, byte in enumerate(bytecode):
        memory.set(len(h.REGISTERS) + i, byte)

    interpreter = Interpreter(memory, bytecode[0])
    interpreter.run()
