from day import Day
import bisect

class Day5(Day):
    # Runs in O(n)
    def part_one(self):
        input = open(self.input).read().splitlines()
        highest_id = 0
        for line in input:
            value = self.parse_input(line)
            seat = self.get_seat(value)
            seat_id = seat[0]*8 + seat[1]
            if (seat_id > highest_id):
                highest_id = seat_id
        return highest_id

    # Runs in O(n + log(n))
    def part_two(self):
        input = open(self.input).read().splitlines()
        seat_ids = []
        for line in input:
            value = self.parse_input(line)
            seat = self.get_seat(value)
            seat_id = seat[0]*8 + seat[1]
            # Sorted insert runs in O(log(n))
            bisect.insort(seat_ids, seat_id)
            
        previous_id = seat_ids[0]
        # Search sorted set for correct id runs in O(n)
        for seat_id in seat_ids:
            if seat_id - previous_id > 1:
                return previous_id + 1
            previous_id = seat_id
        return -1

    # Turns string into a binary value
    def parse_input(self, input):
        output = 0
        for char in input[:10]:
            output = output << 1
            if char == 'F' or char == 'L':
                output = output + 1
        return output
    
    # Does a binary search algorithm based on each bit of the value passed
    def get_seat(self, value):
        high = 127
        low = 0
        for i in range(7):
            mid = int(low + (high - low)/2)
            if 1 & value >> (9 - i) == 1:
                high = mid
            else:
                low = mid + 1
        out1 = high
        high = 7
        low = 0
        for i in range(7, 10):
            mid = int(low + (high - low)/2)
            if 1 & value >> (9 - i) == 1:
                high = mid
            else:
                low = mid + 1
        out2 = high
        return (out1, out2)
            