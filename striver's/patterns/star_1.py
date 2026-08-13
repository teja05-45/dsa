# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()

# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print().

for n in [2,3,5]:
    print(f"pattern for {n}")

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()