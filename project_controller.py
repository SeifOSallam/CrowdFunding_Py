from file_service import FileService
from project_validations import ProjectValidator

class ProjectController:
    def __init__(self):
        self.fileService = FileService()
        self.projectValidator = ProjectValidator()

    def viewProjects(self):
        fileData = self.fileService.getData()
        allProjects = []
        for userData in fileData:
            allProjects.append(userData['Projects'])
        
        return allProjects

    def addProject(self, user, project):
        fileData = self.fileService.getData()
        if self.projectValidator.checkExists(fileData, user, project['Title']):
            print('Project already exists!')
            return
        
        for i in range(0, len(fileData) + 1):
            if fileData[i]['Email'] == user.email:
                fileData[i]['Projects'].append(project)
                break
        self.fileService.addData(fileData)
    
    def deleteProject(self, user, title):
        fileData = self.fileService.getData()
        if not self.projectValidator.checkExists(fileData, user, title):
            print('Project doesn\'t exist!')
            return
        
        found = False
        for i in range(0, len(fileData)):
            if fileData[i]['Email'] == user.email:
                for j in range(0, len(fileData[i]['Projects']) + 1):
                    if fileData[i]['Projects'][j]['Title'] == title:
                        del fileData[i]['Projects'][j]
                        found = True
                        break
            if found:
                break
        self.fileService.addData(fileData)

    def editProject(self, user, newProjectIndex, newProject):
        fileData = self.fileService.getData()
        if not self.projectValidator.editIndex(fileData, user, newProjectIndex):
            print('Index out of bounds!')
            return
        for i in range(0, len(fileData)):
            if fileData[i]['Email'] == user.email:
                fileData[i]['Projects'][newProjectIndex] = newProject
                break
        
        self.fileService.addData(fileData)