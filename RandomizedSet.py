class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.hashmap = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap.keys():
            return False
        self.list.append(val)
        self.hashmap[val] = len(self.list) - 1
        return self.list[len(self.list) - 1] == val
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            # replace the item to be removed with the item at the end of the list 
            self.hashmap[self.list[-1]] = self.hashmap[val]
            self.list[self.hashmap.pop(val)] = self.list[-1]
            self.list.pop()
            return True
        else:
            return False
        
        """
        if val not in self.hashmap.keys():
            return False
        index = self.hashmap[val]
        self.list[index] = None
        self.hashmap.pop(val)
        return True
        """

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.list)
        #return self.list[random.choice(self.hashmap.values())]
