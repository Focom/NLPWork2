import re
import codecs

filename = "./factbook/geos/aa.html"

def findGeography(fileName):
    pattern_all_file = re.compile("Geography - note:[\w\W]*?<div.*?\">(.*)?<\/d")
    country_file = codecs.open(fileName, "r", encoding="utf8")
    test = pattern_all_file.search(country_file.read())
    return str(test.group(1)) 

findGeography(filename)


