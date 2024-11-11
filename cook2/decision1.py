import csv
import math

def load_data(filename):
    data=[]
    with open(filename,'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            # print(row)
            data.append(row)
    return data

def entropy(data):
    total=len(data)
    # print(total)
    if total==0:
        return 0
    count_yes=0
    for row in data:
        if row['class_buys_computer']=='yes':
            count_yes+=1
    count_no=total-count_yes
    # print(count_yes)
    # print(count_no)
    p_yes=count_yes/total
    p_no=count_no/total
    if p_yes>0:
        entropy_yes=-p_yes*math.log2(p_yes)
    else:
        entropy_yes=0
    if p_no>0:
        entropy_no=-p_no*math.log2(p_no)
    else:
        entropy_no=0
    # print(entropy_yes+entropy_no)
    return entropy_yes+entropy_no

def information_gain(data,attribute):
    total_entropy=entropy(data)
    values=set()
    for row in data:
        values.add(row[attribute])
    weighted_entropy=0
    for value in values:
        subset=[]
        for row in data:
            if row[attribute]==value:
                subset.append(row)
        weighted_entropy+=(len(subset)/len(data))*entropy(subset)
    print(total_entropy-weighted_entropy)
    return total_entropy-weighted_entropy


def split_data(data,attribute,value):
    result=[]
    for row in data:
        if row[attribute]==value:
            result.append(row)
    return result

def build_tree(data,attributes):
    if  all(row['class_buys_computer']=='yes' for row in data):
        return 'yes'
    all_no=True
    for row in data:
        if row['class_buys_computer']!='no':
            all_no=False
            break
    if all_no:
        return 'no'
    
    if not attributes:
        count_yes=0
        
        for row in data:
            if row['class_buys_computer']=='yes':
                count_yes+=1
        if count_yes>=len(data)/2:
            return 'yes'
        else:
            return 'no'
    
    best_attribute=None
    max_info_gain=-float('inf')
    
    for attr in attributes:
        info_gain=information_gain(data,attr)
        if info_gain>max_info_gain:
            max_info_gain=info_gain
            best_attribute=attr
    
    tree={best_attribute:{}}
    values=set()
    for row in data:
        
        value=row[best_attribute]
        values.add(value)
    for value in values:
        subset=split_data(data,best_attribute,value)
        remaining_attributes=[]
        for attr in attributes:
            if attr!=best_attribute:
                remaining_attributes.append(attr)
        
        subtree=build_tree(subset,remaining_attributes)
        tree[best_attribute][value]=subtree
    print(tree)
    return tree

def display_tree(tree,indent=''):
    if isinstance(tree,dict):
        for key,value in tree.items():
            print(f'{indent}{key}')
            for subkey,subvalue in value.items():
                if isinstance(subvalue,dict):
                    print(f'{indent} {subkey} ->')
                    display_tree(subvalue,indent+'    ')
                else:
                    print(f"{indent}  {subkey} -> {subvalue}")
    else:
        if tree=='yes':
            print(f"{indent}Predict : Yes")
        else:
            print(f"{indent}Predict : No")
        
def predict(tree,instance):
    if not isinstance(tree,dict):
        return tree
    attribute=next(iter(tree))
    value=instance[attribute]
    subtree=tree[attribute].get(value,'no')
    return predict(subtree,instance)

def predict(tree,instance):
    if not isinstance(tree,dict):
        return tree
    attribute=next(iter(iter))
    value=instance[attribute]
    subtree=tree[attribute].get(value,'no')
    return predict(subtree,instance)
    
             
        
    
        


def get_user_input():
    
    age = input("Enter age (youth/middle_aged/senior): ")
    income = input("Enter income (high/medium/low): ")
    student = input("Are you a student? (yes/no): ")
    credit_rating = input("Enter credit rating (fair/excellent): ")
    return {'age':age,'income':income,'student':student,'credit_rating':credit_rating}

filename='decision_tree.csv'
data=load_data(filename)
attributes=['age','income','student','credit_rating']
# tree=build_tree(data,attributes)
# display_tree(tree)
instance=get_user_input()
# prediction=predict(tree,instance)

entropy(data)
information_gain(data,'age')
tree=build_tree(data,attributes)
display_tree(tree)
prediction=predict(tree,instance)
print(f"Prediction for class_buys_computer: {prediction}")
