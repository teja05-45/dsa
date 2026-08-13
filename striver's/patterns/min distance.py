n = 4

size = 2 * n - 1

for i in range(size):
    for j in range(size):

        top = i
        left = j
        right = size - 1 - j
        bottom = size - 1 - i

        minimum = min(top, left, right, bottom)

        print(n - minimum, end=" ")

    print()