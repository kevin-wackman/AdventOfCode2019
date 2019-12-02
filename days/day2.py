import day
from typing import List
import operator

ADDITION_OPCODE = 1
MULTIPLICATION_OPCODE = 2
TERMINATION_OPCODE = 99
DESIRED_OUTPUT = 19690720

class Day2():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.original_tape = self.parse_input()
        self.refresh_tape()

    def parse_input(self) -> List[int]:
        fp = open(self.file_path)
        arr = fp.read().split(',')
        return list(map(int, arr))

    def refresh_tape(self) -> None:
        self.tape = self.original_tape.copy()

    def run_day(self) -> None:
        print(self.run_part_1())
        print(self.run_part_2())
        
    def run_part_1(self) -> int:
        self.refresh_tape()
        self.tape[1] = 12
        self.tape[2] = 2
        return self.run_program()

    def run_part_2(self) -> int:
        for i in range(100):
            for j in range(100):
                if self.test_inputs(i,j,19690720):
                    return i*100+j
        return -1

    def test_inputs(self, noun: int, verb: int, output: int) -> bool:
        self.refresh_tape()
        self.tape[1] = noun
        self.tape[2] = verb
        return self.run_program() == output

    def run_program(self) -> int:
        instruction_pointer = 0
        while self.run_iteration(instruction_pointer):
            instruction_pointer += 4
        return self.tape[0]

    def run_iteration(self, instruction_pointer: int) -> bool:
        if (instruction_pointer < 0) or (instruction_pointer >= len(self.tape)):
            return False
        if self.tape[instruction_pointer] == TERMINATION_OPCODE:
            return False
        combinator = operator.add if self.tape[instruction_pointer] == ADDITION_OPCODE else operator.mul
        numerator_loc = self.tape[instruction_pointer + 1]
        denominator_loc = self.tape[instruction_pointer + 2]
        result_loc = self.tape[instruction_pointer + 3]
        self.tape[result_loc] = combinator(self.tape[numerator_loc], self.tape[denominator_loc])
        return True

today = Day2("day2in.txt")
today.run_day()