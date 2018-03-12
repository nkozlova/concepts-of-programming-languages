import sys
import numpy as np
import help as h


class Decoder:
    def __init__(self, input_, output_):
        self.offset = 0
        self.input = input_
        self.output = output_
        self.program = np.array([], dtype=np.int32)
        self.static = np.array([], dtype=np.int32)

    def decode(self):
        data = np.fromfile(self.input, dtype=np.int32)[::2]

        output = open(self.output, 'w')

        self.offset = data[0]
        limit = int((self.offset - 1) / h.IP_OFFSET)

        for i in range(limit):
            command = data[h.IP_OFFSET * i + 1]
            level1 = data[h.IP_OFFSET * i + 2]
            arg1 = data[h.IP_OFFSET * i + 3]
            level2 = data[h.IP_OFFSET * i + 4]
            arg2 = data[h.IP_OFFSET * i + 5]

            output.write(self.descriptor(data, command, level1, arg1, level2, arg2))

    def descriptor(self, data, command, level1, arg1, level2, arg2):
        if command == h.COMMAND_BEGIN:
            return h.STR_BEGIN + ' ' + str(arg1) + '\n'

        elif command == h.COMMAND_END:
            return h.STR_END + '\n'

        elif command == h.COMMAND_CALL:
            return h.STR_CALL + ' ' + str(arg1) + '\n'

        elif command == h.COMMAND_ADD:
            return h.STR_ADD + self.get_argument(level1, arg1) + self.get_argument(level2, arg2) + '\n'

        elif command == h.COMMAND_SUB:
            return h.STR_SUB + self.get_argument(level1, arg1) + self.get_argument(level2, arg2) + '\n'

        elif command == h.COMMAND_MOVE:
            return h.STR_MOVE + self.get_argument(level1, arg1) + self.get_argument(level2, arg2) + '\n'

        elif command == h.COMMAND_GO:
            return h.STR_GO + ' ' + '*' * level1 + h.RE_REGISTERS[arg1] + ' ' + str(arg2) + '\n'

        elif command == h.COMMAND_GET:
            return h.STR_GET + self.get_argument(level1, arg1) + '\n'

        elif command == h.COMMAND_POP:
            return h.STR_POP + '\n'

        elif command == h.COMMAND_PUSH:
            return h.STR_PUSH + self.get_argument(level1, arg1) + '\n'

        elif command == h.COMMAND_GET:
            return h.STR_GET + self.get_argument(level1, arg1) + '\n'

        elif command == h.COMMAND_PUT_STR:
            string = h.STR_PUT_STR + ' '
            for i in range(arg1):
                string += chr(data[self.offset + level1 + i])
            return string + '\n'

        elif command == h.COMMAND_PRINT:
            return h.STR_PRINT + self.get_argument(level1, arg1) + '\n'

        elif command == h.COMMAND_EXIT:
            return h.STR_EXIT + '\n'

        else:
            exit('Wrong function')

    @staticmethod
    def get_argument(level, arg):
        if level == 0:
            return ' ' + str(arg)
        else:
            return ' ' + '*' * level + h.RE_REGISTERS[arg]


if len(sys.argv) > 2:
    decoder = Decoder(sys.argv[1], sys.argv[2])
    decoder.decode()
