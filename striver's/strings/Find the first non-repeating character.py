def get_first_unique():
    s = "apple"
    freq = {}
    for ch in s.lower():
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
    for ch in freq:
        if freq[ch] == 1:
            return ch

print(get_first_unique()) 