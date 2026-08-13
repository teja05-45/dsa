s = "aaabbacccc"
prev = s[0]
count = 1
result = ""

for i in range(1, len(s)):
    if s[i] == prev:
        count += 1
    else:
        result += prev + str(count)
        prev = s[i]
        count = 1

result += prev + str(count)

print(result)
