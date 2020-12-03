import datetime
from day3 import Day3

def main():
    day = Day3("input3.txt")
    print(f'Day {datetime.datetime.now().day}:')
    print(f'Part One: {day.part_one()}')
    print(f'Part One: {day.part_two()}')

main()