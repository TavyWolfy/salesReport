import csv
import pycountry
#from iso3166 import countries


FILE_PATH = '10000 Sales Records.csv'
counter = 0

def convert_to_iso(country):
    iso_code = '__'

    try:
        iso_code = pycountry.countries.search_fuzzy(country)
        #iso_code = pycountry.countries.lookup(country)
        iso_code = iso_code[0]
        return iso_code.alpha_2
    except LookupError:
        print('')
        """
        contrs_list = list(pycountry.countries)
        for c in contrs_list:
            if c.name in country:
                print("no_iso", c.alpha_2)
                iso_code = c.alpha_2
                return iso_code
        """
    return iso_code

def convert_to_iso_2(country):

    _country = countries.get(country)
    return _country.alpha2







def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    country_sales = {'country_iso_code': '', 'total_sales': 0 }
    units_sold = 0
    unit_price = 0
    countries = []
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        #Достаем и переводим страну в формат ISO 3166
        country = line["Country"]
        country_code = convert_to_iso(country)
        #Если это первая в списке страна
        #if countries
        print(country_code)
        #print(line["Units Sold"]),
        #print(line["last_name"])

def read_csv():
    with open(FILE_PATH, "r") as f_obj:
        #csv_reader(f_obj)
        csv_dict_reader(f_obj)




if __name__ == "__main__":

    #print(convert_to_iso('Bosnia and Herzegovina'))
    print(pycountry.countries.search_fuzzy(' Republic of the Congo'))
    pycountry.countries.get(alpha_2='DE')
    #print(convert_to_iso_2('Congo'))
    read_csv()



