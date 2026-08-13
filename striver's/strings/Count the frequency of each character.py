s = "apple"
freq = {}

for ch in s.lower():
    if ch.isalpha():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print(freq)