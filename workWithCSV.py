import csv
from flatDto import flatDto

class workWithCSV:
    def writeIfoToCSVFile(self, fileNameCSV: str, flats_info: list[flatDto]):
        flat_info = []
        with open(fileNameCSV + '.csv', 'a', newline='') as fileCSV:
            writer = csv.writer(fileCSV)
            for flat_info_dto in flats_info:
                flat_info = flat_info_dto.convert_dto_to_list()
                writer.writerow(flat_info)


# rowList = [['newFlat', '1111', '32', '4'], ['newFlat1', 'Россия', '2024', '12']]
# n = workWithCSV()
# n.writeIfoToCSVFile('testCSV', rowList)

