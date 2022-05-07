from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


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
    lines = [line.strip() for line in open('neg.train')]
    negwords = []
    negPolarity = []

    for l in lines:
        negPolarity.append(0)
        negwords.extend(l.split())
        
    return negwords, negPolarity

def classifer(string): 
    pass

def main():
    x, y = GetPositiveTrain()
    X_train, X_test, y_train, y_test = train_test_split(x, y)
    print(y_train)
    #  = GetPosTest("hw2data/test/pos/cv009_29592.txt")
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).pred(X_test)

if __name__ == '__main__': 
    main()

