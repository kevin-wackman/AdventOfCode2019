import day
from typing import List

class Day1():
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_input(self) -> List[int]:
        fp = open(self.file_path)
        arr = []
        for n in fp:
            arr.append(int(n))
        return arr

    def run_day(self):
        parsed_input = self.parse_input()
        print(self.run_part_1(parsed_input))
        print(self.run_part_2(parsed_input))

    def run_part_1(self, parsed_input):
        tot = 0
        for n in parsed_input:
            tot += get_required_fuel(n)
        return tot

    def run_part_2(self, parsed_input):
        tot = 0
        for n in parsed_input:
            tot += get_mass_until_zero(n)
        return tot


def get_required_fuel(mass: int) -> int:
    return (mass // 3) - 2

def get_mass_until_zero(mass: int) -> int:
    tot = 0
    fuel_mass = get_required_fuel(mass)
    while fuel_mass > 0:
        tot += fuel_mass
        fuel_mass = get_required_fuel(fuel_mass)
    return tot

today = Day1("day1in.txt")
today.run_day()