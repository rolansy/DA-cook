import pandas as pd
import numpy as np
df=pd.read_csv("corr_nom.csv")
from scipy.stats import chi2_contingency

contingency_table=pd.crosstab(df['a'],df['b'])

print(contingency_table)

chi2,p,dof,expected=chi2_contingency(contingency_table)

print(f"Chi2 stat : {chi2}]\np val : {p}]\ndof : {dof}\nexpected : {expected}")

contingency_table_values=contingency_table.values
print(contingency_table_values)
n=np.sum(contingency_table_values)
k=min(contingency_table_values.shape)-1
print(contingency_table_values.shape)
print(n)
crr=np.sqrt(chi2/(n*k))
print("Correlation : ",crr)

alpha=0.05
if p<alpha:
    print("There IS significatn asso bw a nd b")
else:
    print("No SIGNINFACT ASSO BW A ND B")