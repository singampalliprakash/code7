input=list(map(int,input("enter list here:").split()))
chr=[]
zeros=0
for q in input:
    if (q!=0):
        chr.append(q)
    else:
        zeros+=1
arr= chr + [0]*zeros

print(arr)