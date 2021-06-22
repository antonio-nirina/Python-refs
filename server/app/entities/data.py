import dataclasses


@dataclasses.dataclass(frozen=True)
class Data:
    name_application: str
    version: str
    number_download: int
    date_release: str
    description: str
    logo:str