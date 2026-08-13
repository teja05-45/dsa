n=5 
for i in range(n):
    #for spaces
    for j in range(i):
        print(" ", end=" ")
    #for stars
    for k in range(2*(n-i)-1):
        print("*", end=" ")
    print()

#optimised code
# Bottom half (Inverted Pyramid)
for i in range(n - 2, -1, -1):
    spaces = "  " * (n - i - 1)
    stars = "* " * (2 * i + 1)
    print(spaces + stars)

