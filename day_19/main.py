import re

with open('input.txt', 'r') as f:
    input_data = f.read()

    instruction_pointer = int(re.findall(
        r'^#ip\s(\d+)$', input_data, re.MULTILINE)[0])

    instructions = []
    for i in re.finditer(
            r'^(\w+)\s(\d+)\s(\d+)\s(\d+)$', input_data, re.MULTILINE):
        op, f_in, s_in, out = i.groups()
        instructions.append((op, int(f_in), int(s_in), int(out)))


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



def solve_part_1(instructions, instruction_pointer_at):
    registers = [0, 0, 0, 0, 0, 0]
    instruction_pointer = 0

    while instruction_pointer < len(instructions):
        registers[instruction_pointer_at] = instruction_pointer

        op, f_in, s_in, out = instructions[instruction_pointer]
        globals()[op](registers, f_in, s_in, out)

        instruction_pointer = registers[instruction_pointer_at]
        instruction_pointer += 1

    return registers[0]

def calculate_number(instructions, instruction_pointer_at):
    registers = [1, 0, 0, 0, 0, 0]
    instruction_pointer = 0

    instr_no_calculated = {}

    while instruction_pointer < len(instructions):
        registers[instruction_pointer_at] = instruction_pointer

        op, f_in, s_in, out = instructions[instruction_pointer]
        globals()[op](registers, f_in, s_in, out)

        instruction_pointer = registers[instruction_pointer_at]
        instruction_pointer += 1
        if instruction_pointer in instr_no_calculated:
            break
        instr_no_calculated[instruction_pointer] = True
    
    return registers[5]

def solve_part_2(instructions, instruction_pointer_at):
    num = calculate_number(instructions, instruction_pointer_at)

    # calculate all divisors
    s = [i for i in range(2, (num // 2) + 1) if num % i == 0]

    # add 1 and the number itself to the sum
    s.extend([1, num])
    return sum(s)


first_part = solve_part_1(instructions, instruction_pointer)
print('First part: {0}'.format(first_part))

second_part = solve_part_2(instructions, instruction_pointer)
print('Second part: {0}'.format(second_part))
