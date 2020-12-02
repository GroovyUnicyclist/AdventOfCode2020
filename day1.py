from day import Day
class Day1(Day):
    def part_one(self):
        input = open(self.input).read().splitlines()
        for i in range(len(input) - 1):
            for j in range(i + 1, len(input)):
                if i!=j and int(input[i]) + int(input[j]) == 2020:
                    return int(input[i])*int(input[j])

    def part_two(self):
        input = open(self.input).read().splitlines()
        for i in range(len(input) - 2):
            for j in range(i + 1, len(input) - 1):
                for k in range(j + 1, len(input)):
                    if i!=j and i!=k and j!=k and int(input[i]) + int(input[j]) + int(input[k]) == 2020:
                        return int(input[i])*int(input[j])*int(input[k])