import re

class DataHandler:

    @staticmethod
    def CheckEmptyHandler(data)->str:
        if data:
            return data.get_text()
        else:
            return ""

    @staticmethod
    def DownloadHandler(data:str)->str:
        return re.split(" ", data)[0]

    @staticmethod
    def DateReleaseHandler(data:str)->str:
        return re.sub(r'(\(|\))',"",data)