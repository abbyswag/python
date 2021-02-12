import csv
from Person import Person
from Classifier import Classifier
from Lr import Lr
from Knn import Knn
from Kmeans import testClustering

# loading data from csv file
personList = []
with open('diabetes-dataset.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = 1
    for row in reader:
        if count != 1:
            data = ''.join(row).split(',')
            p = Person(data)
            personList.append(p)
        count += 1

print('result on based of logical regression')
lr = Lr()
c = Classifier(personList,lr)
c.run()
print('result on based on K nearest neighbours')
knn = Knn()
c = Classifier(personList,knn)
c.run()
print('result on based on K means')
for k in (2,4,6):
    print('\n     Test k-means (k = ' + str(k) + ')')
    posFracs = testClustering(personList, k, 2)