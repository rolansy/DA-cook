import pandas as pd
from math import sqrt
import random

k=int(input("Enter Number of clusters : "))
df=pd.read_csv('kmeans.csv')

a=list(df.height)
b=list(df.weight)



x1=a[0]
y1=b[0]
cd={}

data_points=[]
for i in range(len(a)):
    data_points.append((a[i],b[i]))
centroids=random.sample(data_points,k)

for i in range(k):
    cd[i]=[centroids[i]]

for i in range(len(a)):
    x2=a[i]
    y2=b[i]
    
    distances=[]
    for x1, y1 in centroids:
        distance=sqrt(((x2-x1)**2)+((y2-y1)**2))
        distances.append(distance)
    min_d=distances.index(min(distances))
    
    centroid_x,centroid_y=centroids[min_d]
    updated_x=(centroid_x+x2)/2
    updated_y=(centroid_y+y2)/2
    
    centroids[min_d]=updated_x,updated_y
    
    if distances[min_d]!=0:
        if(x2,y2) not in cd[min_d]:
            cd[min_d].append((x2,y2))
            
for i in range(k):
    print(f"Cluster {i+1} : {cd[i]}")
    
import matplotlib.pyplot as plt

for i in range(k):
    x=[]
    y=[]
    xc=[]
    yc=[]
    for point in cd[i]:
        x.append(point[0])
        y.append(point[1])
    for centroid in centroids:
        xc.append(centroid[0])
        yc.append(centroid[1])
    plt.scatter(x,y)
    plt.scatter(xc,yc,marker='*',color='r')
    


plt.show()