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


