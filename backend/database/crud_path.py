import pymysql.err
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_paths(db: Session):
    return db.query(models.Path).all()


def create_path(db: Session, schem_path: schemas.Path):
    try:
        db_path = models.Path(path=schem_path)
        db.add(db_path)
        db.commit()
        db.refresh(db_path)
    except Exception:
        return None

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item