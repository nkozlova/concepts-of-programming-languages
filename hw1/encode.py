import sys
import instruction as ins
import numpy as np


def detected_command(line):
    if line[0] == ins.ADD:
        return np.array([ins.STR_ADD, ins.RE_REGISTERS[line[1]], ins.RE_REGISTERS[line[2]]], dtype=np.float32)

    if line[0] == ins.DEC:
        return np.array([ins.STR_DEC, ins.RE_REGISTERS[line[1]], 0], dtype=np.float32)

    if line[0] == ins.PR:
        return np.array([ins.STR_PR, ins.RE_REGISTERS[line[1]], 0], dtype=np.float32)

    if line[0] == ins.INIT:
        return np.array([ins.STR_INIT, ins.RE_REGISTERS[line[1]], line[2]], dtype=np.float32)

    if line[0] == ins.GET:
        return np.array([ins.STR_GET, ins.RE_REGISTERS[line[1]], 0], dtype=np.float32)

    if line[0] == ins.GOTO:
        return np.array([ins.STR_GOTO, ins.RE_REGISTERS[line[1]], line[2]], dtype=np.float32)

    if line[0] == ins.SAVE:
        return np.array([ins.STR_SAVE, ins.RE_REGISTERS[line[1]], ins.RE_REGISTERS[line[2]]], dtype=np.float32)

    if line[0] == ins.EXIT:
        return np.array([ins.STR_EXIT, 0, 0], dtype=np.float32)

    print("Wrong command ", line[0])
    return np.array([], dtype=np.float32)


def write_to_file(file, commands):
    commands.tofile(file)


def read_from_file(file):
    file = open(file, 'r')

    commands = np.array([], dtype=np.float32)
    static = np.array([], dtype=np.float32)
    offset = 0

    for line_ in file:
        line = line_.split()

        if line[0] == ins.PUTSTR:
            line = line_.split(maxsplit=1)[1].strip()
            for symbol in line:
                static = np.append(static, ord(symbol))
            commands = np.append(commands, [ins.STR_PUTSTR, offset, len(line)])
            offset += len(line)
        else:
            commands = np.append(commands, detected_command(line))

    commands = np.array([len(commands) + 1, ] + list(commands) + list(static), dtype=np.float32)
    return commands


if len(sys.argv) != 3:
    print("Wrong input")
else:
    commands = read_from_file(sys.argv[1])
    write_to_file(sys.argv[2], commands)
