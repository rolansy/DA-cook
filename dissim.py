import pandas as pd
df=pd.read_csv("dissdata.csv")
cols=len(df.columns)
rows=len(df)

numatt=df.select_dtypes(include=['number']).columns.tolist()
nomatt=df.select_dtypes(exclude=['number']).columns.tolist()

print("Number of attributes : ",cols)
print("NUmber of instances  : ",rows)
print(f"Nominal attributes : {nomatt}")
print(f"Numerical Attributes : {numatt}")

df[numatt]=(df[numatt]-df[numatt].min())/(df[numatt].max()-df[numatt].min())
print(f"Normalised data : \n {df}")

numdf=df.select_dtypes(include=['number'])
print(numdf)

numr=numdf.shape[0]
diss_mat=[ [0.0 for i in range(numr)] for i in range (numr)]

print(pd.DataFrame(diss_mat))

for i in range(numr):
    for j in range(numr):
        if i>=j:
            diss_mat[i][j]=round(sum([abs(numdf.iloc[i,k]-numdf.iloc[j,k]) for k in range(len(numdf.columns))]),2)
        else:
            diss_mat[i][j]=0
    
print("Dissimilarity Matrix for num att : ")
print(pd.DataFrame(diss_mat))

nomdf=df.select_dtypes(exclude=['number'])
nomr=nomdf.shape[0]

diss_mat=[[0.0 for i in range(nomr)] for i in range (nomr)]

for i in range(nomr):
    for j in range(nomr):
        if i>j:
            diss_mat[i][j]=round(sum([1 if nomdf.iloc[i,k]!=nomdf.iloc[j,k] else 0 for k in range (len(nomdf.columns))]),2)
        else:
            diss_mat[i][j]=0
            
print("Diss Mat for nom att : ")
print(pd.DataFrame(diss_mat))

mixdf=df
mixr=df.shape[0]
diss_mat=[[0.0 for i in range (mixr)] for i in range(mixr)]
for i in range(mixr):
    for j in range(mixr):
        if i>j:
            dissim=0
            for col in mixdf.columns.tolist():
                if mixdf[col].dtype=='object':
                    dissim+= 1 if mixdf[col][i]!=mixdf[col][j] else 0
                else:
                    dissim+=abs(mixdf[col][i]-mixdf[col][j])            
            diss_mat[i][j]=round(dissim/cols,2)
        else:
            diss_mat[i][j]=0

print("Dissimilartiy of mixed attr : ")
print(pd.DataFrame(diss_mat))