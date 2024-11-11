import pandas as pd
from itertools import combinations

def loadcsv(filepath):
    df=pd.read_csv(filepath,header=None)
    transactions=[]
    for index,row in df.iterrows():
        cleaned_row=row.dropna()
        
        transaction=cleaned_row.tolist()
        transactions.append(transaction)
    return transactions

def create_candidates(frequent_itemsets,length):
    combined_itemsets=set()
    for item1,item2 in combinations(frequent_itemsets,2):
        combined_itemset=item1.union(item2)
        
        if len(combined_itemset)==length:
            combined_itemsets.add(frozenset(combined_itemset))
    return combined_itemsets

def get_frequent_itemsets(dataset,min_support):
    item_count={}
    num_transactions=len(dataset)
    for transaction in dataset:
        for item in transaction:
            itemset=frozenset([item])
            item_count[itemset]=item_count.get(itemset,0)+1
    
    frequent_itemsets={}
    for itemset,count in item_count.items():
        support=count/num_transactions
        if support>=min_support:
            frequent_itemsets[itemset]=count
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
        frequent_itemsets={}
        for itemset,count in item_count.items():
            support=count/num_transactions
            if support>=min_support:
                frequent_itemsets[itemset]=count
        all_frequent_itemsets.update(frequent_itemsets)
        length+=1
    return all_frequent_itemsets

def generate_association_rules(frequent_itemsets,min_confidence):
    rules=[]
    num_transactions=0
    for count in frequent_itemsets.values():
        num_transactions+=count
    for itemset,support in frequent_itemsets.items():
        for combination in combinations(itemset,len(itemset)-1):
            antecedent=frozenset(combination)
            consequent=itemset-antecedent
            if consequent:
                antecedent_support=frequent_itemsets.get(antecedent,0)
                if antecedent_support>0:
                    confidence=support/antecedent_support
                    if confidence>=min_confidence:
                        rules.append((antecedent,consequent,confidence))
    return rules

def genassrules(frequent_itemsets,min_confidence):
    rules=[]
    num_transactions=0
    for count in frequent_itemsets.values():
        num_transactions+=count
    for itemset,support in frequent_itemsets.items():
        for combination in combinations(itemset,len(itemset)-1):
            antecedent=frozenset(combination)
            consequent=itemset-antecedent
            if consequent:
                antecedent_support=frequent_itemsets.get(antecedent,0)
                if antecedent_support>0:
                    confidence=support/antecedent_support
                    if confidence>=min_confidence:
                        rules.append((antecedent,consequent,confidence))
    print(rules)
            


        

filepath='apriori.csv'
dataset=loadcsv(filepath)
print(f"dataset : {dataset}")
min_support=0.2
frequent_itemsets=get_frequent_itemsets(dataset,min_support)

print(f"\nFrequent itemsets : \n")

for itemset,count in frequent_itemsets.items():
    print(f"{set(itemset)} : {count}")
min_confidence=0.6
rules= generate_association_rules(frequent_itemsets,min_confidence)

print("\n Associartion rules : \n")
for antecedent,consequent,confidence in rules:
    print(f"{set(antecedent)}=>{set(consequent)}, confidence : {confidence:.2f}")



