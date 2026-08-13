# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


for n in [2,3,5]:
    print(f"pattern for {n}")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()