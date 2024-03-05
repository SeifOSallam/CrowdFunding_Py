class ProjectValidator:
    def __init__(self):
        pass
    
    def checkExists(self, fileData, user, projectTitle):
        for fileUser in fileData:
            if fileUser['Email'] == user.email:
                for userProject in fileUser['Projects']:
                    if userProject['Title'] == projectTitle:
                        return True
        
        return False
    
    def editIndex(self, fileData, user, index):
        for fileUser in fileData:
            if fileUser['Email'] == user.email:
                if len(fileUser['Projects']) < index:
                    return False
                return True


