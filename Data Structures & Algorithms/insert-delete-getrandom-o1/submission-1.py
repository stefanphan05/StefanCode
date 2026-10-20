class RandomizedSet:

    def __init__(self):
        self.my_list = []
        self.my_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.my_map:
            self.my_map[val] = len(self.my_list)
            self.my_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.my_map:
            return False
        
        index = self.my_map[val]
        last_value = self.my_list[-1]
        self.my_list[index], self.my_list[-1] = self.my_list[-1], self.my_list[index]
        self.my_list.pop()
        # Update the value
        self.my_map[last_value] = index
        del self.my_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()