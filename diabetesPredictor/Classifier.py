import random

class Classifier:
    def __init__(self,data,method):
        """data is dataset for training and testing by method parameter method"""
        self.data = data
        self.method = method
    
    def splitData(self,ratio = 5):
        """splits the dataset into training and testing data according to given ratio"""
        sampleIndices = random.sample(range(len(self.data)),len(self.data)//ratio)
        trainingSet, testSet = [],[]
        for i in range(len(self.data)):
            if i in sampleIndices:
                testSet.append(self.data[i])
            else:
                trainingSet.append(self.data[i])
        return trainingSet, testSet

    def getStats(self,truePos, falsePos, trueNeg, falseNeg, toPrint = True):
        """print the status of result on the terminal"""
        accur = self.getAccuracy(truePos, falsePos, trueNeg, falseNeg)
        sens = self.getSensitivity(truePos, falseNeg)
        spec = self.getSpecificity(trueNeg, falsePos)
        if toPrint:
            print(' Accuracy =', round(accur, 3))
            print(' Sensitivity =', round(sens, 3))
            print(' Specificity =', round(spec, 3))
        return (accur, sens, spec)

    def getAccuracy(self,truePos, falsePos, trueNeg, falseNeg):
        numerator = truePos + trueNeg
        denominator = truePos + trueNeg + falsePos + falseNeg
        return numerator/denominator

    def getSensitivity(self, truePos, falseNeg):
        try:
            return truePos/(truePos + falseNeg)
        except ZeroDivisionError:
            return float('nan')
    
    def getSpecificity(self, trueNeg, falsePos):
        try:
            return trueNeg/(trueNeg + falsePos)
        except ZeroDivisionError:
            return float('nan')

    def run(self, numSplits = 1,toPrint = True):
        """Run the classifier on given dataset with given method.
            Inputs : 
            numSplit - an integer that defines, how many random split will be done.
            toPrint - true for printing status on the terminal.
            Outputs : 
            integer values of true and false postives and negatives"""
        truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
        random.seed(0)
        for t in range(numSplits):
            trainingSet, testSet = self.splitData()
            self.method.setTrainingData(trainingSet)
            self.method.setTestingData(testSet)
            results = self.method.getResult(1)
            truePos += results[0]
            falsePos += results[1]
            trueNeg += results[2]
            falseNeg += results[3]
        self.getStats(truePos/numSplits, falsePos/numSplits,
                trueNeg/numSplits, falseNeg/numSplits, toPrint)
        return truePos/numSplits, falsePos/numSplits, trueNeg/numSplits, falseNeg/numSplits