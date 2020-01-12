from iso3166 import countries

not_founded_from_csv = []
not_founded_from_iso3166 = []

HARDCODED_NOT_FOUND_CODES = {
    'Cape Verde': "CV",
    'Moldova': "MD",
    'Tunisia': "TN",
    'Laos': "LA",
    'Samoa': "WS",
    'Vietnam': "VN",
    'Swaziland': "SZ",
    'The Gambia': "GM",
    'Antigua and Barbuda': "AG",
    'Vatican City': "VA",
    'Czech Republic': "CZ",
    'Republic of the Congo': "CD",
    'The Bahamas': "BS",
    'Syria': "SY",
    'Tanzania': "TZ",
    'East Timor': "TP",
    'Russia': "RU",
    'Federated States of Micronesia': "FM",
    "Cote d'Ivoire": "CI",
    'South Korea': "KR",
    'Democratic Republic of the Congo': "CD",
    'Saint Kitts and Nevis': "KN",
    'Iran': "IR",
    'United Kingdom': "GB",
    'Brunei': "BN",
    'Macedonia': "MK",
    'Seychelles': "SC",
    'North Korea': "KP",
    'Mauritius': "MU",
}

def find_country_code(country_name):
    try:
        _country_code = countries.get(country_name).alpha2
    except KeyError:
        _country_code = HARDCODED_NOT_FOUND_CODES.get(country_name)

    return _country_code


#print(find_country_code("Democratic Republic of the Congo"))