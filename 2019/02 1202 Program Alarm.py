import sys
from itertools import zip_longest

with open('02.txt') as f:
    memory = list(map(int, f.read().split(',')))

class AddressSpace:
    def __init__(self, program):
        self.program = list(program) + [0,0,0]
    def __getitem__(self, k):
        return self.program[k]
    def __setitem__(self, k, v):
        self.program[k] = v

def get_instructions(instructions, size=4):
    return zip_longest(*([iter(instructions)] * size))

def add(loc_a, loc_b, loc_result):
    mem[loc_result] = mem[loc_a] + mem[loc_b]

def mul(loc_a, loc_b, loc_result):
    mem[loc_result] = mem[loc_a] * mem[loc_b]

class Stop(Exception):
    pass

def stop(*args):
    raise Stop('99')

def run(mem):
    for instruction in get_instructions(mem.program, size=4):
        op = codes[instruction[0]]
        try:
            op(*instruction[1:])
        except Stop:
            break

codes = {
    1: add,
    2: mul,
    99: stop,
}

found = False
for i1 in range(0, 99):
    for i2 in range(0, 99):
        mem = AddressSpace(program=memory)
        mem.program[1] = i1
        mem.program[2] = i2
        run(mem)
        if mem.program[0] == 19690720:
            print([i1, i2])
            found = True
            break
    if found:
        break

mem = AddressSpace(program=memory)
mem.program[1] = i1
mem.program[2] = i2
run(mem)
assert mem.program[0] == 19690720
