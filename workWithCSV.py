import csv
from flatDto import flatDto

class workWithCSV:
    def write_info_to_csv_file(self, file_name_csv: str, flats_info: list[flatDto]):
        flat_info = []
        with open(file_name_csv + ".csv", "a", newline="", encoding="utf-8") as file_csv:
            writer = csv.writer(file_csv, delimiter=",")
            for flat_info_dto in flats_info:
                flat_info = flat_info_dto.convert_dto_to_list()
                writer.writerow(flat_info)

    def read_multi_status_from_csv_file(self, file_name_csv: str) -> set:
        multi_ids = set()
        flat_similar_count_all = 0
        with open(file_name_csv + ".csv", "r", newline="", encoding="utf-8") as file_csv:
            csv_reader = csv.reader(file_csv)
            column_flat_offer_id = 12
            column_flat_similar_status = 13
            column_flat_similar_count = 14
            for flat_info_row in csv_reader:
                similar_status = bool(flat_info_row[column_flat_similar_status])
                if similar_status == True:
                    multi_id = int(flat_info_row[column_flat_offer_id])
                    flat_similar_count_all = flat_similar_count_all + int(flat_info_row[column_flat_similar_count])
                    multi_ids.add(multi_id)
            print(multi_ids)
            print(flat_similar_count_all)
        return multi_ids


    def write_info_to_txt_file(self, file_name_txt: str, error_pages: list[int]):
        with open(file_name_txt + ".txt", "a", newline="") as file_txt:
            writer = csv.writer(file_txt)
            for error_page in error_pages:
                file_txt.write(str(error_page) + "\n")

# n = workWithCSV()
# n.read_multi_status_from_csv_file("cian")

