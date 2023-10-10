# CLASS
class Teacher :
    def __init__(self, username, idno, course, is_on_probation):
        self.username = username
        self.idno = idno
        self.course = course
        self.is_on_prob = is_on_probation

    def greetFromTeacher(self):
        print("Hello from teacher")