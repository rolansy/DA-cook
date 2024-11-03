import pandas as pd
from itertools import combinations

def load(fpath):
    df=pd.read_csv(fpath,header=None)
    transactions=df.apply(lambda x: x.dropna().tolist(),axis=1).tolist()
    return transactions

def create_candidates(frequent_itemsets,length):
    return set(frozenset(item1.union(item2)) for item1,item2 in combinations(frequent_itemsets,2) if len(item1.union(item2))==length)

def get_frequent_itemsets(dataset,min_sup):
    item_count={}
    num_transactions=len(dataset)
    
    for transaction in dataset:
        for item in transaction:
            itemset=frozenset([item])
            item_count[itemset]=item_count.get(itemset,0)+1
        
    frequent_itemsets={itemset:count for itemset,count in item_count.items() if count/num_transactions>=min_sup}
    all_frequent_itemsets=frequent_itemsets.copy()
    length=2
    
    while frequent_itemsets:
        candidates=create_candidates(frequent_itemsets.keys(),length)
        item_count={}
        
        for transaction in dataset:
            transaction_set=set(transaction)
            for candidate in candidates:
                if candidate.issubset(transaction_set):
                    item_count[candidate]=item_count.get(candidate,0)+1
        
        frequent_itemsets={itemset:count for itemset,count in item_count.items() if count/num_transactions>=min_sup}
        
        all_frequent_itemsets.update(frequent_itemsets)
        length+=1
    return all_frequent_itemsets

def generate_asso_rules(frequent_itemsets,min_conf):
    rules=[]
    num_transactions=sum(frequent_itemsets.values())
    for itemset,support in frequent_itemsets.items():
        for antecedent in map(frozenset,combinations(itemset,len(itemset)-1)):
            consequent=itemset-antecedent
            if consequent:
                antecedent_support=frequent_itemsets.get(antecedent,0)
                if antecedent_support>0:
                    confidence=support/antecedent_support
                    if confidence>min_conf:
                        rules.append((antecedent,consequent,confidence))
    return rules

p='ap.csv'
q='Apriori.csv'
print(load(q))
min_sup=0.2
min_conf=0.6

dataset=load(q)

frequent_itemsets=get_frequent_itemsets(dataset,min_sup)
print("Frequent Itemsets : ")
for itemset,count in frequent_itemsets.items():
    print(f"{set(itemset)}: {count}")
    
    

rules=generate_asso_rules(frequent_itemsets,min_conf)

print("Asso Rules : ")
for antecedent,consequent,confidence in rules : 
    print(f"{set(antecedent)}=>{set(consequent)}, confidence : {confidence}")


