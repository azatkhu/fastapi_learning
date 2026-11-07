from app.data.db import students
from app.data.model import Student


def get_student_by_id(id: int) -> None|Student:
    
    for student in students:
        if student.id == id:
            
            return student
        
    return None

def get_students():
    
    return students
