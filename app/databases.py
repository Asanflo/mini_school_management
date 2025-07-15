from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# URL de connexion SQLite (tu peux changer facilement pour PostgreSQL/MySQL)
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"


# Créer l'engine SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # SQLite only
)

# Session locale : une session = transaction DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pour créer les tables si besoin :
def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()