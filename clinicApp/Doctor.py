from Person import Person

class Doctor(Person):
    def __init__(self,firstName,lastName,specialization,schedules):
        Person.__init__(self,firstName,lastName,000,'notAllowed','notAllowed')
        self.specialization = specialization
        self.schedules = schedules

    def getSpecialization(self):
        return self.specialization
    def getSchedules(self):
        return self.schedules

    def addSchedule(self,schedule):
        self.schedules.append(schedule)
    def getFriendlyName(self):
        return self.getFirstName() + ' ' + self.getLastName() + '-' + self.getSpecialization()

    


