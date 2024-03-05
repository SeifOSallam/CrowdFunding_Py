from file_service import FileService
from project_validations import ProjectValidator

class ProjectController:
    def __init__(self):
        self.fileService = FileService()
        self.projectValidator = ProjectValidator()

    def viewProjects(self, user):
        fileData = self.fileService.getData()
        for userData in fileData:
            if userData["Email"] == user.email:
                for project in userData["Projects"]:
                    print(project)

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
        for i in range(0, len(fileData) + 1):
            if fileData[i]['Email'] == user.email:
                for j in range(0, len(fileData[i]['Projects']) + 1):
                    if fileData[i]['Projects'][j]['Title'] == title:
                        del fileData[i]['Projects'][j]
                        found = True
                        break
            if found:
                break
        self.fileService.addData(fileData)