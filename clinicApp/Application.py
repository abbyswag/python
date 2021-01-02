from Doctor import Doctor
from Patient import Patient
from Appointment import Appointment
from Schedule import Schedule
from datetime import date

class Application():
    def __init__(self):
        self.doctors = []
        self.appointments = []
        self.workingApp = True

    def showTitle(self):
        print('**************************************')
        print('** Welcome to Rotten Parck Hospital **')
        print('**************************************')

    def showFirstMenu(self):
        print('1. Book an appoitment')
        print('2. Cancel an appoitment')
        print("3. View a doctor's schedule")
        print('4. View a patient apponitment')
        print('5. Exit')

    def addDoctors(self):
        d1 = Doctor('Daniel','Hagan','Opthalmologist',[])
        d2 = Doctor('Bravo','Gilbert','Radiologist',[])
        d3 = Doctor('Steven','Seagal','Cardiologist',[])
        d4 = Doctor('Igor','Dondon','Oncologist',[])
        self.doctors.append(d1)
        self.doctors.append(d2)
        self.doctors.append(d3)
        self.doctors.append(d4)
        # generating schedule for doctors
        for doctor in self.doctors:
            for day in range(1): # set number of days of program
                for hour in range(1,8): # set number of hours per day
                    today = date.today()
                    schedule = Schedule(today,8+hour,9+hour,doctor)
                    doctor.addSchedule(schedule)
                

    def start(self):
        self.addDoctors()
        self.showTitle()
        validInput = True
        while(self.workingApp):
            self.showFirstMenu()
            readline = input()
            print('\n')
            # validation goes here
            while(validInput):
                if readline.isdigit():
                    readlineInt = int(readline)
                    break
                    if readlineInt < 1 or readlineInt > 5:
                        print('Enter option is not valid')
                        readline = input()
                else:
                    print('Enter option is not valid')
                    readline = input()
            # ...
            while(validInput):
                if readlineInt == 1:
                    validInput = self.bookAppointment()
                    break
                elif readlineInt == 2:
                    validInput = self.cancelAppointment()
                    break
                elif readlineInt == 3:
                    validInput = self.viewDoctors()
                    break
                elif readlineInt == 4:
                    validInput = self.viewAppointment()
                    break
                elif readlineInt == 5:
                    validInput = False
                    self.workingApp = False
                else:
                    break
        print('Have a nice day')

    # for 1st option
    def bookAppointment(self):
        print('Please Enter the following information.')
        print('1. First Name')
        firstName = input()
        print('2. Surname')
        lastName = input()
        print('3. Telephone')
        phone = input()
        print('4. Date of Birth (dd//MM//YYYY) format')
        dateOfBirth = input()
        print('Country of Origin')
        countryOfOrigin = input()
        # creating patient object
        patient = Patient(firstName,lastName,phone,dateOfBirth,countryOfOrigin)
        print('Succesful register!')
        print('**************************************\n')
        print('Now please enter the time you want to make an appointment (hour 8-14)')
        hour = input()
        print('\n')
        # validation of hour goes here
        while(True):
            if hour.isdigit():
                hourInt = int(hour)
                if hourInt >= 8 and hourInt <= 14:
                    break
                else:
                    print('Please enter valid input hour')
                    hour = input()
            else:
                print('Please enter valid input hour')
                hour = input()
        # ...
        schedules = self.findSchedules(hourInt)
        print('Available doctors are: ')
        index = 1
        for schedule in schedules:
            print(str(index) + ') '+schedule.getDoctor().getFriendlyName()+' - '+str(schedule.getStartHour())+' to '+str(schedule.getEndHour()))
            index += 1
        # ...
        print('Choose a appointment 1 - ' + str(index-1))
        indexRead = input()
        print('\n')
        # validation goes here
        valid = False
        indexReadInt = 0
        while(not valid):
            if indexRead.isdigit():
                indexReadInt = int(indexRead)
                if indexReadInt > 0 and indexReadInt < index:
                    valid = True
                else:
                    print('Enter a index in interval 1 - ' + str(index-1))
            else:
                print('Enter a index in interval 1 - ' + str(index-1))
        # creating appointment object
        appointment = Appointment(schedules[indexReadInt],patient)
        self.appointments.append(appointment)
        print('Congrats! You have made a appointment')
        print('**************************************\n')
        return True
    
    # helper function for option 1
    def findSchedules(self,hour):
        listToReturn = []
        for doctor in self.doctors:
            for schedule in doctor.getSchedules():
                if(schedule.getStartHour() <= hour and schedule.getEndHour() > hour):
                    if len(self.appointments) == 0:
                        listToReturn.append(schedule)
                    else:
                        for appointment in self.appointments:
                            if appointment.getSchedule() != schedule:
                                listToReturn.append(schedule)
        return listToReturn
    
    # for 2nd option
    def cancelAppointment(self):
        print('Please enter you phone number')
        phone = input()
        print('\n')
        # validation goes here
        appointmentList = self.viewPatientAppointment(phone)
        for a in range(len(appointmentList)):
            print(str(a+1) + ') ' + appointmentList[a].show())
        print('what appointment you wish to cancel?')
        indexInt = int(input())
        if indexInt > len(appointmentList):
            print('Invalid Input')
        self.appointments.remove(appointmentList[indexInt-1])
        print('You appointment has been removed.')
        print('**************************************\n')
        return True
    
    # for 3rd option
    def viewDoctors(self):
        index = 1
        for doctor in self.doctors:
            print(str(index) + ') ' + doctor.getFriendlyName())
            index += 1
        print("what doctor's schedule you want to see?")
        indexInt = int(input())
        print('\n')
        for schedule in self.doctors[indexInt-1].getSchedules():
            for appointment in self.appointments:
                if schedule != appointment.getSchedule():
                    print('Free from ' + str(schedule.getStartHour()) + ' to ' + str(schedule.getEndHour()))
        print('**************************************\n')
        return True
    
    # for 4rth option
    def viewAppointment(self):
        print('Please enter your phone number')
        phone = input()
        print('\n')
        appointmentList = self.viewPatientAppointment(phone)
        for appointment in appointmentList:
            print(appointment.show())
        print('**************************************\n')
        return True

    # helper function for option 2 and 4
    def viewPatientAppointment(self,phone):
        listToReturn = []
        print('Your appointment for this week')
        if len(self.appointments) == 0:
            print('You have no appointment')
        for appointment in self.appointments:
            if appointment.getPatient().getTelephone() == phone:
                listToReturn.append(appointment)
        return listToReturn


        


        
            
