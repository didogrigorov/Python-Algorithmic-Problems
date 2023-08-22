from random import choice


class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        res = val in self.num_map
        if not res:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            idx = self.num_map[val]
            last_val = self.num_list[-1]
            self.num_list[idx] = last_val
            self.num_list.pop()
            self.num_map[last_val] = idx
            del self.num_map[val]
        return res

    def getRandom(self) -> int:
        return choice(self.num_list)