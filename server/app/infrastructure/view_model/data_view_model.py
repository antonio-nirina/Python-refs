import dataclasses

from app.entities.data import Data


@dataclasses.dataclass
class GetDataResponse:
    data: Data