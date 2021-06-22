from pydantic import BaseModel


class InputModel(BaseModel):
    url: str