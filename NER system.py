
# coding: utf-8

# In[2]:

from sklearn.feature_extraction import DictVectorizer
from sklearn import svm


# **Reading train file**

# In[3]:

def readconll(file):
    lines = [line.strip() for line in open(file)]
    while lines[-1] == '':  # Remove trailing empty lines
        lines.pop()
    s = [x.split('_') for x in '_'.join(lines).split('__')]  # Quick split corpus into sentences
    return [[y.split() for y in x] for x in s]

sentences = readconll('eng.train')


# **Extracting features and classes and training classifier**

# In[4]:

#feature extraction function
def featurizer(sentences):
    features = []
    for sentence in sentences:
        token_count = 0
        for token in sentence:
            token_features = {}
            
            token_features['word#' + token[0]] = 1 #lexical identity
            
            token_features['pos#' + token[1]] = 1 #POS tag
            
            if token_count == 0: #first word of sentence/initial capitalization
                if token[0][0].isupper() == True:
                    token_features['firstword-initcaps#'] = 1
                else:
                    token_features['firstword-notinitcaps#'] = 1
            else:
                if token[0][0].isupper() == True:
                    token_features['initcaps#'] = 1
            
            if token[0].isupper() == True: #all caps
                token_features['allcaps#'] = 1
            
            if token[0][0].islower() == True and token[0].upper() != token[0]: #mixed caps
                token_features['mixedcaps#'] = 1
            
            if token_count > 0: #preceding token's lexical identity, POS tag and word shape
                token_features['preceding_word#' + sentence[token_count - 1][0]] = 1
                token_features['preceding_pos#' + sentence[token_count - 1][1]] = 1
                token_features['preceding_word_shape#' + ''.join(['x' if character.islower() == True else 'X' if character.isupper() == True else 'd' if character.isnumeric() == True else character for character in sentence[token_count-1][0]])] = 1
            
            if token_count < len(sentence) - 1: #succeeding token's lexical identity, POS tag and word shape
                token_features['succeeding_word#' + sentence[token_count + 1][0]] = 1
                token_features['succeeding_pos#' + sentence[token_count + 1][1]] = 1
                token_features['succeeding_word_shape#' + ''.join(['x' if character.islower() == True else 'X' if character.isupper() == True else 'd' if character.isnumeric() == True else character for character in sentence[token_count+1][0]])] = 1

            c = 1 #prefixes and suffixes up to four characters
            while c != len(token[0]) and c < 5:
                p = 'pre' + str(c) + '#'
                s = 'suff' + str(c) + '#'
                p = p + token[0][:c]
                s = s + token[0][c:]
                c += 1
                token_features[p] = 1
                token_features[s] = 1
            
            word_shape = ''.join(['x' if character.islower() == True else 'X' if character.isupper() == True else 'd' if character.isnumeric() == True else character for character in token[0]])
            token_features['word_shape#' + word_shape] = 1 #word shape
            
            features.append(token_features)
            token_count += 1
    return features

#vectorizing features
vectorizer = DictVectorizer(sparse = True)
x = vectorizer.fit_transform(featurizer(sentences))

#class extraction function
def classizer(sentences): 
    classes = []
    for sentence in sentences:
        for token in sentence:
            classes.append(token[3])
    return classes

y = classizer(sentences)

#training classifier
classifier = svm.LinearSVC()
classifier.fit(x,y)


# **Running classifier on test data**

# In[5]:

test_file = readconll('eng.testa')

to_predict_test = vectorizer.transform(featurizer(test_file)) #vectorizing test data features
predicted_classes_test = classifier.predict(to_predict_test) #predicting classes for test set


i = 0 #appending predicted classes to test data
for sentence in test_file:
    for token in sentence:
        token.append(predicted_classes_test[i])
        i += 1


# **Writing test data with predicted classes to file**

# In[6]:

with open("eng.guessa", "w") as variable_file:
    for sentence in test_file:
        for token in sentence:
            variable_file.write(" ".join(token))
            variable_file.write("\n")
        variable_file.write("\n")

