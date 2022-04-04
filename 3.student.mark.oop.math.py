import math
import numpy as np

class Student:
    def __init__(self, stuid, stuname, studob, gpa=0):
        self.stuid = stuid
        self.stuname = stuname
        self.studob = studob
        self.gpa = gpa
        
    def get_stuid(self):
        return self.stuid

    def get_stuname(self):
        return self.stuname

    def get_studob(self):
        return self.studob
    
    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

class Course:
    def __init__(self, courseid, coursename, credit):
        self.courseid = courseid
        self.cname = coursename
        self.credit = credit

    def get_courseid(self):
        return self.courseid

    def get_coursename(self):
        return self.coursename
    
    def get_credit(self):
        return self.credit

class Mark():
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

    def get_mark(self):
        return self.mark

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course
    

class Show():
    students = []
    courses = []
    marks = []

    numberofstudents = None
    numberofcourses = None

    def number_students(self):
        while True:
            try:
                self.numberofstudents = int(input("Enter number of students: "))
                while self.numberofstudents <= 0:
                    print("Number of students has to be positive integer!\n")
                    self.numberofstudents = int(input("Enter again number of students: "))
            except:
                print("Number of students has to be positive integer!\n")
            else:
                break

    def number_courses(self):
        while True:
            try:
                self.numberofcourses = int(input("Enter number of courses: "))
                while self.numberofcourses <= 0:
                    print("Number of couses has to be positive integer!\n")
                    self.numberofcourses = int(input("Enter again number of courses: "))
            except:
                print("Number of courses has to be positive integer!\n")
            else:
                break


    def infoofstudent(self):
        if self.numberofstudents <= 0:
            print("Student list is empty. Please enter number of students!")
        elif self.numberofstudents > len(self.students):
            for i in range(0, self.numberofstudents):
                print(f"Enter information of student #{i + 1}")
                while True:
                    try:
                        stuid = int(input(f"Enter student id: "))
                        while stuid <= 0:
                            stuid = int(input(f"ID must be positive. Enter again student id: "))
                    except:
                        print("ID has to be positive integer!")
                    else:
                        break
                        
                while True:
                    try:
                        stuname = input(f"Enter name of student #{stuid}: ")
                        while len(stuname) == 0:
                            stuname = input(f"Student name can't be empty.Enter agian name of student #{stuid}: ")
                    except:
                        print(f"Student name can't be empty.Enter agian name of student #{stuid}: ")
                    else:
                        break 

                while True:
                    try:
                        studob = input(f"Enter date of birth of student #{stuid}: ")
                        while len(sdob) == 0:
                            sdob = input(f"Student name can't be empty.Enter agian name of student #{stuid}: ")
                    except:
                        print("Student name can't be empty.Enter again name of student!!!")
                    else:
                        break

                self.students.append(Student(stuid, stuname, studob))
        else:
            print(f"The student list is full({len(self.students)} students).Please use function 1 to extra student list")
    

    def infoofcourse(self):
        if self.numberofcourses <= 0:
            print("Course list is empty. Please enter number of courses!")
        elif self.numberofcourses > len(self.courses):
            for i in range(0, self.numberofcourses):
                print(f"Enter information of course #{i + 1}")
                while True:
                    try:
                        courseid = int(input(f"Enter course id: "))
                        while courseid <= 0:
                            courseid = int(input(f"Enter again course id: "))
                    except:
                        print("Course id must be positive integer!")
                    else:
                        break

                while True:
                    try:    
                        coursename = input(f"Enter name of course #{courseid}: ")
                        while len(coursename) == 0:
                            coursename = input(f"Name of course can't be empty.Enter name of course #{courseid}: ")
                    except:
                        print(f"Name of course can't be empty.Please enter name of course #{courseid}!!! ")
                    else:
                        break

                while True:
                    try:
                        credit = int(input(f"Enter credit of course #{courseid}: "))
                        while credit <= 0:
                            credit = int(input(f"Credit of Course is positive.Enter again credit of course: "))
                    except:
                        print(f"Credit of Course is positive.Please enter again credit of course #{courseid}!")
                    else:
                        break
                self.courses.append(Course(courseid, coursename, credit))
        else:
            print(f"The list of courses is full({len(self.courses)} courses).Please use function 2 to extra student list")

    def enter_mark(self):
        while True:
            try:
                courseid = int(input("Enter id of course you want to input mark: "))
                while courseid <= 0:
                    courseid = int(input("Course id must be positive.Enter  again course id you want to input mark: "))
            except:
                print("Course id must be positive.Please enter again course id you want to input mark!")
            else:
                break
        for course in self.courses:
            if course.get_courseid() == courseid:
                for student in self.students:
                    while True:
                        try:
                            mark = float(input(f"Enter mark of course {courseid} for student {student.get_stuname()}: "))
                            while mark < 0:
                                mark = float(input("Mark must not be negative\n " \
                                                   f"Enter again mark of course {courseid} for student {student.get_stuname()}: "))
                        except:
                            print("Mark must not be negative\n " \
                                 f"Enter again mark of course {courseid} for student {student.get_stuname()}!")
                        else:
                            break
                    mark = math.floor(mark * 10)/10.0

                    self.marks.append(Mark(student, course, mark))
            else:
                print("Course id is not existed!") 
  
    
    def GPA(self):
        while True:
            try:
                stuid = int(input(f"Enter student id you want to calculate GPA: "))
                while sid <= 0:
                    stuid = int(input(f"ID must be positive. Enter again student id: "))
                
                check = 0
                for mark in self.marks:
                    if check == (len(self.marks) - 1):
                        print(f"Error. Student id {stuid} not existed!!!")
                        break
                    elif stuid != mark.get_student().get_stuid():
                        check = check + 1
                    else:
                        print("Student id is existed!")
            except:
                print("ID must be positive. Enter again student id!")
            else:
                break

        list_score = np.array([])
        list_credit = np.array([])

        check = 0
        for mark in self.marks:
            if stuid == mark.get_student().get_stuid():
                list_score = np.append(list_score, mark.get_mark())
                list_credit = np.append(list_credit, mark.get_course().get_credit())

        gpa = np.dot(list_score, list_credit) / np.sum(list_credit)

        for student in self.students:
            if stuid == student.get_stuid():
                student.set_gpa(gpa)

    def sort_list_of_student(self):
        if len(self.students) == 0:
            print("List of student information is empty!") 
        else:
            data_type = [('stuid', 'S30'), ('stuname', 'S30'), ('gpa', float)]
            new_students = []
            for student in self.students:
                new_student_infor = (student.get_stuid(), student.get_stuname(), student.get_gpa())
                new_students.append(new_student_infor)
            sorting_new_students = np.array(new_students, dtype=data_type)
            sorted_list = np.sort(sorting_new_students, order = 'gpa')
            print(sorted_list)

    def list_of_students(self):
        if len(self.students) == 0:
            print("The student list is empty!")
        else:
            print("Student id", "Student name", "Student dob", sep="             ")
            for student in self.students:
                print(f"{student.get_stuid()}" ,
                      f"{student.get_stuname()}" ,
                      f"{student.get_studob()}", sep="             ")

    def list_of_courses(self):
        if len(self.courses) == 0:
            print("The course list is empty!")
        else:
            for course in self.courses:
                print(f"Course id: {course.get_courseid()}" \
                      f"Course name: {course.get_coursename()}", sep=" - ")

    def list_of_mark(self):
        if len(self.marks) == 0:
            print("The mark list is empty!")
        else:
            while True:
                try:
                    courseid = int(input("Enter id of course you want to list marks: "))
                    while courseid <= 0:
                        courseid = int(input("Course id must be positive.Enter  again course id you want to list marks: "))
                     
                    check = 0
                    for mark in self.marks:
                        if check == (len(self.marks) - 1):
                            print("Error")
                            break
                        elif courseid != mark.get_course().get_courseid():
                            check = check + 1
                        else:
                            print("Course id is existed!")
                except:
                    print("Course id must be positive.Enter again course id you want to list marks!!!")
                else:
                    break
            for mark in self.marks:
                if courseid == mark.get_course().get_courseid():
                    print(mark.get_student().get_stuname(), mark.get_course().get_coursename(), mark.get_mark(), sep="-")

    
    def start_Show(self):
        print("Please select operation: \n"           \
                "1.Input number of students \n"       \
                "2.Input number of courses \n"        \
                "3.Input information for students \n" \
                "4.Input information for courses \n"  \
                "5.Input mark for given courses \n"   \
                "6.Calculate GPA for given student\n" \
                "7.Sort student by gpa\n"             \
                "8.List of the students \n"                  \
                "9.List of the courses \n"                   \
                "10.List of the marks \n"                    \
                "11.Exist!!!" ,  )
        while True:
            select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11:"))
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
                self.GPA()
            elif select == 7:
                self.sort_list_of_student()
            elif select == 8:
                self.list_of_students()
            elif select == 9:
                self.list_of_courses()
            elif select == 10:
                self.list_of_mark()
            elif select == 11:
                print("Existed!!!")
                break
            else:
                print("Invalid value")
                

if __name__ == "__main__":
    d = Show()
    d.start_Show()
