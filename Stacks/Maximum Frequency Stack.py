class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxcount = 0
        self.stacks = {}

    def push(self, val) -> None:
        val_count = 1 + self.count.get(val, 0)
        self.count[val] = val_count

        if val_count > self.maxcount:
            self.maxcount = val_count
            self.stacks[val_count] = []

        self.stacks[val_count].append(val)

    def pop(self) -> int:
        result = self.stacks[self.maxcount].pop()
        self.count[result] -= 1

        if not self.stacks[self.maxcount]:
            self.maxcount -= 1

        return result