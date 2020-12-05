import datetime
from day5 import Day5

def main():
    day = Day5("input5.txt")
    print(f'Day {datetime.datetime.now().day}:')
    print(f'Part One: {day.part_one()}')
    print(f'Part Two: {day.part_two()}')

main()