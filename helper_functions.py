from global_vars import *

# helper functions
def intN(text=""):
    """same as python int() but here it returns None when
    the argument is empty string

    Args:
        text (str): a string of number or empty string

    Returns:
        number (int)
    """
    try:
        return int(text)
    except:
        return None


def convert_str_to_int(text=""):
    """convert string to number, when the int() function does not work
    Some numbers in the website are like 3,589 which will not be converted
    to 3589 when using int() to the string. This function will help to do
    that.

    Args:
        text (str): a string of number

    Returns:
        number (int)

    Example:
        >>> convert_str_to_int(58)
        58
        >>> convert_str_to_int(3,597)
        3597
        >>> convert_str_to_int(1,000,000)
        1000000
    """
    tokens = list(reversed(text.split(",")))
    number = 0
    if len(tokens) == 0:
        return 0
    for i in range(len(tokens)):
        number += (10**(3*i))*int(tokens[i])  # because of 3 digit split
    return number


def merge_years_for_two_list(l1, l2):
    """a function to merge two list of list where the last element of
    first list is equal to first element of the second list

    Args:
        l1 (list): first list
        l2 (list): second list

    Returns:
        l (list): merged list of l1 and l2

    Example:
            >>> merge_years_for_two_list(
                    ['2013', '2014', '2015'],['2015', '2016', '2019']
                    )
            ['2013', '2014', '2015', '2016']
    """
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    if l1[-1] == l2[0]:
        result = l1 + l2[1:]
    else:
        result = l1 + [''] + l2
    return result


def merge_years_for_lists_of_list(list_of_lists):
    """merge list of lists when last element of each list matches with the
    fist element of the next list

    Args:
        list_of_lists (list): a list of lists which will be merged

    Returns:
        l (list): a merged list of elements in lists of the list

    Example:
        >>> merge_years_for_lists_of_list(
                [["2010", "2012"], ["2012", "2014"], ["2014", "2020"]]
                )
        ["2010", "2012", "2014", "2020"]
    """
    if len(list_of_lists) < 2:
        return list_of_lists[0]
    result = []
    for i in range(len(list_of_lists)):
        result = merge_years_for_two_list(result, list_of_lists[i])
    return result


def separate_affiliations_from_pos(text):
    """A function to find affiliation position from a special type of string

    Args:
        text (str): a text which has forms of
        POSTION,AFFILIATION or AFFILIATION

    Returns:
        pos (str)
    """
    pos = text.split(",")[0].upper()
    if pos in AFFILIATIONS_POSITIONS:
        return pos
    else:
        return ''

