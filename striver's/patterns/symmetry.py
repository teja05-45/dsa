n = 5

# Top Half
for i in range(n):
    # Left stars
    for j in range(n - i):
        print("*", end=" ")
    # Middle spaces
    for j in range(2 * i):
        print(" ", end=" ")
    # Right stars
    for j in range(n - i):
        print("*", end=" ")
    print()

# Bottom Half
for i in range(n):
    # Left stars
    for j in range(i + 1):
        print("*", end=" ")
    # Middle spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    # Right stars
    for j in range(i + 1):
        print("*", end=" ")
    print()


print("\n")
n = 5

# Top Half
for i in range(n):
    stars = "* " * (n - i)
    spaces = "  " * (2 * i)
    print(stars + spaces + stars)

# Bottom Half
for i in range(n):
    stars = "* " * (i + 1)
    spaces = "  " * (2 * (n - i - 1))
    print(stars + spaces + stars)