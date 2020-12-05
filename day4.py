from day import Day
import re
class Day4(Day):
    def part_one(self):
        required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        input = open(self.input, "r")
        lines = input.readlines()
        count = 0
        fields = set()
        for line in lines:
            elements = line.split()
            for element in elements:
                if element[:3] in required_fields:
                    fields.add(element[:3])
            if len(elements) == 0:
                if (fields == required_fields):
                    count = count + 1
                fields.clear()
        if (fields == required_fields):
            count = count + 1
        return count
        

    def part_two(self):
        required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        input = open(self.input, "r")
        lines = input.readlines()
        count = 0
        fields = set()
        valid = True
        for line in lines:
            elements = line.split()
            for element in elements:
                if element[:3] in required_fields and valid:
                    valid = self.validate(element[:3], element[4:])
                    fields.add(element[:3])
            if len(elements) == 0:
                if (fields == required_fields and valid):
                    count = count + 1
                fields.clear()
                valid = True
        if (fields == required_fields and valid):
            count = count + 1
        return count

    def validate(self, key, value):
        valid = False
        if key == 'byr':
            valid = len(value) == 4 and 1920 <= int(value) <= 2002
        elif key == 'iyr':
            valid = len(value) == 4 and 2010 <= int(value) <= 2020
        elif key == 'eyr':
            valid = len(value) == 4 and 2020 <= int(value) <= 2030
        elif key == 'hgt':
            match = re.match(r'\d+', value)
            if match is not None and value[len(match.group()):] == 'cm':
                valid = 150 <= int(match.group()) <= 193
            elif match is not None and value[len(match.group()):] == 'in':
                valid = 59 <= int(match.group()) <= 76
        elif key == 'hcl':
            valid = re.match(r'^#[\da-f]{6}$', value) is not None
        elif key == 'ecl':
            valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            valid = re.match(r'^\d{9}$', value) is not None
        return valid