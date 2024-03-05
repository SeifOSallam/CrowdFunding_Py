import os
import json
from user_model import User
from project_model import Project

class FileService:
    def __init__(self):
        self.filePath = "users.json"
    
    def addData(self, data):
        with open(self.filePath, "w") as file:
            json.dump(data, file, indent=4)


    def getData(self):
        if os.path.exists(self.filePath):
            with open(self.filePath, "r") as file:
                return json.load(file)
        else:
            return []
    
    def getUser(self, user):
        return self.getData()

    
        
