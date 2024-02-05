from Student import Student
import pymysql
class Registrar:
    def __init__(self, hst="localhost", usr="root", pas="saad", db="myDb"):
        if hst == "" or usr == "" or pas == "" or db == "":
            myexp = EmptyStringArgument()
            raise myexp
        self.__host = hst
        self.__user = usr
        self.__password = pas
        self.__database = db
        self.myDb = None
        self.__connectionWithDB()

    def __connectionWithDB(self):
        if self.myDb != None:
            return
        try:
            self.myDb = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,
                                        db=self.__database)
        except Exception as e:
            print(str(e))
    def getStudent(self):
        n = input("Enter your name.")
        r = input("Enter your roll number.")
        semester = input("Enter your semester.")
        cgpa = input("Enter your cgpa.")
        obj = Student(r,n,semester,cgpa)
        return obj
    def getUserName(self):
        userName = input("Select your userName.")
        return userName
    def getPassword(self):
        password = input("Set your password.")
        return password
    def registerStudent(self):
        try:
            myCursor=self.myDb.cursor()
            studObj = self.getStudent()
            query = "INSERT INTO students (rollno,name,semester,cgpa) VALUES(%s,%s,%s,%s);"
            values = (studObj.getRollNumber(), studObj.getName(), studObj.getSemster(), studObj.getCgpa())
            myCursor.execute(query, values)
            self.myDb.commit()
            sql = "INSERT INTO login (user_name,password) VALUES(%s,%s);"
            values=(self.getUserName(),self.getPassword())
            myCursor.execute(sql,values)
            self.myDb.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            if myCursor is not None:
                myCursor.close()

    def __getCourses(self):
        try:
            myCursor = self.myDb.cursor()
            sql = "select * from courses"
            myCursor.execute(sql)
            data = myCursor.fetchall()
            return data
        except Exception as e:
            print(str(e))
            return False
        finally:
            if myCursor is not None:
                myCursor.close()
    def showAvailableCourses(self):
       data = self.__getCourses()
       if data == False:
           return
       for item in data:
           print("course_id: ",item[0],"\tcourse_name: ",item[1],"    course_credit_hour: ",item[2],
                 "\tcourse_open_closed: ",item[3])
    def __searchAvailableCourse(self,key,data):
        if data == False:
            return
        key = int(key)
        for item in data:
            if int(item[0]) == key:
                if item[3] == 'y' or item[3] == 'Y' or item[3] == 'yes' or item[3] =='YES':
                    return True
        return False

    def enrollCourse(self):
        data = self.__getCourses()
        cId = input("Enter course Id.")
        rollno=input("Enter your roll number.")
        if self.__searchAvailableCourse(cId,data) == False:
            return False
        try:
            myCursor = self.myDb.cursor()
            sql = "update students set course_id=%s where rollno=%s"
            values = (cId, rollno)
            myCursor.execute(sql, values)
            self.myDb.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
    def overAllEnrollMents(self):
        try:
            myCursor = self.myDb.cursor()
            sql = "select students.rollno, students.name, students.semester, courses.course_id, courses.course_name from students, courses where students.course_id=courses.course_id"
            myCursor.execute(sql)
            data = myCursor.fetchall()
            myCursor.close()
            print("Roll_No:\t\tName\t\tSemester:\t\tCourse_Id:\t\tCourse_Name:\t\t")
            for item in data:
                print(item[0],'\t   ',item[1],'\t\t',item[2],'\t\t   ',item[3],'\t\t\t\t',item[4],'\t\t')
        except Exception as e:
            print(str(e))








'''
def insertStudentData(self,stud):
    try:
        myCursor = self.myDb.cursor()
        query = "INSERT INTO student (Roll_Num,Name,Semester,cgpa) VALUES(%s,%s,%s,%s);"
        values=(stud.getRollNumber(),stud.getName(),stud.getSemster(),stud.getCgpa())
        myCursor.execute(query,values)
        self.myDb.commit()
    except Exception as e:
        print(str(e))
    finally:
        if myCursor is not None:
            myCursor.close()
def __displayAvailableCourses(self, data):
    if data == None:
        return
    for item in data:
        print("Course_Id:",item[0],"Course_Name:",item[1],"Available_OR_Not:",item[2])
def __searchAvailableCourses(self,key,data):
    if data == None:
        return
    key = int(key)
    for item in data:
        if int(item[0]) == key and int(item[2]) == 1:
            return True
    return False

def registrationForm(self):
    try:
        myDbCursor = self.myDb.cursor()
        sql = "select * from course"
        myDbCursor.execute(sql)
        data = myDbCursor.fetchall()
        self.__displayAvailableCourses(data)
        choice = input("Which course You wanna Enroll.\n"
                       "For pf enter a.\nFor oop enter b.\n"
                       "For dsa enter c.\nFor Algorithm enter d.\n")
        status = True
        while status:
            if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
                status = False
            else:
                print("You select wrong choice please enter valid input.\n")
                choice = input("Which course You wanna Enroll.\n"
                               "For pf enter a.\nFor oop enter b.\n"
                               "For dsa enter c.\nFor Algorithm enter d.\n")
        key = int(input("Enter Id of Selected Course."))
        status = False
        if self.__searchAvailableCourses(key, data) == True:
            roll = input("Enter Roll_Number of you student.")
            n = input("Enter Name of Student.")
            sem = input("Enter Student Current Semester")
            cgpa = input("Enter Studemt Current cgpa")
            obj = Student(roll, n,sem, cgpa)
            self.insertStudentData(obj)
            status = True
        else:
            print("Enrollement for selected course is closed.")
            return False
        if choice == 'a' or choice == 'A':
                print("Your have successfully enrolled in pf.")
        elif choice == 'b' or choice == 'B':
                print("Your have successfully enrolled in oop.")
        elif choice == 'c' or choice == 'C':
                print("Your have successfully enrolled in dsa.")
        elif choice == 'c' or choice == 'C':
                print("Enrollement for Algorithm is not Available.")
        return True
    except Exception as e:
        print(str(e))
def confirmationMessage(self):
    if self.registrationForm() == True:
        print("You have successsfully enrolled in selected course.\n")
    else:
        print("Eror.\n")
'''