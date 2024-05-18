import json
import time
from getInfoFromWebsites import GetInfoFromWebsites
from flatCianMapperDto import FlatCianMapperDto
from workWithCSV import workWithCSV


class FlatExportService:
    def export_flat_info_from_cian(self):
        offer_info = GetInfoFromWebsites()
        mapper_dto = FlatCianMapperDto(offer_info)
        writer_to_csv = workWithCSV()
        cian_csv = "cian"
        offers_page_count = offer_info.get_cian_offers_page_count()
        for page in range(1, offers_page_count+1):
            offer_page_info = offer_info.get_cian_offers_info(page)
            flats_info = mapper_dto.flat_cian_mapper_dto(offer_page_info)
            writer_to_csv.writeIfoToCSVFile(cian_csv, flats_info)
            print(page)
            time.sleep(5)


    def export_flat_info_from_domclick(self):
        pass

if __name__ == '__main__':
    flat_export = FlatExportService()
    flat_export.export_flat_info_from_cian()
