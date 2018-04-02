import numpy as np


class MemoryVM:
    def __init__(self, size):
        self.memory = np.zeros(size, dtype=np.float32)

    def get(self, addr):
        return self.memory[addr]

    def set(self, addr, val):
        self.memory[addr] = val
