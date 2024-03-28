from fastapi import FastAPI, Request, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from database import schemas
from users.db import create_db_and_tables, User
from users.schemas import UserRead, UserCreate, UserUpdate
from users.users import fastapi_users, auth_backend, current_active_user
from database import models
from database.database import engine, SessionLocal
from loguru import logger

models.Base.metadata.create_all(bind=engine)

# logs
logger.add("logs/logs.csv",
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
           level="INFO",
           rotation="200 MB",
           compression="zip")

app = FastAPI(docs_url="/api/docs", openapi_url='/api/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/storage", StaticFiles(directory="storage"), name="storage")


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/api/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/api/users",
    tags=["users"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    logger.info(f'{request.url}')
    return response


@app.get("/api/")
def read_root():
    logger.info(f'Hello world')
    return {"Hello": "World"}


@app.post("/api/upload-model")
async def upload_file(request: Request,
                      file: UploadFile = File(...),
                      skybox_image: UploadFile = File(None),
                      env_image: UploadFile = File(None),
                      db: Session = Depends(get_db),
                      user: User = Depends(current_active_user)):

    if not file.filename.endswith('.glb'):
        logger.warning("No valid format")
        raise HTTPException(status_code=422, detail="No valid file format")

    if skybox_image:
        if not skybox_image.filename.endswith('.hdr') and not skybox_image.filename.endswith('.jpg'):
            logger.warning("No valid skybox image format")
            raise HTTPException(status_code=422, detail="No valid skybox image format")

    if env_image:
        if not env_image.filename.endswith('.jpg'):
            logger.warning("No valid env image format")
            raise HTTPException(status_code=422, detail="No valid env image format")

    from database.crud_path import create_path
    from utils.load_data import load_data

    load_data(
            file,
            skybox_image,
            env_image
        )

    url = f"{str(request.url)[:-len(request.url.path)]}:90/storage/{file.filename}"

    url_skybox_image = f"{str(request.url)[:-len(request.url.path)]}:90/storage/{skybox_image.filename}" if skybox_image else None

    url_env_image = f"{str(request.url)[:-len(request.url.path)]}:90/storage/{env_image.filename}" if env_image else None

    path_data = schemas.Path(
        path_model=url,
        url_skybox_image=url_skybox_image,
        url_env_image=url_env_image
    )

    create_path(db=db, schem_path=path_data)
    logger.info(f"Create new model with path {url}")
    return {
        "path": url,
        "path_skybox_image": url_skybox_image,
        "path_env_image": url_env_image
    }


@app.get("/api/models")
async def get_models(db: Session = Depends(get_db)):
    from database.crud_path import get_paths
    logger.info("Get models")
    return {"models": get_paths(db)}


@app.get('/api/delete-model')
async def delete_model(path_id: int, db: Session = Depends(get_db), user: User = Depends(current_active_user)):
    from database.crud_path import delete_path, get_paths
    delete_path(db, path_id)
    logger.info(f"Delete model with id {path_id}")
    return get_paths(db)


@app.get('/api/model')
async def delete_model(path_id: int, db: Session = Depends(get_db)):
    from database.crud_path import get_path
    logger.info(f"Get model with id {path_id}")
    return get_path(db, path_id)


@app.get("/api/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

