import requests
import json
from types import SimpleNamespace
import time


class GetInfoFromWebsites:
    def __init__(self):
        self.map1 = {}

    def get_cian_offers_page_count(self, price_range: tuple, rooms_area_room: int, rooms_area_area: tuple) -> int:
        offers_page_count = 0
        url = "https://spb.cian.ru/cian-api/site/v1/offers/search/meta/"
        headers = {"Content-Type": "application/json"}
        data = {"_type": "flatsale",
                "building_status": {"type": "term", "value": 2},
                "engine_version": {"type": "term", "value": 2},
                "price": {"type": "range", "value": {"gte": price_range[0], "lte": price_range[1]}},
                "region": {"type": "terms", "value": [2]},
                "room": {"type": "terms", "value": [rooms_area_room]},
                "total_area": {"type": "range", "value": {"gte": rooms_area_area[0], "lte": rooms_area_area[1]}}
                }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            response_string = response.text
            x = json.loads(response_string, object_hook=lambda d: SimpleNamespace(**d))
            offers_count = x.data.count
            if offers_count != 0:
                offers_page_count = offers_count // 28 + 1
            print(offers_page_count)
        else:
            print("Ошибка: ", response.status_code)
        return offers_page_count

    def get_cian_offers_info(self, page: int, price_range: tuple, rooms_area_room: int, rooms_area_area: tuple) -> str:
        url = "https://api.cian.ru/search-offers/v2/search-offers-desktop/"
        headers = {"Content-Type": "application/json"}
        data = {"jsonQuery": {"_type": "flatsale",
                              "building_status": {"type": "term", "value": 2},
                              "engine_version": {"type": "term", "value": 2},
                              "page": {"type": "term", "value": page},
                              "price": {"type": "range", "value": {"gte": price_range[0], "lte": price_range[1]}},
                              "region": {"type": "terms", "value": [2]},
                              "room": {"type": "terms", "value": [rooms_area_room]},
                              "sort": {"type": "term", "value": "price_object_order"},
                              "total_area": {"type": "range", "value": {"gte": rooms_area_area[0], "lte": rooms_area_area[1]}}
                              }}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
            return str(response.status_code)


    def get_cian_multi_offers_info(self, page: int, price_range: tuple, rooms_area_room: int, rooms_area_area: tuple, multi_id: int) -> str:
        url = "https://api.cian.ru/search-offers/v2/search-offers-desktop/"
        headers = {"Content-Type": "application/json"}
        data = {"jsonQuery": {"_type": "flatsale",
                              "building_status": {"type": "term", "value": 2},
                              "engine_version": {"type": "term", "value": 2},
                              "page": {"type": "term", "value": page},
                              "price": {"type": "range", "value": {"gte": price_range[0], "lte": price_range[1]}},
                              "region": {"type": "terms", "value": [2]},
                              "room": {"type": "terms", "value": [rooms_area_room]},
                              "sort": {"type": "term", "value": "price_object_order"},
                              "total_area": {"type": "range", "value": {"gte": rooms_area_area[0], "lte": rooms_area_area[1]}},
                              "multi_id": {"type": "term", "value": multi_id}
                              }}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
            return str(response.status_code)

    def get_cian_jk_info(self, developer_jk_id: int) -> str:
        if developer_jk_id in self.map1:
            return self.map1[developer_jk_id]
        time.sleep(5)
        url = "https://api.cian.ru/newbuilding-search/v1/get-newbuildings-for-serp/"
        headers = {"Content-Type": "application/json"}
        data = {"jsonQuery": {"region": {"type": "terms", "value": [2]},
                              "newbuilding_id": {"type": "terms", "value": [developer_jk_id]}},
                "uri": "/newobjects/list?deal_type=sale&engine_version=2&offer_type=newobject&region=2",
                "subdomain": "spb",
                "offset": 0,
                "count": 25,
                "userCanUseHiddenBase": False}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            response_string = response.text
            # print(response_string)
        else:
            response_string = "Ошибка:", response.status_code
        self.map1[developer_jk_id] = response_string
        return response_string
