class Students:
    def __init__(self, stuid, stuname, studob):
        self.stuid = stuid
        self.stuname = stuname
        self.studob = studob

    def stuid(self):
        return self.stuid

    def stuname(self):
        return self.stuname

    def studob(self):
        return self.studob


class Courses:
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

    def courseid(self):
        return self.courseid

    def coursename(self):
        return self.coursename


class Marks():
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def mark(self):
        return self.mark

    def student(self):
        return self.student

    def course(self):
        return self.course

class Show():
    students = []
    courses = []
    marks = []

    numberofstudents = None
    numberofcourses = None


    def number_students(self):
        self.numberofstudents = int(input("Enter number of students: "))
        while True:
            if self.numberofstudents <= 0:
                print("Invalid value \n" \
                    "Number of students has to be positive integer!!!\n" \
                    "Please enter number of students againt")
                self.number_students()
            else:
                break

    def number_courses(self):
        self.numberofcourses = int(input("Enter number of courses: "))
        while True:
            if self.numberofcourses <= 0:
                print("Invalid value \n" \
                    "Number of courses has to be positive integer!!!\n" \
                    "Please enter number of courses againt")
                self.number_courses()
            else:
                break

    
    def infoofstudent(self):
        for i in range(0, self.numberofstudents):
            print(f"Enter information of student #{i + 1}")

            stuid = int(input(f"Enter student id: "))
            while stuid <= 0:
                stuid = int(input(f"ID must be positive. Enter again student id: "))

            stuname = input(f"Enter name of student #{stuid}: ")
            while len(stuname) == 0:
                stuname = input(f"Student name can't be empty.Enter agian name of student #{stuid}: ")

            studob = input(f"Enter date of birth of student #{stuid}: ")
            while len(studob) == 0:
                studob = input(f"Student date of birth can't be empty.Enter again date of birth of student #{sid}: ")

            self.students.append(Students(stuid, stuname, studob))
    

    def infoofcourse(self):
        for i in range(0, self.numberofcourses):
            print(f"Enter information of course #{i + 1}")

            courseid = int(input(f"Enter course id: "))
            while courseid <= 0:
                courseid = int(input(f"Course id is positive.Enter again course id: "))
            
            coursename = input(f"Enter name of course #{courseid}: ")
            while len(coursename) == 0:
                coursename = input(f"Name of course can't be empty.Enter name of course #{courseid}: ")

            self.courses.append(Courses(courseid, coursename))

    def enter_mark(self):
        courseid = int(input("Enter id of course you want to input mark: "))
        while courseid <= 0:
            courseid = int(input("Course id must be positive.Enter  again course id you want to input mark: "))
        for course in self.courses:
            if course.courseid() == courseid:
                for student in self.students:
                    mark = float(input(f"Enter mark of course {courseid} for student {student.stuname()}: "))
                    while mark < 0:
                        mark = float(input("Mark must not be negative\n " \
                                            f"Enter mark of course {courseid} for student {student.stuname()}: "))

                    self.marks.append(Marks(student, course, mark))


    def list_of_students(self):
        if len(self.students) == 0:
            print("The student list is empty!!!")
        else:
            print("Student id", "Student name", "Student dob", sep="             ")
            for student in self.students:
                print(f"{student.stuid()}" ,
                      f"{student.stuname()}" ,
                      f"{student.studob()}", sep="             ")

    def list_of_courses(self):
        if len(self.courses) == 0:
            print("The course list is empty!!!")
        else:
            for course in self.courses:
                print(f"Course id: {course.courseid()}" ,
                      f"Course name: {course.coursename()}", sep="\n")

    def list_of_mark(self):
        courseid = int(input("Enter id of course you want to list marks: "))
        while courseid <= 0:
            courseid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))
        if len(self.mark) == 0:
            print("The mark list is empty!!!")
        else:
            for mark in self.mark:
                if courseid == mark.course().courseid():
                    print(mark.student().stuname(), mark.course().coursename(), mark.mark(), sep="-")

    def start_Show(self):
        print("Please select operation: \n"           \
                "1.Enter number of students \n"       \
                "2.Enternumber of courses \n"        \
                "3.Enter information for students \n" \
                "4.Enter information for courses \n"  \
                "5.Enter mark for given courses \n"   \
                "6.List ofstudents \n"                  \
                "7.List ofcourses \n"                   \
                "8.List ofmarks \n"                     \
                "9.Exist!!!" ,
                )
        while True:
            select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9:"))
            if select == 1:
                self.number_students()    
            elif select == 2:
                self.number_courses()
            elif select == 3:
                self.infoofstudent()
            elif select == 4:
                self.infoofcourse()
            elif select == 5:
                self.enter_mark()
            elif select == 6:
                self.list_of_students()
            elif select == 7:
                self.list_courses()
            elif select == 8:
                self.list_of_mark()
            elif select == 9:
                print("Existed!!!")
                break
            else:
                print("Invalid value")
                


if __name__ == "__main__":
    d = Show()
    d.start_Show()
