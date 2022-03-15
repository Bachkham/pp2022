course_info = {}
student_info = {}
course_with_mark = {}
end = False


def input_student_info(info):
    number_student = input("Input number of students: ")
    number = int(number_student)
    while number > 0:
        id = input("Input student's ID: ")
        if is_exist(info, id):
            name = input("Input student's name: ")
            dob = input("Input student's date of birth (dd/mm/yyyy): ")
            student = [name, dob]
            info[id] = student
            number = number - 1
        else:
            print(f"This id existed.")
    print(f"Add {number_student} students success.")

    def input_course_info(info):
        number_of_course = input("Enter number of course : ")
    number = int(number_of_course)
    while number > 0:
        id = input("Enter course ID : ")
        if is_exist(info, id):
            name = input("Enter course name : ")
            course = [name]
            info[id] = course
            number = number - 1
        else:
            print(f"This id existed.")
    print(f"Add {number_of_course} courses success.")


def list_of_student():
    print("{:20} | {:30} | {:30}".format("ID", "Name", "Date of Birth"))
    for key in student_info:
        print("{:20} | {:30} | {:30}".format(key, student_info[key][0], student_info[key][1]))


def list_of_course():
    print("{:15} | {:18}".format("ID", "Name"))
    for key in course_info:
        print("{:15} | {:18}".format(key, course_info[key][0]))


def list_course_with_mark():
    i = 0
    print("{:20} | {:30} | {:30}".format("ID", "Name", "Mark"))
    for key in course_with_mark:
        name = str(course_with_mark[key][i][i])
        mark = str(course_with_mark[key][i][i + 1])
        print("{:20} | {:30} | {:30}".format(key, name, mark))


def add_mark_to_course(course_mark, student, course):
    input_course = input("Input a course's ID wanted to add marks: ")
    for k_e_y in course:
        if k_e_y == input_course:
            course_mark[input_course] = []
            for key in student:
                student_mark = input(f"Input student {key} / {student[key][0]}'s mark: ")
                course_mark[input_course].append([student[key][0], student_mark])
            break
        if k_e_y not in course:
            print("Invalid course name!")


def is_empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False


def is_exist(dictionary, id):
    if id in dictionary:
        return True
    return False


print("Welcome To Student Management Program!")
while not end:
    print("-----------menu----------")
    print("[1] Add Courses")
    print("[2] Add Students")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show a course with marks")
    print("[0] Exit")
    choice = input("Please choose an option: ")
    if choice == "1":
        input_student_info(info=student_info)
    elif choice == "2":
        input_course_info(info=course_info)
    elif choice == "3":
        empty = is_empty(student_info)
        if not empty:
            list_student()
        else:
            print("There are no students in class!")
    elif choice == "4":
        empty = is_empty(course_info)
        if not empty:
            list_course()
        else:
            print("There are no courses!")
    elif choice == "5":
        add_mark_to_course(course_with_mark, student_info, course_info)
    elif choice == "6":
        empty = is_empty(course_with_mark)
        if not empty:
            list_course_with_mark()
        else:
            print("There are no courses have mark!")
    elif choice == "0":
        end = True
    else:
        print(f"{choice} is an invalid input!")