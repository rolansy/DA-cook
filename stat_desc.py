import pandas as pd
import numpy as np
df=pd.read_csv('statdata.csv')
l=list(df.data)
d={}
n=len(l)
for x in l:
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
if n%2==0:
    median=(l[n//2-1]+l[n//2])/2
else:
    median=l[n//2]
print("Median : ",median)
print("Mode : ",end="")
for k,v in d.items():
    if v==mxx:
        print(k,end=", ")
print()

print("Quartiles : ")
print("Q0 : ",l[0])
q1=l[n//4]
q2=median
q3=l[(3*n)//4]
q4=l[n-1]
print(f"Q1 : {q1}")
print(f"Q2 : {q2}")
print(f"Q3 : {q3}")
print(f"Q4 : {q4}")
iqr=q3-q1
print(f"IQR : {iqr}")
ho=q3+(1.5*iqr)
lo=q1-(1.5*iqr)
print(f"HO : {ho}\nLO : {lo}")
print("Low Outliers : ",end="")
p=0
out=[]
for i in range(n//4):
    if l[i]<lo:
        p+=1
        out.append(l[i])
        print(l[i],end= ' ')
        
    else:
        if p==0:
            print("None")
        break
print()
p=0
print("Higher Outliers  : ",end="")
for i in range(n-1,(n*3)//4,-1):
    if l[i]>ho:
        out.append(l[i])
        p+=1
        print(l[i],end=" ")
    else:
        if p==0:
            print("None")
        break
print(l)
while out:
    l.remove(out.pop())
print(f"AFter removing outliers : \n {l}")

d={}
n=len(l)
for x in l:
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
if n%2==0:
    median=(l[n//2-1]+l[n//2])/2
else:
    median=l[n//2]
print("Median : ",median)

md=0
mod={1:"uni",2:"bi",3:"tri"}
print("Mode : ",end="")
for k,v in d.items():
    if v==mxx:
        md+=1
        print(k,end=", ")
print(f"The data has {mod[md]}mod")

print("Variance : ",np.var(l))
print("Standard Deviation  : ",np.var(l)**(1/2))

print("Quartiles : ")
print("Q0 : ",l[0])
q1=l[n//4]
q2=median
q3=l[(3*n)//4]
q4=l[n-1]
print(f"Q1 : {q1}")
print(f"Q2 : {q2}")
print(f"Q3 : {q3}")
print(f"Q4 : {q4}")
iqr=q3-q1
print(f"IQR : {iqr}")
ho=q3+(1.5*iqr)
lo=q1-(1.5*iqr)
print(f"HO : {ho}\nLO : {lo}")
print("Low Outliers : ",end="")
p=0
out=[]
for i in range(n//4):
    if l[i]<lo:
        p+=1
        out.append(l[i])
        print(l[i],end= ' ')
        
    else:
        if p==0:
            print("None")
        break
print()
p=0
print("Higher Outliers  : ",end="")
for i in range(n-1,(n*3)//4,-1):
    if l[i]>ho:
        out.append(l[i])
        p+=1
        print(l[i],end=" ")
    else:
        if p==0:
            print("None")
        break
    
