from user_controller import UserController
from project_controller import ProjectController
controller = UserController()
projectController = ProjectController()

controller.registerUser(
    "seif", 
    "sallam", 
    "seif.osallam@gmail.com",
    "dodofire",
    "dodofire",
    "01099134054"
)

controller.loginUser("seif.osallam@gmail.com", "dodofire")

controller.createProject("Hello3", "Details", 10000, "1000", "5000")
# controller.createProject("Hello2", "Details2", 102000, "10200", "50200")
# controller.deleteProject("Hello")

