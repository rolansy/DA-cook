import pandas as pd
from math import sqrt as m
import random
import matplotlib.pyplot as plt

k=int(input("Enter Numbernof  cluster : "))
df=pd.read_csv("kmeans.csv")

a=list(df.height)
b=list(df.weight)

x1=a[0]
x2=b[0]
cd={}

centroids=random.sample(list(zip(a,b)),k)

cd={i: [centroids[i]] for i in range(k)}

for i in range(len(a)):
    x2=a[i]
    y2=b[i]
    
    distances=[m((x2-x1)**2+(y2-y1)**2) for x1,y1 in centroids]
    
    min_d=distances.index(min(distances))
    
    centroid_x,centroid_y=centroids[min_d]
    updated_centroid_x=(centroid_x+x2)/2
    updated_centroid_y=(centroid_y+y2)/2
    centroids[min_d]=(updated_centroid_x,updated_centroid_y)
    
    if distances[min_d]!=0:
        if (x2,y2) not in cd[min_d]:
            cd[min_d].append((x2,y2))

for i in range(k):
    print(f"Cluster {i+1} : {cd[i]}")
for i in range(k):
    x,y=zip(*cd[i])
    plt.scatter(x,y)

centroids_x,centroids_y=zip(*centroids)
plt.scatter(centroids_x,centroids_y,marker="*")

plt.show()