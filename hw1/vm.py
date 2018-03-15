import sys
import numpy as np
import instruction as ins
import memory as m


class VirtualMachine:
    def __init__(self, memory):
        self.memory = memory
        self.offset = self.memory.get(0)    # ячейки под регистеры
        self.off = self.memory.get(len(ins.REGISTERS)) + self.offset - 1 # смещение под текст

    def run(self):
        while True:
            command = self.memory.get(self.offset)
            arg1 = self.memory.get(self.offset + 1)
            arg2 = self.memory.get(self.offset + 2)

            if not self.descriptor(command, arg1, arg2):
                break

            self.offset += 3


    def descriptor(self, command, arg1, arg2):
        if command == ins.STR_EXIT:
            return False
        elif command == ins.STR_GET:
            self.memory.set(arg1, input())
            return True
        elif command == ins.STR_ADD:
            self.memory.set(arg1, self.memory.get(arg1) + self.memory.get(arg2))
            return True
        elif command == ins.STR_SUB:
            if self.memory.get(arg1):
                self.memory.set(arg1, self.memory.get(arg1) - 1)
            return True
        elif command == ins.STR_INIT:
            self.memory.set(arg1, arg2)
            return True
        elif command == ins.STR_PR:
            print(self.memory.get(arg1))
            return True
        elif command == ins.STR_GOTO:
            if self.memory.get(arg1):
                self.offset = self.memory.get(0) + (arg2 - 1) * 3;
            return True
        elif command == ins.STR_SW:
            tmp = self.memory.get(arg1)
            self.memory.set(arg1, self.memory.get(arg2))
            self.memory.set(arg2, tmp)
            return True
        elif command == ins.STR_PUTSTR:
            string = ''
            for i in range(arg2):
                string += chr(self.memory.get(self.off + arg1 + i))
            print(string)
            return True
        else:
            print("Wrong command ")
            return False


if len(sys.argv) != 2:
    print("Wrong input")
else:
    mem = m.MemoryVM(500)
    mem.set(0, len(ins.REGISTERS) + 1)
    mem.set(1, 500)

    file = np.fromfile(sys.argv[1], dtype=np.int32)

    for i, s in enumerate(file):
        mem.set(i + len(ins.REGISTERS), s)

    vm = VirtualMachine(mem)

    vm.run()

