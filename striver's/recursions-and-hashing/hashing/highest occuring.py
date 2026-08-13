from collections import Counter

s=input("enter the string:")

freq=Counter(s)

max_count=None
max_char=0

for ch,count in freq.items():
    if max_count is None or count>max_count:
        max_count=count
        max_char=ch

print(f"The highest occurring character is '{max_char}' with a frequency of {max_count}")