import random
class RandomizedCollection:

    def __init__(self):
        self.random_dict = defaultdict(int)
        self.lst = []
        

    def insert(self, val: int) -> bool:
        self.random_dict[val] += 1
        self.lst.append(val)
        return self.random_dict[val] == 1
        

    def remove(self, val: int) -> bool:
        if not self.random_dict[val]: 
            return False
        else:
            self.random_dict[val] -= 1
            self.lst.remove(val)
            return True
             

    def getRandom(self) -> int:
         return random.choice(self.lst)
