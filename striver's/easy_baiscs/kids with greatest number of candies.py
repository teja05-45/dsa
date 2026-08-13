candies=[2,3,5,1,3]
extra_candies=3
ans=[]
maximum=max(candies)
for i in range(len(candies)):
    total_candies=candies[i]+extra_candies
    if total_candies<maximum:
        ans.append(False)
    else:
        ans.append(True)
print(ans)