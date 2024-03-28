from typing import Optional

from pydantic import BaseModel


class Path(BaseModel):
    path_model: str
    url_skybox_image: Optional[str] = None
    url_env_image: Optional[str] = None
