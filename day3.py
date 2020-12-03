from day import Day
class Day3(Day):
    def part_one(self):
        input = open(self.input, "r")
        lines = input.readlines()
        input.close()
        x = 0
        count = 0
        for line in lines:
            if line[x] == '#':
                count = count + 1
            x = x + 3
            if x >= len(line) - 1:
                x = x%(len(line) - 1)
        return count

    def part_two(self):
        input = open(self.input, "r")
        lines = input.readlines()
        input.close()
        return self.find_trees(lines, 1, 1) * self.find_trees(lines, 3, 1) * self.find_trees(lines, 5, 1) * self.find_trees(lines, 7, 1) * self.find_trees(lines, 1, 2)

    def find_trees(self, lines, right, down):
        x = 0
        count = 0
        for i in range(0, len(lines), down):
            if lines[i][x] == '#':
                count = count + 1
            x = x + right
            if x >= len(lines[i]) - 1:
                x = x%(len(lines[i]) - 1)
        return count