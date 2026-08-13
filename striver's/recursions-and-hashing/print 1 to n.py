def print_numbers(i,n):
    if i > n:          # Base condition
        return

    print(i)
    print_numbers(i + 1, n)#function calling itself

n=int(input("Enter n: "))
print_numbers(1, n)