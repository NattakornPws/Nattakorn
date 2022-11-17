# #Tuple
# #Way 1
# point = 1,7
# print(point[0])
# print(point[1])
# #Way 2
# pointB = (1,7)
# print(pointB[1])
#
# th = ("Thailand", 5, 10 ,15)

def distance(pointA, pointB):
    return ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**0.5

pointA = (1,7)
pointB = (1,10)
d = distance(pointA, pointB)
print(d)
