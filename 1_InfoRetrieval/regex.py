import re

filename = "./factbook/geos/fr.html"

def findGeography(fileName):
    i = 0
    #faire une seule string plutot que lire chaque ligne

    pattern_all_file = re.compile("Geography - note:[\w\W]*?<div.*?\">(.*)?<\/d")
    
    country_file = open(fileName, "r", encoding="utf8")
    test = ""
    for line in country_file:
        i = i + 1
        test = pattern_all_file.search(line)
        if test:
            good_line = line
            break
    print(str(test))
    

findGeography(filename)
