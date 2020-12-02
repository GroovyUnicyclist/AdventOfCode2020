from day import Day
import re

class Day2(Day):
    def part_one(self):
        input = open(self.input).read().splitlines()
        valid_count = 0
        for password in input:
            char_count = 0
            m = re.match(r"(\d+)-(\d+) (\w): (\w+)", password)
            groups = m.groups()
            for current_char in groups[3]:
                if current_char == groups[2]:
                    char_count = char_count + 1
            if int(groups[0]) <= char_count <= int(groups[1]):
                valid_count = valid_count + 1
        return valid_count

    def part_two(self):
        input = open(self.input).read().splitlines()
        valid_count = 0
        for password in input:
            char_count = 0
            m = re.match(r"(\d+)-(\d+) (\w): (\w+)", password)
            groups = m.groups()
            if groups[3][int(groups[0]) - 1] == groups[2]:
                char_count = char_count + 1
            if groups[3][int(groups[1]) - 1] == groups[2]:
                char_count = char_count + 1
            if char_count == 1:
                valid_count = valid_count + 1
        return valid_count