import json
import requests
from types import SimpleNamespace
from getInfoFromWebsites import GetInfoFromWebsites
from flatDto import flatDto


class FlatCianMapperDto:
    def __init__(self, get_info_from_web: GetInfoFromWebsites):
        self.get_info_from_web = get_info_from_web
    def flat_cian_mapper_dto(self, response_string: str) -> list[flatDto]:
        flats_info = []
        flat_info = []
        x = json.loads(response_string, object_hook=lambda d: SimpleNamespace(**d))
        offers_info = x.data.offersSerialized
        for offer in offers_info:
            jk = offer.geo.jk.displayName
            address = self.get_address(offer)
            price = offer.bargainTerms.price
            total_area = float(offer.totalArea)
            price_per_area = round(price/total_area)
            floor_number = offer.floorNumber
            rooms_count = self.get_rooms_count(offer)
            decoration = offer.decoration
            deadline_quarter_int, deadline_year = self.get_deadline_year_quarter(offer)
            developer_jk_id = offer.geo.jk.id
            sale_from_developer = offer.fromDeveloper
            offer_id = offer.id
            if offer.similar is not None:
                similar_status = True
                similar_count = offer.similar.count
            else:
                similar_status = False
                similar_count = 0
            flat_info = flatDto([jk, address, price, total_area, price_per_area, floor_number, rooms_count, decoration,
                                 deadline_year, deadline_quarter_int, developer_jk_id, sale_from_developer, offer_id,
                                 similar_status, similar_count])
            flats_info.append(flat_info)
        return flats_info


    def get_rooms_count(self, offer):
        rooms_count = ""
        if hasattr(offer, "roomsCount"):
            rooms_count = offer.roomsCount
        return rooms_count

    def get_deadline_year_quarter(self, offer):
        deadline_year = ""
        deadline_quarter_int = ""
        if offer.newbuilding.house is not None:
            deadline_year = offer.newbuilding.house.finishDate.year
            deadline_quarter_int = offer.newbuilding.house.finishDate.quarter
            deadline_date = (offer.newbuilding.house.finishDate.year, offer.newbuilding.house.finishDate.quarter)
        elif offer.building.deadline is not None:
            deadline_year = offer.building.deadline.year
            deadline_quarter = offer.building.deadline.quarter
            deadline_quarter_int = 0
            if deadline_quarter == "first":
                deadline_quarter_int = 1
            elif deadline_quarter == "second":
                deadline_quarter_int = 2
            elif deadline_quarter == "third":
                deadline_quarter_int = 3
            elif deadline_quarter == "fourth":
                deadline_quarter_int = 4
            deadline_date = (deadline_year, deadline_quarter_int)
        return deadline_quarter_int, deadline_year

    def get_address(self, offer):
        geo_address = offer.geo.address
        address = ""
        street = ""
        house = ""
        for val in geo_address:
            if val.type == "street":
                street = val.fullName
            if val.type == "house":
                house = val.fullName
        if street != "" and house != "":
            address = street + ", " + house
        elif street != "" and house == "":
            address = street
        return address
