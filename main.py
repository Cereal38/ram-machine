import sys

from lexical_analysis import lexical_analysis

DEBUG = True
NB_REGISTERS = 32
used_registers = []


def update_used_registers(i):
    if i not in used_registers:
        used_registers.append(i)


def copy(registers, i, j):
    if DEBUG:
        print(f"copy r{j} r{i}")
    registers[i] = registers[j]
    update_used_registers(i)
    update_used_registers(j)


def inc(registers, i):
    if DEBUG:
        print(f"inc r{i} : {registers[i]} -> {registers[i] + 1}")
    registers[i] += 1
    update_used_registers(i)


def dec(registers, i):
    if DEBUG:
        print(f"dec r{i} : {registers[i]} -> {registers[i] - 1}")
    registers[i] -= 1
    update_used_registers(i)


def jump(registers, i, ligne):
    if registers[i] == 0:
        if DEBUG:
            print(f"jump r{i} {ligne+1} : r{i} == 0, jumping to line {ligne+1}")
        return ligne
    else:
        if DEBUG:
            print(f"jump r{i} {ligne+1} : r{i} == {registers[i]}, not jumping")
        return None


def execute_program(program, registers_init: list = None):
    registers = [0] * NB_REGISTERS
    instruction_pointer = 0

    # Initialize registers
    if registers_init is not None:
        for i, value in enumerate(registers_init):
            registers[i] = value
            update_used_registers(i)

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]

        if instruction.startswith("copy"):
            _, i, j = instruction.split()
            # Remove the "R" prefix
            copy(registers, int(i[1:]), int(j[1:]))
        elif instruction.startswith("inc"):
            _, i = instruction.split()
            inc(registers, int(i[1:]))
        elif instruction.startswith("dec"):
            _, i = instruction.split()
            dec(registers, int(i[1:]))
        elif instruction.startswith("jump"):
            _, i, ligne = instruction.split()
            # Add -1 to ligne because we start at 0
            jump_label = jump(registers, int(i[1:]), int(ligne) - 1)
            if jump_label is not None:
                instruction_pointer = jump_label
                continue
        elif instruction.startswith("stop"):
            break

        instruction_pointer += 1

    return registers


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <program_file> <R0> <R1> ...")
        return

    # Get program file and initial register values
    program_file = sys.argv[1]
    registers_init = [int(arg) for arg in sys.argv[2:]]

    with open(program_file, "r") as file:
        program = file.readlines()

    # Create a list of instructions and check syntax
    program = [line.strip() for line in program]
    if not lexical_analysis(program, NB_REGISTERS):
        exit(1)

    registers = execute_program(program, registers_init)

    print() if DEBUG else None  # Line break if debug mode is on
    print("Final register values:")
    for i, value in enumerate(registers):
        if i in used_registers:
            print(f"R{i}: {value}")


if __name__ == "__main__":
    main()
