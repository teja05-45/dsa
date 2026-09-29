class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1


# Create HashMap
obj = MyHashMap()

# Add key-value pairs
obj.put(1, 2)
obj.put(2, 5)

# Get values
print(obj.get(1))  # 2
print(obj.get(2))  # 5
print(obj.get(3))  # -1

# Update existing key
obj.put(1, 10)
print(obj.get(1))  # 10

# Remove
obj.remove(1)
print(obj.get(1))  # -1