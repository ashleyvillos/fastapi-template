from typing import Any
from pydantic import BaseModel, ConfigDict

class Response(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    status: int
    message: str
    response: Any = {}