def get_country_id(text):
    """returns country id from country name in the text,
    it is supposed the country's name is avaialable in text

    Args:
        text (str)

    Returns:
        (str): a text with length 2"""

    textc = text.lower().strip()
    if "United States".lower() in textc:
        return "US" 
    if "China".lower() in textc:
        return "CN"
    if "French Polynesia".lower() in textc:
        return "PF"
    if "French Southern Territories".lower() in textc:
        return "TF"
    if "France".lower() in textc:
        return "FR"
    if "Germany".lower() in textc:
        return "DE"
    if "Iran".lower() in textc:
        return "IR"
    if "Israel".lower() in textc:
        return "IL"
    if "Japan".lower() in textc:
        return "JP"
    if "Netherlands".lower() in textc:
        return "NL"
    if "Russia".lower() in textc:
        return "RU"
    if "South Africa".lower() in textc:
        return "ZA"
    if "South Korea".lower() in textc:
        return "KR"
    if "Sweden".lower() in textc:
        return "SE"
    if "Switzerland".lower() in textc:
        return "CH"
    if "Afghanistan".lower() in textc:
        return "AF"
    if "Aland Islands".lower() in textc:
        return "AX"
    if "Albania".lower() in textc:
        return "AL"
    if "Algeria".lower() in textc:
        return "DZ"
    if "American Samoa".lower() in textc:
        return "AS"
    if "Andorra".lower() in textc:
        return "AD"
    if "Angola".lower() in textc:
        return "AO"
    if "Anguilla".lower() in textc:
        return "AI"
    if "Antarctica".lower() in textc:
        return "AQ"
    if "Antigua and Barbuda".lower() in textc:
        return "AG"
    if "Argentina".lower() in textc:
        return "AR"
    if "Armenia".lower() in textc:
        return "AM"
    if "Aruba".lower() in textc:
        return "AW"
    if "Australia".lower() in textc:
        return "AU"
    if "Austria".lower() in textc:
        return "AT"
    if "Azerbaijan".lower() in textc:
        return "AZ"
    if "Bahamas".lower() in textc:
        return "BS"
    if "Bahrain".lower() in textc:
        return "BH"
    if "Bangladesh".lower() in textc:
        return "BD"
    if "Barbados".lower() in textc:
        return "BB"
    if "Belarus".lower() in textc:
        return "BY"
    if "Belgium".lower() in textc:
        return "BE"
    if "Belize".lower() in textc:
        return "BZ"
    if "Benin".lower() in textc:
        return "BJ"
    if "Bermuda".lower() in textc:
        return "BM"
    if "Bhutan".lower() in textc:
        return "BT"
    if "Bolivia".lower() in textc:
        return "BO"
    if "Bonaire, Saint Eustatius and Saba".lower() in textc:
        return "BQ"
    if "Bosnia and Herzegovina".lower() in textc:
        return "BA"
    if "Botswana".lower() in textc:
        return "BW"
    if "Bouvet Island".lower() in textc:
        return "BV"
    if "Brazil".lower() in textc:
        return "BR"
    if "British Indian Ocean Territory".lower() in textc:
        return "IO"
    if "British Virgin Islands".lower() in textc:
        return "VG"
    if "Brunei".lower() in textc:
        return "BN"
    if "Bulgaria".lower() in textc:
        return "BG"
    if "Burkina Faso".lower() in textc:
        return "BF"
    if "Burundi".lower() in textc:
        return "BI"
    if "Cambodia".lower() in textc:
        return "KH"
    if "Cameroon".lower() in textc:
        return "CM"
    if "Canada".lower() in textc:
        return "CA"
    if "Cape Verde".lower() in textc:
        return "CV"
    if "Cayman Islands".lower() in textc:
        return "KY"
    if "Central African Republic".lower() in textc:
        return "CF"
    if "Chad".lower() in textc:
        return "TD"
    if "Chile".lower() in textc:
        return "CL"
    if "Christmas Island".lower() in textc:
        return "CX"
    if "Cocos Islands".lower() in textc:
        return "CC"
    if "Colombia".lower() in textc:
        return "CO"
    if "Comoros".lower() in textc:
        return "KM"
    if "Cook Islands".lower() in textc:
        return "CK"
    if "Costa Rica".lower() in textc:
        return "CR"
    if "Croatia".lower() in textc:
        return "HR"
    if "Cuba".lower() in textc:
        return "CU"
    if "Curacao".lower() in textc:
        return "CW"
    if "Cyprus".lower() in textc:
        return "CY"
    if "Czech Republic".lower() in textc:
        return "CZ"
    if "Democratic Republic of the Congo".lower() in textc:
        return "CD"
    if "Denmark".lower() in textc:
        return "DK"
    if "Djibouti".lower() in textc:
        return "DJ"
    if "Dominica".lower() in textc:
        return "DM"
    if "Dominican Republic".lower() in textc:
        return "DO"
    if "East Timor".lower() in textc:
        return "TL"
    if "Ecuador".lower() in textc:
        return "EC"
    if "Egypt".lower() in textc:
        return "EG"
    if "El Salvador".lower() in textc:
        return "SV"
    if "Equatorial Guinea".lower() in textc:
        return "GQ"
    if "Eritrea".lower() in textc:
        return "ER"
    if "Estonia".lower() in textc:
        return "EE"
    if "Ethiopia".lower() in textc:
        return "ET"
    if "Falkland Islands".lower() in textc:
        return "FK"
    if "Faroe Islands".lower() in textc:
        return "FO"
    if "Fiji".lower() in textc:
        return "FJ"
    if "Finland".lower() in textc:
        return "FI"
    if "French Guiana".lower() in textc:
        return "GF"
    if "Gabon".lower() in textc:
        return "GA"
    if "Gambia".lower() in textc:
        return "GM"
    if "Georgia".lower() in textc:
        return "GE"
    if "Ghana".lower() in textc:
        return "GH"
    if "Gibraltar".lower() in textc:
        return "GI"
    if "Greece".lower() in textc:
        return "GR"
    if "Greenland".lower() in textc:
        return "GL"
    if "Grenada".lower() in textc:
        return "GD"
    if "Guadeloupe".lower() in textc:
        return "GP"
    if "Guam".lower() in textc:
        return "GU"
    if "Guatemala".lower() in textc:
        return "GT"
    if "Guernsey".lower() in textc:
        return "GG"
    if "Guinea".lower() in textc:
        return "GN"
    if "Guinea-Bissau".lower() in textc:
        return "GW"
    if "Guyana".lower() in textc:
        return "GY"
    if "Haiti".lower() in textc:
        return "HT"
    if "Heard Island and McDonald Islands".lower() in textc:
        return "HM"
    if "Honduras".lower() in textc:
        return "HH"
    if "Hong Kong".lower() in textc:
        return "HK"
    if "Hungary".lower() in textc:
        return "HU"
    if "Iceland".lower() in textc:
        return "IS"
    if "India".lower() in textc:
        return "IN"
    if "Indonesia".lower() in textc:
        return "ID"
    if "Iraq".lower() in textc:
        return "IQ"
    if "Ireland".lower() in textc:
        return "IE"
    if "Isle of Man".lower() in textc:
        return "IM"
    if "Italy".lower() in textc:
        return "IT"
    if "Ivory Coast".lower() in textc:
        return "CI"
    if "Jamaica".lower() in textc:
        return "JM"
    if "Jersey".lower() in textc:
        return "JE"
    if "Jordan".lower() in textc:
        return "JO"
    if "Kazakhstan".lower() in textc:
        return "KZ"
    if "Kenya".lower() in textc:
        return "KE"
    if "Kiribati".lower() in textc:
        return "KI"
    if "Kosovo".lower() in textc:
        return "XK"
    if "Kuwait".lower() in textc:
        return "KW"
    if "Kyrgyzstan".lower() in textc:
        return "KG"
    if "Laos".lower() in textc:
        return "LA"
    if "Latvia".lower() in textc:
        return "LV"
    if "Lebanon".lower() in textc:
        return "LB"
    if "Lesotho".lower() in textc:
        return "LS"
    if "Liberia".lower() in textc:
        return "LR"
    if "Libya".lower() in textc:
        return "LY"
    if "Liechtenstein".lower() in textc:
        return "LI"
    if "Lithuania".lower() in textc:
        return "LT"
    if "Luxembourg".lower() in textc:
        return "LU"
    if "Macao".lower() in textc:
        return "MO"
    if "Macedonia".lower() in textc:
        return "MK"
    if "Madagascar".lower() in textc:
        return "MG"
    if "Malawi".lower() in textc:
        return "MW"
    if "Malaysia".lower() in textc:
        return "MY"
    if "Maldives".lower() in textc:
        return "MV"
    if "Mali".lower() in textc:
        return "ML"
    if "Malta".lower() in textc:
        return "MT"
    if "Marshall Islands".lower() in textc:
        return "MH"
    if "Martinique".lower() in textc:
        return "MQ"
    if "Mauritania".lower() in textc:
        return "MR"
    if "Mauritius".lower() in textc:
        return "MU"
    if "Mayotte".lower() in textc:
        return "YT"
    if "Mexico".lower() in textc:
        return "MX"
    if "Micronesia".lower() in textc:
        return "FM"
    if "Moldova".lower() in textc:
        return "MD"
    if "Monaco".lower() in textc:
        return "MC"
    if "Mongolia".lower() in textc:
        return "MN"
    if "Montenegro".lower() in textc:
        return "ME"
    if "Montserrat".lower() in textc:
        return "MS"
    if "Morocco".lower() in textc:
        return "MA"
    if "Mozambique".lower() in textc:
        return "MZ"
    if "Myanmar".lower() in textc:
        return "MM"
    if "Namibia".lower() in textc:
        return "NA"
    if "Nauru".lower() in textc:
        return "NR"
    if "Nepal".lower() in textc:
        return "NP"
    if "Netherlands Antilles".lower() in textc:
        return "AN"
    if "New Caledonia".lower() in textc:
        return "NC"
    if "New Zealand".lower() in textc:
        return "NZ"
    if "Nicaragua".lower() in textc:
        return "NI"
    if "Niger".lower() in textc:
        return "NE"
    if "Nigeria".lower() in textc:
        return "NG"
    if "Niue".lower() in textc:
        return "NU"
    if "Norfolk Island".lower() in textc:
        return "NF"
    if "North Korea".lower() in textc:
        return "KP"
    if "Northern Mariana Islands".lower() in textc:
        return "MP"
    if "Norway".lower() in textc:
        return "NO"
    if "Oman".lower() in textc:
        return "OM"
    if "Pakistan".lower() in textc:
        return "PK"
    if "Palau".lower() in textc:
        return "PW"
    if "Palestinian Territory".lower() in textc:
        return "PS"
    if "Panama".lower() in textc:
        return "PA"
    if "Papua New Guinea".lower() in textc:
        return "PG"
    if "Paraguay".lower() in textc:
        return "PY"
    if "Peru".lower() in textc:
        return "PE"
    if "Philippines".lower() in textc:
        return "PH"
    if "Pitcairn".lower() in textc:
        return "PN"
    if "Poland".lower() in textc:
        return "PL"
    if "Portugal".lower() in textc:
        return "PT"
    if "Puerto Rico".lower() in textc:
        return "PR"
    if "Qatar".lower() in textc:
        return "QA"
    if "Republic of the Congo".lower() in textc:
        return "CG"
    if "Reunion".lower() in textc:
        return "RE"
    if "Romania".lower() in textc:
        return "RO"
    if "Rwanda".lower() in textc:
        return "RW"
    if "Saint Barthelemy".lower() in textc:
        return "BL"
    if "Saint Helena".lower() in textc:
        return "SH"
    if "Saint Kitts and Nevis".lower() in textc:
        return "KN"
    if "Saint Lucia".lower() in textc:
        return "LC"
    if "Saint Martin".lower() in textc:
        return "MF"
    if "Saint Pierre and Miquelon".lower() in textc:
        return "PM"
    if "Saint Vincent and the Grenadines".lower() in textc:
        return "VC"
    if "Samoa".lower() in textc:
        return "WS"
    if "San Marino".lower() in textc:
        return "SM"
    if "Sao Tome and Principe".lower() in textc:
        return "ST"
    if "Saudi Arabia".lower() in textc:
        return "SA"
    if "Senegal".lower() in textc:
        return "SN"
    if "Serbia".lower() in textc:
        return "RS"
    if "Serbia and Montenegro".lower() in textc:
        return "CS"
    if "Seychelles".lower() in textc:
        return "SC"
    if "Sierra Leone".lower() in textc:
        return "SL"
    if "Singapore".lower() in textc:
        return "SG"
    if "Sint Maarten".lower() in textc:
        return "SX"
    if "Slovakia".lower() in textc:
        return "SK"
    if "Slovenia".lower() in textc:
        return "SI"
    if "Solomon Islands".lower() in textc:
        return "SB"
    if "Somalia".lower() in textc:
        return "SO"
    if "South Georgia and the South Sandwich Islands".lower() in textc:
        return "GS"
    if "South Sudan".lower() in textc:
        return "SS"
    if "Spain".lower() in textc:
        return "ES"
    if "Sri Lanka".lower() in textc:
        return "LK"
    if "Sudan".lower() in textc:
        return "SD"
    if "Suriname".lower() in textc:
        return "SR"
    if "Svalbard and Jan Mayen".lower() in textc:
        return "SJ"
    if "Swaziland".lower() in textc:
        return "SZ"
    if "Syria".lower() in textc:
        return "SY"
    if "Taiwan".lower() in textc:
        return "TW"
    if "Tajikistan".lower() in textc:
        return "TJ"
    if "Tanzania".lower() in textc:
        return "TZ"
    if "Thailand".lower() in textc:
        return "TH"
    if "Togo".lower() in textc:
        return "TG"
    if "Tokelau".lower() in textc:
        return "TK"
    if "Tonga".lower() in textc:
        return "TO"
    if "Trinidad and Tobago".lower() in textc:
        return "TT"
    if "Tunisia".lower() in textc:
        return "TN"
    if "Turkey".lower() in textc:
        return "TR"
    if "Turkmenistan".lower() in textc:
        return "TM"
    if "Turks and Caicos Islands".lower() in textc:
        return "TC"
    if "Tuvalu".lower() in textc:
        return "TV"
    if "U.S. Virgin Islands".lower() in textc:
        return "VI"
    if "Uganda".lower() in textc:
        return "UG"
    if "Ukraine".lower() in textc:
        return "UA"
    if "United Arab Emirates".lower() in textc:
        return "AE"
    if "United Kingdom".lower() in textc:
        return "GB"
    if "United States Minor Outlying Islands".lower() in textc:
        return "UM"
    if "Uruguay".lower() in textc:
        return "UY"
    if "Uzbekistan".lower() in textc:
        return "UZ"
    if "Vanuatu".lower() in textc:
        return "VU"
    if "Vatican".lower() in textc:
        return "VA"
    if "Venezuela".lower() in textc:
        return "VE"
    if "Vietnam".lower() in textc:
        return "VN"
    if "Wallis and Futuna".lower() in textc:
        return "WF"
    if "Western Sahara".lower() in textc:
        return "EH"
    if "Yemen".lower() in textc:
        return "YE"
    if "Zambia".lower() in textc:
        return "ZM"
    if "Zimbabwe".lower() in textc:
        return "ZW"
    else:
        return None
