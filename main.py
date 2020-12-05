import datetime
from day4 import Day4

def main():
    day = Day4("input4.txt")
    print(f'Day {datetime.datetime.now().day}:')
    print(f'Part One: {day.part_one()}')
    print(f'Part Two: {day.part_two()}')

main()