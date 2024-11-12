def read_csv(filepath):
    data=[]
    with open(filepath,'r') as file:
        next(file)
        for line in file:
            row=line.strip().split(',')
            features=row[1:-1]
            label=row[-1]
            data.append((features,label))
    return data

def calculate_prior_probabilities(data):
    total_samples=len(data)
    class_counts={}
    
    for features,label in data:
        if label not in class_counts:
            class_counts[label]=0
        class_counts[label]+=1
    priors={}
    for label in class_counts:
        priors[label]=class_counts[label]/total_samples
    return priors

def calculate_likelihoods(data):
    feature_counts={}
    class_counts={}
    
    for features,label in data:
        if label not in class_counts:
            class_counts[label]=0
            feature_list=[]
            for i in range(len(features)):
                feature_list.append({})
            feature_counts[label]=feature_list
        class_counts[label]+=1
        for i in range(len(features)):
            if features[i] not in feature_counts[label][i]:
                feature_counts[label][i][features[i]]=0
            feature_counts[label][i][features[i]]+=1
    likelihoods={}
    for label in feature_counts:
        likelihoods[label]=[]
        for i in range(len(feature_counts[label])):
            feature_likelihoods={}
            for key in feature_counts[label][i]:
                likelihood=feature_counts[label][i][key]/class_counts[label]
                feature_likelihoods[key]=likelihood
            likelihoods[label].append(feature_likelihoods)
    return likelihoods

def classify(priors,likelihoods,new_data):
    posteriors={}
    for label in priors:
        posteriors[label]=priors[label]
        for i in range(len(new_data)):
            if new_data[i] in likelihoods[label][i]:
                posteriors[label]*=likelihoods[label][i][new_data[i]]
            else:
                posteriors[label]*=0
    print("posteriors : ",posteriors)
    
    for label in posteriors:
        print(f"posterior probability for \"{label}\" ={posteriors[label]}")
        
    max_label=None
    max_posterior=-float('inf')
    for label,posterior in posteriors.items():
        if posterior>max_posterior:
            max_posterior=posterior
            max_label=label
    return max_label


filename='naive_bayes.csv'
data=read_csv(filename)
print(data)
print()
priors=calculate_prior_probabilities(data)
print("priors : ",priors)
print()
likelihoods=calculate_likelihoods(data)
print("likelihoods : ",likelihoods)
print()
new_sample=['senior','high','yes','fair']
print(f"\nPredicted CLass for {new_sample} : {classify(priors,likelihoods,new_sample)}")
                        