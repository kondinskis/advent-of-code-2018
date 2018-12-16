import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    samples = []
    test_program = []
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        s = list(map(int, re.findall(r'\d+', line)))
        if len(s):
            if i < 3248:
                samples.append(s)
            else:
                test_program.append(s)


def addr(registers, f_in, s_in, out):
    registers[out] = registers[f_in] + registers[s_in]


def addi(registers, f_in, s_in, out):
    registers[out] = registers[f_in] + s_in


def mulr(registers, f_in, s_in, out):
    registers[out] = registers[f_in] * registers[s_in]


def muli(registers, f_in, s_in, out):
    registers[out] = registers[f_in] * s_in


def banr(registers, f_in, s_in, out):
    registers[out] = registers[f_in] & registers[s_in]


def bani(registers, f_in, s_in, out):
    registers[out] = registers[f_in] & s_in


def borr(registers, f_in, s_in, out):
    registers[out] = registers[f_in] | registers[s_in]


def bori(registers, f_in, s_in, out):
    registers[out] = registers[f_in] | s_in


def setr(registers, f_in, s_in, out):
    registers[out] = registers[f_in]


def seti(registers, f_in, s_in, out):
    registers[out] = f_in


def gtir(registers, f_in, s_in, out):
    registers[out] = 1 if f_in > registers[s_in] else 0


def gtri(registers, f_in, s_in, out):
    registers[out] = 1 if registers[f_in] > s_in else 0


def gtrr(registers, f_in, s_in, out):
    registers[out] = 1 if registers[f_in] > registers[s_in] else 0


def eqir(registers, f_in, s_in, out):
    registers[out] = 1 if f_in == registers[s_in] else 0


def eqri(registers, f_in, s_in, out):
    registers[out] = 1 if registers[f_in] == s_in else 0


def eqrr(registers, f_in, s_in, out):
    registers[out] = 1 if registers[f_in] == registers[s_in] else 0


def samples_three_or_more(samples):

    total = 0

    random_op_codes = {
        0: addr,
        1: addi,
        2: mulr,
        3: muli,
        4: banr,
        5: bani,
        6: borr,
        7: bori,
        8: setr,
        9: seti,
        10: gtir,
        11: gtri,
        12: gtrr,
        13: eqir,
        14: eqri,
        15: eqrr
    }

    possible_op_codes = defaultdict(set)

    for j in range(0, len(samples), 3):
        op, f_in, s_in, out = samples[j + 1]

        count = 0

        for i in range(16):
            registers = samples[j].copy()
            random_op_codes[i](registers, f_in, s_in, out)

            if registers == samples[j + 2]:
                count += 1
                possible_op_codes[op].add(random_op_codes[i].__name__)
        if count >= 3:
            total += 1

    real_op_codes = {}
    while len(real_op_codes.keys()) < 16:
        for key in possible_op_codes:
            if len(possible_op_codes[key]) == 1:
                oop = possible_op_codes[key].pop()
                real_op_codes[key] = globals()[oop]
                for kkey in possible_op_codes:
                    if kkey != key:
                        try:
                            possible_op_codes[kkey].remove(oop)
                        except KeyError:
                            pass

    return total, real_op_codes


def execute_test_program(test_program, op_codes):
    registers = [0, 0, 0, 0]

    for op, f_in, s_in, o in test_program:
        op_codes[op](registers, f_in, s_in, o)

    return registers[0]


first_part, op_codes = samples_three_or_more(samples)
print('First part: {0}'.format(first_part))

second_part = execute_test_program(test_program, op_codes)
print('Second part: {0}'.format(second_part))
