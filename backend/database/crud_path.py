from loguru import logger
from sqlalchemy.orm import Session

from . import models, schemas


def get_path(db: Session, path_id: int):
    try:
        return db.query(models.Path).filter(models.Path.id == path_id).first()
    except Exception as error:
        logger.critical(f'{error}')


def get_paths(db: Session):
    try:
        return db.query(models.Path).all()
    except Exception as error:
        logger.critical(f'{error}')


def delete_path(db: Session, path_id):
    try:
        path = db.query(models.Path).filter(models.Path.id == path_id).first()

        if path:
            db.delete(path)
            db.commit()
    except Exception as error:
        logger.critical(f'{error}')


def create_path(db: Session, schem_path: schemas.Path):
    try:
        db_path = models.Path(path=schem_path.path_model, path_skybox_image=schem_path.url_skybox_image, path_env_image=schem_path.url_env_image)
        db.add(db_path)
        db.commit()
        db.refresh(db_path)
    except Exception as error:
        logger.critical(f'{error}')
