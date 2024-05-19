import json
import time
from getInfoFromWebsites import GetInfoFromWebsites
from flatCianMapperDto import FlatCianMapperDto
from workWithCSV import workWithCSV


class FlatExportService:
    price_range = (10000000, 22000000)
    # rooms_area = {
    #     1: [(1, 37), (37, 42), (42, 48), (48, 150)],
    #     2: [(1, 56), (56, 60), (60, 64), (64, 69), (69, 150)],
    #     3: [(1, 87), (87, 150)],
    #     4: [(1, 150)]
    # }
    rooms_area = {
        1: [(36, 37)]
    }

    def export_flat_info_from_cian(self):
        error_pages_list = []
        set_multi_ids = set()
        offer_info = GetInfoFromWebsites()
        mapper_dto = FlatCianMapperDto(offer_info)
        writer_to_csv = workWithCSV()
        cian_csv = "cian"
        for key, values in self.rooms_area.items():
            for value in values:
                page = 1
                flats_info = self.get_cian_data(key, mapper_dto, offer_info, page, value, error_pages_list)
                while flats_info != []:
                    writer_to_csv.write_info_to_csv_file(cian_csv, flats_info)
                    print(page)
                    time.sleep(5)
                    page = page + 1
                    flats_info = self.get_cian_data(key, mapper_dto, offer_info, page, value, error_pages_list)
        writer_to_csv.write_info_to_txt_file("cian_error_pages", error_pages_list)
        set_multi_ids = writer_to_csv.read_multi_status_from_csv_file(cian_csv)
        for multi_id in set_multi_ids:
            for key, values in self.rooms_area.items():
                for value in values:
                    page = 1
                    flats_similar_info = self.get_cian_similar_data(key, mapper_dto, offer_info, page, value, error_pages_list, multi_id)
                    while flats_similar_info != []:
                        writer_to_csv.write_info_to_csv_file(cian_csv, flats_similar_info)
                        print(page)
                        time.sleep(5)
                        page = page + 1
                        flats_similar_info = self.get_cian_similar_data(key, mapper_dto, offer_info, page, value, error_pages_list, multi_id)
        writer_to_csv.write_info_to_txt_file("cian_error_pages", error_pages_list)


    def get_cian_data(self, key, mapper_dto, offer_info, page, value, error_pages_list):
        try:
            offer_page_info = offer_info.get_cian_offers_info(page, self.price_range, key, value)
            flats_info = mapper_dto.flat_cian_mapper_dto(offer_page_info)
        except Exception as err:
            time.sleep(60)
            error_pages_list.append(page)
            print(err)
            offer_page_info = offer_info.get_cian_offers_info(page, self.price_range, key, value)
            flats_info = mapper_dto.flat_cian_mapper_dto(offer_page_info)
        return flats_info

    def get_cian_similar_data(self, key, mapper_dto, offer_info, page, value, error_pages_list, multi_id):
        try:
            offer_page_info = offer_info.get_cian_multi_offers_info(page, self.price_range, key, value, multi_id)
            flats_info = mapper_dto.flat_cian_mapper_dto(offer_page_info)
        except Exception as err:
            time.sleep(60)
            error_pages_list.append(page)
            print(err)
            offer_page_info = offer_info.get_cian_multi_offers_info(page, self.price_range, key, value, multi_id)
            flats_info = mapper_dto.flat_cian_mapper_dto(offer_page_info)
        return flats_info

    def export_flat_info_from_domclick(self):
        pass


if __name__ == "__main__":
    flat_export = FlatExportService()
    flat_export.export_flat_info_from_cian()
    print("finish")
