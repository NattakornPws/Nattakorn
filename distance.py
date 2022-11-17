

def distance(pointA, pointB):
    return ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**0.5

if __name__ == '__main__':
    pointA = (1,7)
    pointB = (1,10)
    d = distance(pointA, pointB)
    print(d)
