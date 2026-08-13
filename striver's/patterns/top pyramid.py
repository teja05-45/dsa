# n=5

# #for spaces

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     #for stars
#     for k in range(i+1):
#         print("*", end=" ")
#     print()

n = 5

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")

    print()


    #optimised code
    n = 5

# Top half (Pyramid)
for i in range(n):
    spaces = "  " * (n - i - 1)
    stars = "* " * (2 * i + 1)
    print(spaces + stars)

