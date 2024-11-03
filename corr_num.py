import pandas as pd
df=pd.read_csv("corr_numeric.csv")
am=df.a.mean()
bm=df.b.mean()
n=len(df)
s=0
for i in range(n):
    s+=(df.a[i]-am)*(df.b[i]-bm)
    
asd=df.a.std()
bsd=df.b.std()
corr=s/(asd*bsd*n)
print(f"Correlation Coefficient : {corr}")
cov=corr*asd*bsd
print(f"Covariance : {cov}")

print("Using func")

corr=df.a.corr(df.b)
print(f"COrr : {corr}")
cov=df.cov().loc['a','b']
print("Covaruacne : ",cov)
