import re
import codecs

filename = "./factbook/geos/uk.html"

def findGeography(fileName):
    pattern_all_file = re.compile("(Geography - note:[\w\W]*?<div.*?\">)(.*)?(<\/d)")
    country_file = codecs.open(fileName, "r", encoding="utf8")
    test = pattern_all_file.search(country_file.read())
    return str(test.group(2)) 


def findEconomy(fileName):
    pattern_all_file = re.compile("(Economy - overview[\w\W]*?<div class=\"category_data\">)(.*)?(<\/div)")
    country_file = codecs.open(fileName, "r", encoding="utf8")
    test = pattern_all_file.search(country_file.read())
    return str(test.group(2)) 

def findIntroduction(fileName):
    pattern_all_file = re.compile("(Introduction</span>[\w\W]*?<div class=\"category_data\">)(.*)?(<\/div)")
    country_file = codecs.open(fileName, "r", encoding="utf8")
    test = pattern_all_file.search(country_file.read())
    return str(test.group(2)) 

print(findEconomy(filename))