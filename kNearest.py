#K Nearest Neighbours
#Aishwarya Srinivas

from math import sqrt
from collections import Counter




#------------------FUNCTIONS---------------------------
def kNearest (data, predict, k=3):

    if len(data) >= k:
        print ('Sorry, but K is set to a value less than total voting groups!')


    distances = []

    for i in data:
        for j in data [i]:
            euclidDistance = sqrt( (j[0]-predict[0])**2 + (j[1]-predict[1])**2 )
            distances.append([euclidDistance, i])

    votes = [i[1] for i in sorted(distances)[:k]]
    popularResult = Counter(votes).most_common(1)[0][0]


    return popularResult




#--------------------MAIN PROGRAM------------------------
#The data
dataset = {
        'Group 1':[[1,2],[2,3],[3,1]],
        'Group 2':[[6,5],[7,7],[8,6]]
    }
newFeatures = [5,7]


result = kNearest(dataset, newFeatures)
print('The point is in ' + result)
