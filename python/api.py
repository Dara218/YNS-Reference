from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = [
    {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Wick',
        'course' : 'BSIT',
        'birthday': '10-21-2000'
    },
    {
        'id': 2,
        'first_name': 'Jane',
        'last_name': 'Doe',
        'course' : 'BSIS',
        'birthday': '03-21-2000'
    }
]

class StudentPost(BaseModel):
    id: int
    first_name: str
    last_name: str
    course: str
    birthday: str

class StudentUpdate(BaseModel):
    id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    course: Optional[str] = None
    birthday: Optional[str] = None

# Get all students
@app.get('/')
def index():
    return students

# Get a single student
@app.get('/student/{student_id}')
def get_student(student_id: int):
        student = next((student for student in students if student['id'] == student_id), None)

        if student is None:
            return 'Student not found'
        
        return student

# Store a student
@app.post('/store-student')
def store_student(newStudent: StudentPost):
    student = next((student for student in students if student['id'] == newStudent.id), None)
    
    if student:
        return 'Student ID already exists'
    
    students.append(newStudent)
    return newStudent

# Update a student
@app.put('/update-student/{student_id}')
def update_student(student_id: int, updatedStudent: StudentUpdate):
    student = next((student for student in students if student['id'] == student_id), None)
    # return student['first_name']

    if student not in students:
        return 'Student not found.'
    
    if updatedStudent.first_name: student['first_name'] = updatedStudent.first_name
    if updatedStudent.last_name: student['last_name'] = updatedStudent.last_name
    if updatedStudent.course: student['course'] = updatedStudent.course
    if updatedStudent.birthday: student['birthday'] = updatedStudent.birthday
    
    return updatedStudent

# Delete a student
@app.delete('/delete-student/{student_id}')
def delete_student(student_id : int):
    index_of_student = next((index for index, student in enumerate(students) if student['id'] == student_id), None)

    if index_of_student is None:
        return 'Student not found.'
    
    del students[index_of_student]
    return 'Student has been deleted.'



# from fastapi import FastAPI, Path
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# students = {
#     1: { 'name': 'john doe', 'age': 22, 'class': '3rd year' }
# }

# @app.get('/')
# def index():
#     return students

# @app.get('/get-student/{student_id}')
# def getStudent(student_id: int = Path(description="ID of the student", gt=0, lt=10)):
#     return students[student_id]

# @app.get("/get-by-student-name")
# def getStudentByName(*, student_name: str, test: Optional[int] = None):
#     for student_id in students:
#         if students[student_id]['name'] == student_name:
#             return students[student_id]
#         return { 'data': 'Not found.' }
    
# class Student(BaseModel):
#     name: str
#     age: int
#     year: str

# class UpdateStudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     year: Optional[int] = None

# @app.post('/store-student/{student_id}')
# def storeStudent(student_id : int, student: Student):
#     if student_id in students:
#         return { 'data': 'student id already exists.' }
    
#     students[student_id] = student
#     return student

# @app.put('/update-student/{student_id}')
# def updateStudent(student_id: int, student: UpdateStudent):
#     if student_id not in students:
#         return {'data': 'Student not found.'}
    
#     if student.name != None: #if student.name has a value
#         students[student_id].name = student.name
    
#     if student.age != None: #if student.age has a value
#         students[student_id].age = student.age

#     if student.year != None: #if student.year has a value
#         students[student_id].year = student.year

#     return student

# @app.delete('/delete-student/{student_id}')
# def deleteStudent(student_id : int):
#     if student_id not in students:
#         return { 'data': 'Student not found' }

#     del students[student_id]
#     return { 'Message' : 'Student has been deleted.' }