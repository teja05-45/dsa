def find_sum(i, total):
    if i < 1:
        return total

    total += i
    return find_sum(i - 1, total)

n = int(input("Enter n: "))
print(find_sum(n, 0))