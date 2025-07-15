from pydantic import BaseModel
from typing import List, Optional

class NoteBase(BaseModel):
    course_id: int
    note: float

class NoteCreate(NoteBase):
    student_id: int

class NoteRead(GradeBase):
    id: int

    class Config:
        orm_mode = True

class EtudiantBase(BaseModel):
    name: str
    email: str

class EtudiantCreate(EtudiantBase):
    pass

class EtudiantRead(EtudiantBase):
    id: int
    notes: List[NoteRead] = []

    class Config:
        orm_mode = True

class CoursBase(BaseModel):
    title: str
    description: Optional[str] = None

class CoursCreate(CoursBase):
    pass

class CourseRead(CourseBase):
    id: int
    notes: List[NoteRead] = []

    class Config:
        orm_mode = True