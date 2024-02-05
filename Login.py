import pymysql
class Admin:
    def __init__(self, hst='localhost', usr='root', pas='saad', db='myDb'):
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
    def verifyStudent(self):
        myCursor = self.myDb.cursor()
        sql = "select password from login"
        myCursor.execute(sql)
        data = myCursor.fetchall()
        data=[x[0] for x in data]
        i = 0
        count = 0
        while i < 5:
            userName = input("Enter your username.")
            password = input("Enter your Password.")
            for item in data:
                if password == item:
                    print("Successfully Login.")
                    return True
            if count == 0:
                print("You have entered wrong password."
                      "Again.")
            i = i + 1
        if count == 0:
            print("You login attempts has been reached.")
            return False
        return True

