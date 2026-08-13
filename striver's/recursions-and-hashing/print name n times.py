def print_name(i, n):
    if i > n:          # Base condition
        return

    print("Teja")
    print_name(i + 1, n)#function calling itself

n = int(input("Enter n: "))
print_name(1, n)