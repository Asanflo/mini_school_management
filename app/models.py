from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Etudiant(Base):
    """Model concernant les etudiants"""
    __tablemame__ = "etudiants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    
    
class Cours(Base):
    """Model pour les cours"""
    
    __tablename__ = "cours"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    
class Note(Base):
    """Model pour les notes en fonction du cours et de l'etudiant"""
    
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    etudiant_id = Column(Integer, ForeignKey("Etudiant.id"))
    course_id = Column(Integer, ForeignKey("Cours.id"))
    note = Column(Float, nullable=False)
    
    student = relationship("Etudiant", back_populates="grades")
    cours = relationship("Cours", back_populates="grades")