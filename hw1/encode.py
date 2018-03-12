import sys
import numpy as np
import help as h


class Encoder:
    def __init__(self, input_, output_):
        self.offset = 0
        self.input = input_
        self.output = output_
        self.program = np.array([], dtype=np.int32)
        self.static = np.array([], dtype=np.int32)

    def encode(self):
        file = open(self.input, 'r')

        for line in file:
            self.program = np.append(self.program, self.descriptor(line))

        self.program = np.array([len(self.program) + 1, ] + list(self.program) + list(self.static))

        self.program.tofile(self.output)

    def descriptor(self, line_):
        line = line_.split()
        command = line[0]

        if command == h.STR_BEGIN:
            return np.array([h.COMMAND_BEGIN, 0, hash(line[1]), 0, 0])

        elif command == h.STR_END:
            return np.array([h.COMMAND_END, 0, 0, 0, 0])

        elif command == h.STR_CALL:
            return np.array([h.COMMAND_CALL, 0, hash(line[1]), 0, 0])

        elif command == h.STR_ADD:
            level1, arg1 = self.get_arguments(line[1])
            level2, arg2 = self.get_arguments(line[2])
            return np.array([h.COMMAND_ADD, level1, arg1, level2, arg2])

        elif command == h.STR_SUB:
            level1, arg1 = self.get_arguments(line[1])
            level2, arg2 = self.get_arguments(line[2])
            return np.array([h.COMMAND_SUB, level1, arg1, level2, arg2])

        elif command == h.STR_MOVE:
            level1, arg1 = self.get_arguments(line[1])
            level2, arg2 = self.get_arguments(line[2])
            return np.array([h.COMMAND_MOVE, level1, arg1, level2, arg2])

        elif command == h.STR_GO:
            level1, arg1 = self.get_arguments(line[1])
            level2, arg2 = self.get_arguments(line[2])
            return np.array([h.COMMAND_GO, level1, arg1, level2, arg2])

        elif command == h.STR_POP:
            return np.array([h.COMMAND_POP, 0, 0, 0, 0])

        elif command == h.STR_PUSH:
            level, arg = self.get_arguments(line[1])
            return np.array([h.COMMAND_PUSH, level, arg, 0, 0])

        elif command == h.STR_GET:
            level, arg = self.get_arguments(line[1])
            return np.array([h.COMMAND_GET, level, arg, 0, 0])

        elif command == h.STR_PUT_STR:
            line = line_.split(maxsplit=1)[1].strip()
            code = np.array([], dtype=np.int32)
            for symbol in line:
                code = np.append(code, ord(symbol))
            self.offset += len(line)
            self.static = np.append(self.static, code)
            return np.array([h.COMMAND_PUT_STR, self.offset - len(line), len(line), 0, 0])

        elif command == h.STR_PRINT:
            level, arg = self.get_arguments(line[1])
            return np.array([h.COMMAND_PRINT, level, arg, 0, 0])

        elif command == h.STR_EXIT:
            return np.array([h.COMMAND_EXIT, 0, 0, 0, 0])

        else:
            exit("It's wrong command")

    @staticmethod
    def get_arguments(str):
        level = 0

        for symbol in str:
            if symbol == '*':
                level += 1
            else:
                arg = str[level:]
                try:
                    arg = int(arg)
                except ValueError:
                    arg = h.REGISTERS[arg]
                return level, arg


if len(sys.argv) > 2:
    encoder = Encoder(sys.argv[1], sys.argv[2])
    encoder.encode()
