class MyHashSet(object):

    def __init__(self):
        self.hash=[False]*1000001
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash[key]=True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash[key]=False
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hash[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
obj=MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(2))
obj.remove(1)
print(obj.contains(1))  