# this file implement KNN algorithm for classification

class Knn:
    def __init__(self,k = 4):
        self.trainingData = []
        self.testingData = []
        self.k = k

    def setTrainingData(self,trainingData):
        self.trainingData = trainingData
    
    def setTestingData(self,testingData):
        self.testingData = testingData

    def findKNearest(self,example,exampleSet,k):
        kNearest, distances = [], []
        #Build lists containing first k examples and their distances
        for i in range(k):
            kNearest.append(exampleSet[i])
            distances.append(example.distance(exampleSet[i]))
        maxDist = max(distances) #Get maximum distance
        #Look at examples not yet considered
        for e in exampleSet[k:]:
            dist = example.distance(e)
            if dist < maxDist:
                #replace farther neighbor by this one
                maxIndex = distances.index(maxDist)
                kNearest[maxIndex] = e
                distances[maxIndex] = dist
                maxDist = max(distances)      
        return kNearest, distances
    
    def KNearestClassify(self,label,k):
        """Assumes training & testSet lists of examples, k an int
       Predicts whether each example in testSet has label
       Returns number of true positives, false positives,
          true negatives, and false negatives"""
        truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
        for testCase in self.testingData:
            nearest, distances = self.findKNearest(testCase, self.trainingData, k)
            #conduct vote
            numMatch = 0
            for i in range(len(nearest)):
                if nearest[i].getOutcome() == label:
                    numMatch += 1
            if numMatch > k//2: #guess label
                if testCase.getOutcome() == label:
                    truePos += 1
                else:
                    falsePos += 1
            else: #guess not label
                if testCase.getOutcome() != label:
                    trueNeg += 1
                else:
                    falseNeg += 1
        return truePos, falsePos, trueNeg, falseNeg

    def getResult(self,label):
        return self.KNearestClassify(label,self.k)
