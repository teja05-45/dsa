s="the sky is blue"

words=s.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)



# s = "learning Python is fun"

# # Finds the item with the maximum length in the split list
# longest = max(s.split(), key=len)

# print(longest)  # Outputs: learning