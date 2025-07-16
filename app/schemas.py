from pydantic import BaseModel, EmailStr
from typing import List, Optional

class NoteBase(BaseModel):
    course_id: int
    note: float

class NoteCreate(NoteBase):
    student_id: int

class NoteRead(NoteBase):
    id: int

    class Config:
        from_attributes = True

class EtudiantBase(BaseModel):
    name: str
    email: EmailStr

class EtudiantCreate(EtudiantBase):
    pass

class EtudiantRead(EtudiantBase):
    id: int
    notes: List[NoteRead] = []

    class Config:
        from_attributes = True
        
class EtudiantUpdate(EtudiantBase):
    name: str
    email: EmailStr
    

class CoursBase(BaseModel):
    title: str
    description: Optional[str] = None

class CoursCreate(CoursBase):
    pass

class CoursRead(CoursBase):
    id: int
    notes: List[NoteRead] = []

    class Config:
        from_attributes = True