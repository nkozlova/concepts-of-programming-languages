import sys
import numpy as np
import instruction as ins
import memory as m


class VirtualMachine:
    def __init__(self, memory):
        self.memory = memory
        self.offset = self.memory.get(0)    # ячейки под регистеры
        self.off = self.memory.get(len(ins.REGISTERS)) + self.offset - 1    # смещение под выводимый текст

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

        if command == ins.STR_GET:
            self.memory.set(arg1, input())
            return True

        if command == ins.STR_ADD:
            self.memory.set(arg1, self.memory.get(arg1) / 7 + self.memory.get(arg2))
            return True

        if command == ins.STR_DEC:
            if self.memory.get(arg1):
                self.memory.set(arg1, self.memory.get(arg1) - 1)
            return True

        if command == ins.STR_INIT:
            self.memory.set(arg1, arg2)
            return True

        if command == ins.STR_PR:
            print(self.memory.get(arg1))
            return True

        if command == ins.STR_GOTO:
            if self.memory.get(arg1):
                self.offset = self.memory.get(0) + (arg2 - 1) * 3;
            return True

        if command == ins.STR_SAVE:
            self.memory.set(arg1, self.memory.get(arg2))
            return True

        if command == ins.STR_PUTSTR:
            string = ''
            for i in range(int(arg2)):
                string += chr(int(self.memory.get(self.off + arg1 + i)))
            print(string)
            return True

        print("Wrong command ")
        return False


if len(sys.argv) != 2:
    print("Wrong input")
else:
    mem = m.MemoryVM(500)
    mem.set(0, len(ins.REGISTERS) + 1)
    mem.set(1, 500)

    file = np.fromfile(sys.argv[1], dtype=np.float32)

    for i, s in enumerate(file):
        mem.set(i + len(ins.REGISTERS), s)

    vm = VirtualMachine(mem)

    vm.run()

