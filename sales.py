import csv
import pycountry


FILE_PATH = '10000 Sales Records.csv'


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

def read_csv():
    with open(FILE_PATH, "r") as f_obj:
        csv_reader(f_obj)

def convert_to_iso(country):
    iso_code = pycountry.countries.search_fuzzy(country)
    iso_code = iso_code[0]
    return iso_code.alpha_2


if __name__ == "__main__":

    print(convert_to_iso('USA'))
    read_csv()


