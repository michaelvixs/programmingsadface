from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer

def ContainsNum(string):
    nums = "1234567890"
    for i in nums:
        if i in string:
            return True
    return False

def getData(file):
    X,Y = np.empty([2,2]),np.empty([1,1])
    h = np.empty([1])
    with open(file) as f:
        for line in f:
            y,x = line.split()
            if not ContainsNum(x):
                X = np.append(X,x)
                Y = np.append(Y,y)
    
    return X,Y

def main():
    x,y = getData("data/es_v.txt")
    x = x[4:] # why do we need this?
    y = y[1:] # Numpy generated random numbers for some reason.
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    Vec = CountVectorizer(stop_words='english')
    x_train = Vec.fit_transform(x_train).toarray()
    gnb = GaussianNB()
    print("here")
    Boom = gnb.fit(x_train,y_train)

if  __name__ == "__main__":
    main()