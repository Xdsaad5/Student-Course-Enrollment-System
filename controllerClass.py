from Login import Admin
from Registrar import Registrar
class View:
    def display(self):
        choice = input("a-Login.\tb-Registration.\n")
        obj = Registrar()
        if choice == 'b':
            if obj.registerStudent() == False:
                print("Your information isn't correct.")
                return
            else:
                print("Sucessfully Registered.Now login in Sysytem.")
        adObj = Admin()
        if adObj.verifyStudent() == False:
            return
        status = True
        count = 0
        while status:
            choice = input("a-Show Available Courses.\tb-Enroll In Course.\t\tc-Over All Enrollment.\td-Stop.")
            if choice == 'a':
                obj.showAvailableCourses()
            elif choice == 'b' and count == 0:
                if obj.enrollCourse() == True :
                    print("Your course has been registered successfully.")
                    count = count + 1
                else:
                    print("Course has not been registered.\nCourse Registration has been closed.")
            elif choice == 'b' and count == 1:
                print("You already enroll the course.\n")
            elif choice == 'c':
                obj.overAllEnrollMents()
            elif choice == 'd':
                status = False
                print("Good Bye.\n")
            else:
                print("you select Wrong choice.\n")


obj = View()
obj.display()