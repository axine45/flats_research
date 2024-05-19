import requests

class flatDto:
    def __init__(self, flat_info: list):
        self.flat_jk = flat_info[0]
        self.flat_address = flat_info[1]
        self.flat_price = flat_info[2]
        self.flat_total_area = flat_info[3]
        self.flat_price_per_area = flat_info[4]
        self.flat_floor_number = flat_info[5]
        self.flat_rooms_count = flat_info[6]
        self.flat_decoration = flat_info[7]
        self.flat_deadline_year = flat_info[8]
        self.flat_deadline_quarter = flat_info[9]
        self.flat_developer_jk_id = flat_info[10]
        self.flat_sale_from_developer = flat_info[11]
        self.flat_offer_id = flat_info[12]
        self.flat_similar_status = flat_info[13]
        self.flat_similar_count = flat_info[14]

    def convert_dto_to_list(self) -> list:
        flat_info = []
        flat_info = [self.flat_jk, self.flat_address, self.flat_price, self.flat_total_area, self.flat_price_per_area,
                     self.flat_floor_number, self.flat_rooms_count, self.flat_decoration, self.flat_deadline_year,
                     self.flat_deadline_quarter, self.flat_developer_jk_id, self.flat_sale_from_developer,
                     self.flat_offer_id, self.flat_similar_status, self.flat_similar_count]
        return flat_info


