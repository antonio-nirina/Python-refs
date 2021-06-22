from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import status
from app.entities.data import Data

def response_success(data:List[Data]):
    items = {
        "code": status.HTTP_200_OK,
        "message":"success",
        "data":data
    }
    
    return jsonable_encoder(items)



