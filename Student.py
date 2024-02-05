class Student:
    def __init__(self,rollno,n,sem,cgpa):
        self.__name = n
        self.__rollNumber = rollno
        self.__cgpa = cgpa
        self.__semester = sem

    def getName(self):
        return self.__name
    def getRollNumber(self):
        return self.__rollNumber
    def getCgpa(self):
        return self.__cgpa
    def getSemster(self):
        return self.__semester
    def getStudent(self):
        return Student(self.__name,self.__rollNumber,self.__semester,self.__cgpa)
    def printStudent(self):
        print("Name:", self.__name, "RollNo:",
              self.__rollNumber, "CGPA:", self.__cgpa,"Semester:",self.__semester)

