n=int(input("Enter Number of ELements  : "))
l=[]
d={}
for i in range(n):
    x=int(input(f"Enter element {i+1} : "))
    l.append(x)
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
    
print(f"Mean : {sum(l)/n}")

mkx=mxx=0
for k,v in d.items():
    if v>mxx:
        mxx=v
        mkx=k
l.sort()
print(f"Sorted : {l}")
print("Median : ")
if n%2==0:
    print("Median : ",(l[n//2-1]+l[n//2])/2)
else:
    print("Median : ",l[n//2])
print("Mode : ")
for k,v in d.items():
    if v==mxx:
        print(k,end=", ")
print()


    
