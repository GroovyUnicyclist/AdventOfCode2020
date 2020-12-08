import datetime
from day6 import Day6

def main():
    day = Day6("input6.txt")
    print(f'Day {datetime.datetime.now().day}:')
    print(f'Part One: {day.part_one()}')
    print(f'Part Two: {day.part_two()}')

main()