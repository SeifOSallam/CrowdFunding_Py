from user_model import User
import json
import os
from file_service import FileService

class UserController:
    def __init__(self):
        self.fileService = FileService()

    def registerUser(self, firstName, lastName, email, password, confirmPassword, phone):
        if (password != confirmPassword):
            print("Entered passwords don't match.")
            return

        file_data = self.fileService.getData()
        
        user_data = User(firstName, lastName, email, password, phone)
        exists = next((x for x in file_data if x["Email"] == user_data.email), None)

        if exists:
            print("User already exists")
            return
        
        file_data.append(user_data.toJson())

        self.fileService.addData(file_data)


    def loginUser(self, email, password):
        
        file_data = self.fileService.getData()

        exists = next((x for x in file_data if x["Email"] == email and x["Password"] == password), None)
        if exists:
            self.currentUser = User.initJSON(exists)
            print("Welcome, " + self.currentUser.firstName)
        else:
            print("Sorry, user doesn't exist!")

    def logoutUser(self):
        self.currentUser = None
    
    def viewProjects(self):
        print(self.currentUser.projects)
    
    def createProject(self, title, details, target, start, end):
        

