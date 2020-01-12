import csv
import pycountry
import re
from iso3166 import countries, countries_by_name
import sales_fix_iso


FILE_PATH = '10000 Sales Records.csv'
FILE_PATH_test = 'not_founded_countries.txt'

def save_to_file(name, data):
    with open(name, "w") as f_obj:
        for row in data:
            f_obj.write(row + "\n")


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    test_list = []
    n_of_countries_in_csv = []
    country_sales = {'country_iso_code': '', 'total_sales': 0 }
    units_sold = 0
    unit_price = 0
    countries = []
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        #Достаем и переводим страну в формат ISO 3166
        country = line["Country"]
        country = country.strip()  # clear whitespaces

        n_of_countries_in_csv.append(country)

        country_code = sales_fix_iso.find_country_code(country)
        print('country_code: ', country_code, "for country: ", country)
        test_list.append(country_code)
        #if country_code:

        #Если это первая в списке страна
        #if countries
        #print(country_code + "  for " + country)
        #print(line["Units Sold"]),
        #print(line["last_name"])
    uniq_list = set(test_list)
    n_of_countries_in_csv = set(n_of_countries_in_csv)
    print('n_of_countries_in_csv: ', len(n_of_countries_in_csv))
    print('n of codes found: ', len(test_list))
    save_to_file("founded_countries.txt", uniq_list)


def read_csv():
    with open(FILE_PATH, "r") as f_obj:

        csv_dict_reader(f_obj)


def read_txt():
    with open(FILE_PATH_test, "r") as f:
        #print(f.readlines())
        lines = f.readlines()
        for line in lines:
            # Достаем и переводим страну в формат ISO 3166
             print(convert_to_iso_2(line))


#def to_sql(country_iso_code, total_sales):



if __name__ == "__main__":

    #print(convert_to_iso_2('Laos'))
    #read_txt()
    #print(pycountry.countries.search_fuzzy(' Republic of the Congo'))
    #pycountry.countries.get(alpha_2='DE')
    #print(convert_to_iso_2('Congo'))
    read_csv()
    #for c in countries:
        #findInDict("Republic of the Congo", c)
    #print(countries.get("Iran"))
    #print(findWholeWord("Congo")("Republic of the Congo"))
    #print(fuzzySearch("Republic of the Congo"))




