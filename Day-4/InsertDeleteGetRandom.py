class RandomizedSet:

    def __init__(self):
        self.random_set = []

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set.append(val)
            return True
        return False
        
        
    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        return False
    
        
    def getRandom(self) -> int:
        return random.choice(self.random_set)
