
def getData(File):
    Vec = [[],[],[]]
    with open(File) as f:
        for line in f:
            Vars = line.split()
            GoldenValue = int(Vars[0]) # Golden Value
            for i in range(1, len(Vars), 1):
                if not Vec[GoldenValue]:
                    Vec[GoldenValue] = []
                Vec[GoldenValue].append(Vars[i].split(":")[0])
    return Vec


def main():
    x = getData("hw3data/restaurant_train.txt")
    print(x[0][0:10])



if __name__ == "__main__":
    main()