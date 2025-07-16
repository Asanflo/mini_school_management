from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models
from app.databases import get_db

router = APIRouter()

# -- CRUD Etudiant -- 

@router.post("/etudiants/", response_model=schemas.EtudiantRead)
def create_etudiant(etudiant: schemas.EtudiantCreate, db: Session = Depends(get_db)):
    db_etudiant = db.query(models.Etudiant).filter(models.Etudiant.email == etudiant.email).first()
    if db_etudiant:
        raise HTTPException(status_code=400, detail="Email deja existant")
    
    new_etudiant = models.Etudiant(name=etudiant.name, email=etudiant.email)
    db.add(new_etudiant)
    db.commit()
    db.refresh
    return new_etudiant

@router.get("/etudiants/", response_model=List[schemas.EtudiantRead])
def list_etudiants(db: Session = Depends(get_db)):
    return db.query(models.Etudiant).all()


@router.get("/etudiants/{etudiant_id}", response_model=schemas.EtudiantRead)
def get_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id==etudiant_id).first()
    if not etudiant:
        raise HTTPException(status_code=404, detail="Etudiant non trouve")
    return etudiant

@router.put("/etudiants/{etudiant_id}", response_model=schemas.EtudiantRead)
def update_etudiant(etudiant_id: int, etudiant_up: schemas.EtudiantUpdate, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id==etudiant_id).first()
    if not etudiant:
        raise HTTPException(status_code=404, detail="Etudiant non trouve")
    etudiant.name = etudiant_up.name
    etudiant.email = etudiant_up.email
    db.commit()
    db.refresh(etudiant)
    return etudiant   

@router.delete("/etudiants/{etudiant_id}")
def delete_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.id==etudiant_id).first()
    if not etudiant:
        raise HTTPException(status_code=404, detail="Etudiant non trouve") 
    db.delete(etudiant)
    db.commit()
    return {"detail":"Etudiant supprime"}