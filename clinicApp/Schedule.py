class Schedule():
    def __init__(self,date,startHour,endHour,doctor):
        self.date = date
        self.startHour = startHour
        self.endHour = endHour
        self.doctor = doctor

    def getDate(self):
        return self.date
    def getStartHour(self):
        return self.startHour
    def getEndHour(self):
        return self.endHour
    def getDoctor(self):
        return self.doctor
    
    