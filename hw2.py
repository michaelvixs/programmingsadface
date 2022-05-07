from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def classifer(string): 
    pass

def main():
    lines = [line.strip() for line in open('pos.train')]

    poswords = []

    for l in lines:

        poswords.extend(l.split())
    print(poswords)

if __name__ == '__main__': 
    main()

