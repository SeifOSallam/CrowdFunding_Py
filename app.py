from user_controller import UserController
from project_controller import ProjectController
userController = UserController()
projectController = ProjectController()


def projectsMenu():
    while True:
        print('1- Create Project')
        print('2- View All Projects')
        print('3- Edit Project')
        print('4- Delete Project')
        print('5- Logout\n')
        try:
            userinp = int(input("> "))
            if userinp == 1:
                title = input("Title: ")
                details = input("Details: ")
                target = int(input("Target: "))
                start = input("Start: ")
                end = input("End: ")
                userController.createProject(title, details, target, start, end)

            elif userinp == 2:
                projects = userController.viewProjects()
                for i in range (0, len(projects)):
                    print(str(i+1) + "- " + str(projects[i]))
            elif userinp == 3:
                projects = userController.viewProjects()
                for i in range (0, len(projects)):
                    print(str(i+1) + "- " + str(projects[i]))
                print('Enter the project\'s index\n')
                indexinp = int(input('> '))
                print('Enter the new project\n')
                title = input("Title: ")
                details = input("Details: ")
                target = int(input("Target: "))
                start = input("Start: ")
                end = input("End: ")

                userController.editProject(indexinp, title, details, target, start, end)
                
            elif userinp == 4:
                title = input("Title: ")
                userController.deleteProject(title)
            elif userinp == 5:
                userController.logoutUser()
                return
        except:
            print('Invalid input, try again.')

def login():
    email = input("Email: ")
    password = input("Password: ")
    if userController.loginUser(email, password):
        projectsMenu()
    else:
        print("Invalid email or password!")


def register():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    email = input('Email: ')
    password = input('Password: ')
    confirm_password = input('Confirm Password: ')
    phone = input('Phone: ')
    userController.registerUser(
        first_name,
        last_name,
        email,
        password,
        confirm_password,
        phone
    )

def mainMenu():
    while True:
        print('1- Login')
        print('2- Register')
        print('*- Exit\n')
        try:
            userinp = int(input("> "))
            if userinp == 1:
                login()
            elif userinp == 2:
                register()
            else:
                print("Thank you for using the application!")
                return
        except:
            print("Invalid input, try again")



mainMenu()

