class Person:
    def __init__(self,data):
        self.outcome = int(data[8])
        self.featureVec = []
        for i in range(8):
            self.featureVec.append(float(data[i]))
        
    def getFeatureVec(self):
        return self.featureVec
        
    def getOutcome(self):
        return self.outcome

    def minkowskiDist(self,v1, v2, p):
        """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
        dist = 0.0
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i])**p
        return dist**(1/p)

    def distance(self,other):
        return self.minkowskiDist(self.getFeatureVec(), other.getFeatureVec(), 2)
    
    def dimensionality(self):
        return len(self.featureVec)