from abc import ABCMeta, abstractmethod
from app.infrastructure.view_model.data_view_model import GetDataResponse


class AbstractGetDataUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self,ulr:str) -> GetDataResponse:
        raise NotImplementedError()