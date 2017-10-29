import re
import codecs

filename = "./factbook/geos/uk.html"

def findGeography(fileName):
    try:
        pattern_all_file = re.compile("(Geography - note:[\w\W]*?<div.*?\">)(.*)?(<\/d)")
        country_file = codecs.open(fileName, "r", encoding="utf8")
        test = pattern_all_file.search(country_file.read())
        return str(test.group(2)) 
    except AttributeError:
        return '\"\"'  


def findEconomy(fileName):
    try:
        pattern_all_file = re.compile("(Economy - overview[\w\W]*?<div class=\"category_data\">)(.*)?(<\/div)")
        country_file = codecs.open(fileName, "r", encoding="utf8")
        test = pattern_all_file.search(country_file.read())
        return str(test.group(2)) 
    except AttributeError:        
        return '\"\"'

def findIntroduction(fileName):
    try:
        pattern_all_file = re.compile("(Introduction</span>[\w\W]*?<div class=\"category_data\">)(.*)?(<\/div)")
        country_file = codecs.open(fileName, "r", encoding="utf8")
        test = pattern_all_file.search(country_file.read())
        return str(test.group(2)) 
    except AttributeError:
        return '\"\"'

def getCountryName(fileName):
    if ((fileName[-7]+fileName[-6]) == "dq"):
        return ("Jarvis Island (TERRITORY OF THE US)")
    elif ((fileName[-7]+fileName[-6]) == "hq"):
        return ("HOWLAND ISLAND (TERRITORY OF THE US)")
    elif ((fileName[-7]+fileName[-6]) == "jq"):
        return ("JOHNSTON ATOLL (TERRITORY OF THE US)")
    elif ((fileName[-7]+fileName[-6]) == "kq"):
        return ("KINGMAN REEF (TERRITORY OF THE US)")
    elif ((fileName[-7]+fileName[-6]) == "lq"):
        return ("PALMYRA ATOLL (TERRITORY OF THE US)")
    elif ((fileName[-7]+fileName[-6]) == "mq"):
        return ("MIDWAY ISLANDS (TERRITORY OF THE US)")
    else:
        regex = "<o.*s\/"+fileName[-7]+fileName[-6]+".html\"> (.*) <\/"
        pattern_all_file = re.compile(regex)
        country_file = codecs.open("./factbook/index.html", "r", encoding="utf8")
        test = pattern_all_file.search(country_file.read())
        # print(test)
        return str(test.group(1))
