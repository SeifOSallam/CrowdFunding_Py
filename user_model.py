class User:
    def __init__(self, firstName, lastName, email, password, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.projects = []
    
    @classmethod
    def initJSON(self, json):
        self.firstName = json["First_Name"]
        self.lastName = json["Last_Name"]
        self.email = json["Email"]
        self.password = json["Password"]
        self.phone = json["Phone"]
        self.projects = []
        return self
    
    def toJson(self):
        return {
            "First_Name": self.firstName,
            "Last_Name": self.lastName,
            "Email": self.email,
            "Password": self.password,
            "Phone": self.phone,
            "Projects" : self.projects
        }
    
