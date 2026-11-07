from pydantic import BaseModel


class Student(BaseModel):
    
    id: int
    name: str
    inf_score: int
    math_score: int
    history_score: int
    