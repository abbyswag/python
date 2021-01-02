from Person import Person

class Patient(Person):
    def __init__(self,firstName,lastName,telephone,dateOfBirth,countryOfOrigin):
        Person.__init__(self,firstName,lastName,telephone,dateOfBirth,countryOfOrigin)

