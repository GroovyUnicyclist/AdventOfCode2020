from day import Day
class Day6(Day):
    def part_one(self):
        input = open(self.input, "r")
        lines = input.readlines()
        count = 0
        total = 0
        previous_len = 0
        answers = set()
        for line in lines:
            for char in line.rstrip():
                answers.add(char)
                if len(answers) != previous_len:
                    count = count + 1
                previous_len = len(answers)
            if len(line.rstrip()) == 0:
                total = total + count
                count = 0
                previous_len = 0
                answers.clear()
        if count > 0:
            total = total + count
        return total

    def part_two(self):
        input = open(self.input, "r")
        lines = input.readlines()
        total = 0
        answers = []
        for line in lines:
            if len(line.rstrip()) != 0:
                answers.append(set())
                for char in line.rstrip():
                    answers[len(answers)-1].add(char)
            else:
                total = total + self.count_union(answers)
                answers = []
        if len(answers) > 0:
            total = total + self.count_union(answers)
        return total

    def count_union(self, set_list):
        final_set = set_list[0]
        first = True
        for answer_set in set_list:
            if not first:
                first = False
            else:
                final_set = final_set.intersection(answer_set)
        return len(final_set)