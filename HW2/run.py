from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def GetPosTest(TestLocation):
    lines = [line.strip() for line in open(TestLocation)]
    poswords = []
    posPolarity = []

    for l in lines:
        poswords.extend(l.split())
    for i in range(len(poswords)):
        posPolarity.append(1)
    return poswords, posPolarity

def GetPositiveTrain():
    lines = [line.strip() for line in open('hw2data/pos.train')]
    poswords = []
    posPolarity = []

    for l in lines:
        poswords.extend(l.split())
    for i in range(len(poswords)):
        posPolarity.append(1)
    return poswords, posPolarity

def GetNegativeTrain():
    lines = [line.strip() for line in open('hw2data/neg.train')]
    negwords = []
    negPolarity = []

    for l in lines:
        negwords.extend(l.split())
    for i in range(len(negwords)):
        negPolarity.append(0)
        
    return negwords, negPolarity

def classifer(string): 
    pass

def main():
    posx, posy = GetPositiveTrain()
    negx, negy = GetNegativeTrain()
    x = np.array(posx + negx)
    y = np.array(posy+negy)
    Vec = CountVectorizer(stop_words='english')
    x = Vec.fit_transform(x).toarray()
    #  = GetPosTest("hw2data/test/pos/cv009_29592.txt")
    gnb = GaussianNB()
    Boom = gnb.fit(x,y)

if __name__ == '__main__': 
    main()

