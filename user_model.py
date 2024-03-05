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
        return User(
            json["First_Name"],
            json["Last_Name"],
            json["Email"],
            json["Password"],
            json["Phone"]
        )
    
    def toJson(self):
        return {
            "First_Name": self.firstName,
            "Last_Name": self.lastName,
            "Email": self.email,
            "Password": self.password,
            "Phone": self.phone,
            "Projects" : self.projects
        }
    
