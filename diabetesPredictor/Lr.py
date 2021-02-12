# This code process the data according to logistic regression
import sklearn.linear_model

class Lr:
    def __init__(self,prob = 0.5):
        self.trainingData = []
        self.testingData = []
        self.prob = prob
    
    def setTrainingData(self,trainingData):
        self.trainingData = trainingData
    
    def setTestingData(self,testingData):
        self.testingData = testingData

    def buildModel(self):
        """Building sklearn linear model from training data"""
        featureVecs, labels = [],[]
        for p in self.trainingData:
            featureVecs.append(p.getFeatureVec())
            labels.append(p.getOutcome())
        LogisticRegression = sklearn.linear_model.LogisticRegression
        model = LogisticRegression().fit(featureVecs, labels)
        return model

    def applyModel(self,model,label):
        """Applying model to test data"""
        testFeatureVecs = [e.getFeatureVec() for e in self.testingData]
        probs = model.predict_proba(testFeatureVecs)
        truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
        for i in range(len(probs)):
            if probs[i][1] > self.prob:
                if self.testingData[i].getOutcome() == label:
                    truePos += 1
                else:
                    falsePos += 1
            else:
                if self.testingData[i].getOutcome() != label:
                    trueNeg += 1
                else:
                    falseNeg += 1
        return truePos, falsePos, trueNeg, falseNeg
    
    def getResult(self,lable):
        model = self.buildModel()
        return self.applyModel(model,lable)