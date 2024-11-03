file='naive_bayes.csv'

def read_csv(filen):
    data=[]
    with open(filen,'r') as f:
        next(f)
        for line in f:
            row=line.strip().split(',')
            features=row[1:-1]
            label=row[-1]
            data.append((features,label))
    return data
training_data=read_csv(file)
print(training_data)

def calculate_priors(data):
    total_samples=len(data)
    class_counts={}
    
    for feature,label in data:
        if label not in class_counts:
            class_counts[label]=0
        class_counts[label]+=1
    
    priors={}
    for label in class_counts:
        priors[label]=class_counts[label]/total_samples
    return priors

print(calculate_priors(training_data))
            
def calculate_likelihoods(data):
    feature_counts={}
    class_counts={}
    
    for features,label in data:
        if label not in class_counts:
            class_counts[label]=0
            feature_counts[label]=[{} for i in range(len(features))]
        class_counts[label]+=1
        for i in range(len(features)):
            if features[i] not in feature_counts[label][i]:
                feature_counts[label][i][features[i]]=0
            feature_counts[label][i][features[i]]+=1
    print("\n",feature_counts,"\n")
    likelihoods={}
    for label in feature_counts:
        likelihoods[label]=[]
        for i in range(len(feature_counts[label])):
            likelihoods[label].append({key: feature_counts[label][i][key]/class_counts[label] for key in feature_counts[label][i]})
    return likelihoods

def classify(priors,likelihoods, new_data):
    posteriors={}
    for label in priors:
        posteriors[label]=priors[label]
        for i in range(len(new_data)):
            if new_data[i] in likelihoods[label][i]:
                posteriors[label]*=likelihoods[label][i][new_data[i]]
            else:
                posteriors[label]*=0
    for label in posteriors:
        print(f"Posterior Probability for \"{label}\" = {posteriors[label]}")

    return max(posteriors, key=posteriors.get)

def naive_bayes_classifier(training_data,new_data):
    priors=calculate_priors(training_data)
    likelihoods=calculate_likelihoods(training_data)
    return classify(priors,likelihoods,new_data)
    
print()
print(calculate_likelihoods(training_data))
new_data=['youth','high','yes','excellent']
predicted_class=naive_bayes_classifier(training_data,new_data)
print(f"Predicted class for {new_data} : {predicted_class} ")