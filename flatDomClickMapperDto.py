import json
from types import SimpleNamespace
from getInfoFromWebsites import GetInfoFromWebsites


responseString = GetInfoFromWebsites().getCianFlatsInfo()

class FlatCianMapperDto:
    def flatCianMapperDto(self, responseString):
        x = json.loads(responseString, object_hook=lambda d: SimpleNamespace(**d))
        offersCount = x.data.count
        print(offersCount)
    else:
        responseString = "Ошибка:" + response.status_code
    return responseString



