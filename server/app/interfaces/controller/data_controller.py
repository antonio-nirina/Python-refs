from fastapi import APIRouter,HTTPException

from app.application.use_cases.data.data_usecase import GetDataUseCase
from app.interfaces.serializers.serialize import response_success
from app.infrastructure.view_model.data_input_model import InputModel

data = APIRouter()

@data.post('/')
def root(input:InputModel):
    if not input.url:
        raise HTTPException(status_code=404, detail="Url not found")
    res = GetDataUseCase().handle(input.url)

    return response_success(res) 
