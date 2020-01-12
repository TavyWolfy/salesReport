import csv
import sales_fix_iso


ISO_FILE_PATH = '10000 Sales Records.csv'
OUTPUT_FILE_PATH = 'SQL_Records.txt'


def save_to_file(name, data):
    with open(name, "w") as f_obj:
        for row in data:
            f_obj.write(row + "\n")


def csv_dict_reader(file_obj):
    sales_per_country = {}
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        #Достаем и переводим страну в формат ISO 3166
        country = line["Country"]
        country = country.strip()  # clear whitespaces
        country_code = sales_fix_iso.find_country_code(country)
        # print('country_code: ', country_code, "for country: ", country)
        #Достаем продажи
        revenue = float(line["Total Revenue"])
        if country_code in sales_per_country:
            sales_per_country[country_code] += revenue
        else:
            sales_per_country[country_code] = revenue

    make_SQL_reports(sales_per_country)



def read_csv():
    with open(ISO_FILE_PATH, "r") as f_obj:

        csv_dict_reader(f_obj)


def to_sql(country_iso_code, total_sales):
    q = "INSERT INTO sales_reports (country_iso_code, total_sales) VALUES ({COUNTRY_ISO_CODE}, {TOTAL_SALES});".format(COUNTRY_ISO_CODE =country_iso_code, TOTAL_SALES=total_sales)
    return q

def make_SQL_reports(codes_and_sales):
    reports = []
    for code, sale in codes_and_sales.items():
        # print(code, '->', sale)
        reports.append(to_sql(code, sale))
    save_to_file(OUTPUT_FILE_PATH, reports)


if __name__ == "__main__":

    read_csv()




