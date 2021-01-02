class Appointment():
    def __init__(self,schedule,patient):
        self.schedule = schedule
        self.patient = patient
    
    def getSchedule(self):
        return self.schedule
    def getPatient(self):
        return self.patient
    def show(self):
        return 'with ' + self.getSchedule().getDoctor().getFirstName() + ' from ' + str(self.getSchedule().getStartHour()) + ' to ' + str(self.getSchedule().getEndHour())
