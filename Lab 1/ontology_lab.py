# Part A: Define Ontology Classes

class Student:
    def __init__(self, name, student_id, major, year):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.year = year

class Lecturer:
    def __init__(self, name, lecturer_id, department, courses): 
        self.name = name
        self.lecturer_id = lecturer_id
        self.department = department
        self.courses = courses

class Course:
    def __init__(self, course_name, course_code, credits, lecturer):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.lecturer = lecturer

class Department:
    def __init__(self, department_name, faculty, head_of_department):
        self.department_name = department_name  # FIXED: was 'deparment_name'
        self.faculty = faculty
        self.head_of_department = head_of_department

class Classroom:
    def __init__(self, room_number, building, capacity):
        self.room_number = room_number
        self.building = building
        self.capacity = capacity


# Part B: Create Ontology Objects

s1 = Student("Aisha", "672727", "Software Engineering", 3)
s2 = Student("Alvin", "672728", "Applied Computer Science", 2)
s3 = Student("Siti", "672729", "Psychology", 1)
s4 = Student("Kiprop", "672730", "Cybersecurity", 4)
s5 = Student("John", "672731", "International Business Administration", 3)
s6 = Student("Wanjiku", "672732", "Pharmacy", 2)

l1 = Lecturer("Austin", "L001", "School of Technology", "Applied Computer Science")
l2 = Lecturer("Maggie", "L002", "School of Business", "International Business Administration")
l3 = Lecturer("Dr. Smith", "L003", "School of Humanities and Social Sciences", "Psychology")
l4 = Lecturer("Prof. Johnson", "L004", "School of Technology", ["Software Engineering", "Cybersecurity"]) 
l5 = Lecturer("prof. Rao", "L005", "School of Science", "Pharmacy")

c1 = Course("Knowledge Based Systems", "APT3020", 3, "Austin")
c2 = Course("Principles of Accounting", "ACT1010", 3, "Maggie")
c3 = Course("Introduction to Psychology", "PSY1010", 3, "Dr. Smith")
c4 = Course("Programming with FrameWorks", "SWE3010", 3, "Prof. Johnson")
c5 = Course("Cybersecurity Fundamentals", "CYB3010", 3, "Prof. Johnson")
c6 = Course("Pharmacology", "PHA3010", 3, "prof. Rao")
c7 = Course("Database Management Systems", "DBMS2010", 3, "Dr. Sophie")

d1 = Department("School of Technology", "Faculty of Software Engineering and Applied Computer Science", "Dr. Sifuna")
d2 = Department("School of Business", "Faculty of Business Administration", "Dr. Mwangi")
d3 = Department("School of Humanities and Social Sciences", "Faculty of Psychology", "Prof. Njoroge")
d4 = Department("School of Technology", "Faculty of Data Science", "Dr. Sophie")
d5 = Department("School of Technology", "Faculty of Cybersecurity", "Dr. Kimani")
d6 = Department("School of Science", "Faculty of Pharmacy", "Dr. Karori")

r1 = Classroom("101", "Main Building", 50)
r2 = Classroom("202", "Science Block", 30)
r3 = Classroom("303", "Technology Wing", 40)
r4 = Classroom("404", "Business School", 25)
r5 = Classroom("505", "Humanities Block", 35)
r6 = Classroom("606", "Engineering Building", 45)


# Part C: Create Relationships

enrollments = {
    "672727": ["APT3020", "SWE3010"],  
    "672728": ["ACT1010", "PSY1010"],  
    "672729": ["PSY1010", "PHA3010"],  
    "672730": ["CYB3010", "SWE3010"],  
    "672731": ["APT3020"],             
    "672732": ["PHA3010", "CYB3010"]   
}

completed_courses = {
    "672727": ["SWE3010"],             
    "672728": ["ACT1010", "PSY1010"],  
    "672729": ["PSY1010"],             
    "672730": ["CYB3010", "SWE3010"],  
    "672731": ["APT3020"],             
    "672732": ["PHA3010", "CYB3010"]   
}

course_assignments = {
    "APT3020": "Austin",
    "ACT1010": "Maggie",
    "PSY1010": "Dr. Smith",
    "SWE3010": "Prof. Johnson",
    "CYB3010": "Prof. Johnson",
    "PHA3010": "prof. Rao"
}

course_departments = {
    "APT3020": "School of Technology",
    "ACT1010": "School of Business",
    "PSY1010": "School of Humanities and Social Sciences",
    "SWE3010": "School of Technology",
    "CYB3010": "School of Technology",
    "PHA3010": "School of Science"
}

course_prerequisites = {
    "APT3020": ["DBMS2010"],   
    "ACT1010": [],
    "PSY1010": [],
    "SWE3010": [],
    "CYB3010": [],
    "PHA3010": []
}

course_classrooms = {
    "APT3020": "101",
    "ACT1010": "202",
    "PSY1010": "303",
    "SWE3010": "404",
    "CYB3010": "505",
    "PHA3010": "606"
}


# Part D: Reasoning Functions

def get_student_courses(student_id):
    return enrollments.get(student_id , []) 

def get_course_lecturer(course_code):
    return course_assignments.get(course_code, None)

def get_course_department(course_code):
    return course_departments.get(course_code, None)

def get_courses_in_department(department_name):
    return [code for code, dept in course_departments.items() if dept == department_name]

def get_student_name(student_id):
    for student in [s1, s2, s3, s4, s5, s6]:
        if student.student_id == student_id:
            return student.name
    return None

def get_students_in_course(course_code):
    return [sid for sid, courses in enrollments.items() if course_code in courses]

def can_take_course(student_id, course_code):
    # Safety checks
    if student_id not in completed_courses:
        print("Student not found or no completed courses recorded.")
        return False
    if course_code not in course_prerequisites:
        print("Course not found.")
        return False

    required = course_prerequisites[course_code]
    completed = completed_courses[student_id]

    missing = [prereq for prereq in required if prereq not in completed]

    if missing:
        print(f"No. Missing prerequisite: {missing[0]}")
        return False
    else:
        print("Yes. All prerequisites met.")
        return True


# Main Execution (Output)

if __name__ == "__main__":
    print(f"Courses taken by {s1.name}:")
    for course in get_student_courses(s1.student_id):
        print(f"- {course}")

    print("\nLecturer teaching APT3020:")
    print(f"- {get_course_lecturer('APT3020')}")

    print("\nCourses in School of Technology:")
    for course in get_courses_in_department("School of Technology"):
        print(f"- {course}")

    print("\nStudents taking APT3020:")
    for student_id in get_students_in_course("APT3020"):
        print(f"- {get_student_name(student_id)}")

    print("\nCan Aisha take APT3020?")
    can_take_course(s1.student_id, "APT3020")   