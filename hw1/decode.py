import sys
import instruction as ins
import numpy as np


def detected_command(data, command, arg1, arg2, offset):
    if command == ins.STR_ADD:
        return ins.ADD + ' ' + ins.REGISTERS[arg1] + ' ' + ins.REGISTERS[arg2] + '\n'

    if command == ins.STR_DEL:
        return ins.DEL + ' ' + ins.REGISTERS[arg1] + ' ' + ins.REGISTERS[arg2] + '\n'

    if command == ins.STR_DEC:
        return ins.DEC + ' ' + ins.REGISTERS[arg1] + '\n'

    if command == ins.STR_PR:
        return ins.PR + ' ' + ins.REGISTERS[arg1] + '\n'

    if command == ins.STR_GET:
        return ins.GET + ' ' + ins.REGISTERS[arg1] + '\n'

    if command == ins.STR_INIT:
        return ins.INIT + ' ' + ins.REGISTERS[arg1] + ' ' + str(arg2) + '\n'

    if command == ins.STR_GOTO:
        return ins.GOTO + ' ' + ins.REGISTERS[arg1] + ' ' + str(arg2) + '\n'

    if command == ins.STR_SAVE:
        return ins.SAVE + ' ' + ins.REGISTERS[arg1] + ' ' + ins.REGISTERS[arg2] + '\n'

    if command == ins.STR_EXIT:
        return ins.EXIT + '\n'

    if command == ins.STR_PUTSTR:
        string = ins.PUTSTR + ' '
        for i in range(int(arg2)):
            string += chr(int(data[offset + arg1 + i + 1]))
        return string + '\n'

    return '\n'


def write_to_file(file, commands):
    file = open(file, 'w')

    offset = commands[0] - 1
    limit = int((commands[0] - 1) / 3)

    for i in range(limit):
        command = commands[3 * i + 1]
        arg1 = commands[3 * i + 2]
        arg2 = commands[3 * i + 3]

        file.write(detected_command(commands, command, arg1, arg2, offset))


def read_from_file(file):
    return np.fromfile(file, dtype=np.float32)


if len(sys.argv) != 3:
    print("Wrong input")
else:
    commands = read_from_file(sys.argv[1])
    write_to_file(sys.argv[2], commands)
