"""by using the sort function
li=[1,10,2,6,5,3]
li.sort()
s=li[-1]*li[-2]
print(s)"""
"""with out using sort function"""
li=[1,10,2,6,5,3]
print("the original list:",li)
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i]>=li[j]:
            li[i],li[j]=li[j],li[i]
print("SORTED LIST:",li)
l1=li[-1]*li[-2]
print("the two maximum product in a list:",l1)
