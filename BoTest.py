import random, lib.Bo 

def getSample():
    return [random.randint(0, 100), random.randint(0, 3)]

def getRating(v, target):
    return [abs(v[0]-target[0]) + abs(v[1]-target[1])]


if __name__ == "__main__":

    x = []
    y = []
    for i in range(10):
        s = getSample()  
        r = getRating(s, [35, 2])
        x.append(s)
        y.append(r)

    z = list(zip(x, y))
    print(z)


    x0 = NumericDimension(min=0, max=100, name="p0")
    x1 = NumericDimension(min=0, max=3, name="p1")
    ranking_y = NumericDimension(min=0, max=10, name="Ranking")

    compSpace = ComputeSpace([x0, x1], [ranking_y])

    optimizer = Bo()


