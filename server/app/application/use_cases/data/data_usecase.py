from typing import Dict,Optional
from bs4 import BeautifulSoup
import urllib.request

from app.application.use_cases.data.data_usecase_interface import AbstractGetDataUseCase
from app.infrastructure.view_model.data_view_model import GetDataResponse
from app.entities.data import Data
from app.infrastructure.service.data_handler import DataHandler


class GetDataUseCase(AbstractGetDataUseCase):
    def handle(self,url:str)->GetDataResponse:
        # type: ignore
        page = urllib.request.urlopen(url)
        bs = BeautifulSoup(page,"html.parser")
        download:str = bs.find("span",{"class":"mini-stats__Info-sc-188veh1-6"}).get_text()
        version:str = bs.find("div",{"class":"mini-versions__LatestVersion-sc-19sko2j-5"})
        name:str = bs.find("h1",{"class":"header-desktop__AppName-xc5gow-5"})
        logo:str = bs.find("img",{"class":"responsive-image__Image-o4o8ec-1"})['src']
        date_release:str    = bs.find("div",{"class":"mini-versions__VersionDate-sc-19sko2j-6"}).get_text()
        description:str     = bs.find("h2",{"class":"header-desktop__AppNameH2-xc5gow-6"})
        print(description)
        newName:str         = DataHandler.CheckEmptyHandler(name)
        newLogo:str         = logo if(logo) else ""
        newVersion:str      = DataHandler.CheckEmptyHandler(version)
        newDescription:str  = DataHandler.CheckEmptyHandler(description)
        newDownload:str     = DataHandler.DownloadHandler(download)
        newDateRelease:str  = DataHandler.DateReleaseHandler(date_release)
        
        return Data(name_application=newName,
            version=newVersion,
            number_download=newDownload,
            date_release=newDateRelease,
            logo=newLogo,
            description=newDescription
            )

