students_name = []
students = []
courses_id = []
courses = []
marks = []

def number_student():
    numberofstudent = int(input("Input number of student: "))
    return numberofstudent

def number_course():
    numberofcourse = int(input("Input number of course: "))
    return numberofcourse

num_of_student = number_student()
num_of_course = number_course()

def student_info():
    for i in range(1, num_of_student+1):
        stuid = input(f"Enter student #{i} id: ")
        stuname = input(f"Enter student #{i} name: ")
        studob = input(f"Enter student #{i} dob: ")
        student = [stuid, stuname, studob]
        students.append(student)
        students_name.append(stuname)

def course_info():
    for i in range(1, num_of_course+1):
        courseid = input(f"Enter course #{i} id: ")
        coursename = input(f"Enter course #{i} name: ")
        course = [courseid, coursename]
        courses.append(course)
        courses_id.append(courseid)

def enter_mark():
    courseid = int(input("Enter course id you want to input mark: "))
    
    if courseid in courses_id:
        for i in range(0, num_of_student):
            enter_mark = input(f"Enter mark of course {courseid} for student {students_name[i]} :")
            input_mark = [courseid, students_name[i], enter_mark]
            marks.append(input_mark)

def list_of_coures():
    for i in range(courses):
        print(f"Course info {i}: ")
        print(courses[i])

def list_of_students():
    for i in range(students):
        print(f"Student info {i}: ")
        print(students[i])

def output_mark():
    v = int(input("Enter course id you want to show: "))
    if v in courses_id:
        for items in marks:
            for nested_item in items:
                if nested_item == v:
                    print(items)

student_info()
course_info()
enter_mark()
output_mark()