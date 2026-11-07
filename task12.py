# Task 12 - Reversible Range
class ReversibleRange:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("step cannot be zero")
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        x = self.start
        while (self.step > 0 and x < self.stop) or (self.step < 0 and x > self.stop):
            yield x
            x += self.step

    def __len__(self):
        count = 0
        for x in self:                       # count without making a list
            count += 1
        return count

    def __reversed__(self):
        for i in range(len(self) - 1, -1, -1):
            yield self.start + i * self.step

    def __contains__(self, value):
        for x in self:
            if x == value:
                return True
        return False

r = ReversibleRange(2, 11, 3)
print(list(r), list(reversed(r)), len(r), 5 in r)    # [2, 5, 8] [8, 5, 2] 3 True
print(list(ReversibleRange(10, 0, -3)))              # [10, 7, 4, 1]
