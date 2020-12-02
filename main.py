import datetime
from day2 import Day2

def main():
    day = Day2("input2.txt")
    print(f'Day {datetime.datetime.now().day}:')
    print(f'Part One: {day.part_one()}')
    print(f'Part One: {day.part_two()}')

main()