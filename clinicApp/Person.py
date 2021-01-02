class Person():
    def __init__(self,firstName,lastName,telephone,dateOfBirth,countryOfOrigin):
        self.firstName = firstName
        self.lastName = lastName
        self.telephone = telephone
        self.dateOfBirth = dateOfBirth
        self.countryOfOrigin = countryOfOrigin

    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getTelephone(self):
        return self.telephone
    def getDateOfBirth(self):
        return self.dateOfBirth
    def getCountryOfOrigin(self):
        return self.countryOfOrigin

    