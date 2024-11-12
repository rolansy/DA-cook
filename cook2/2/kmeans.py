import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
import random

k=int(input("Enter Number of clusters : "))
df=pd.read_csv('kmeans.csv')

a=list(df.height)
b=list(df.weight)

cd={}

data_points=[]
for i in range(len(a)):
    data_points.append((a[i],b[i]))
centroids=random.sample(data_points,k)

for i in range(k):
    cd[i]=centroids[i]
    
for i in range(len(a)):
    x2=a[i]
    y2=b[i]
    
    distances=[]
    for x1,y1 in centroids:
        distance=sqrt(((x2-x1)**2)+((y2-y1)**2))
        distances.append(distance)
    min_d=distances.index(min(distances))
    
    centroid_x,centroid_y=centroids[min_d]
    x_updated=(centroid_x+x2)/2
    y_updated=(centroid_y+y2)/2
    centroids[min_d]=x_updated,y_updated
    
    if distances[min_d]!=0:
        if (x2,y2) not in cd[min_d]:
            cd[min_d].append((x2,y2))
    
for i in range(k):
    print(f"cluster {i+1} : {cd[i]}")
    
for i in range(k):
    
    x=[]
    y=[]
    xc=[]
    yc=[]
    for point in cd[i]:
        x.append(point[0])
        y.append(point[1])
    for c in centroids[i]:
        xc.append(point[0])
        yc.append(point[1])
    plt.scatter(x,y)
    plt.scatter(xc,yc,marker='*',color='r')
plt.show()
        
    