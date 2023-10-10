# CLASS

from TeacherClass import Teacher

class Student(Teacher):
    def __init__(self, username, idno, course, is_on_probation):
        self.username = username
        self.idno = idno
        self.course = course
        self.is_on_prob = is_on_probation

    def greet(self):
        print("Hello from student named " + self.username)

# student1 = Student('sydney', 201911143, 'BSIS', False)
# student1.greet()