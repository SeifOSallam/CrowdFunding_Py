from user_controller import UserController

controller = UserController()

controller.registerUser(
    "seif", 
    "sallam", 
    "seif.osallam@gmail.com",
    "dodofire",
    "dodofire",
    "01099134054"
)

controller.loginUser("seif.osallam@gmail.com", "dodofire")