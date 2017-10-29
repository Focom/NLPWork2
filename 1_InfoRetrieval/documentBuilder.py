import helper
import regex
import json
import re


def createJSON(fileName):
    country_name = regex.getCountryName(fileName).replace('"','\\"')
    intro = regex.findIntroduction(fileName).replace('"','\\"')
    economy = regex.findEconomy(fileName).replace('"','\\"')
    geography = regex.findGeography(fileName).replace('"','\\"')

    data = {'Name': country_name, 'Intro': intro, 'Economy': economy, 'Geography': geography }
    with open('./JSON/'+country_name+'.json', 'w') as fp:
        json.dump(data, fp)
    return data

def createAllJSON():
    files = helper.getAllFile()
    print(files)
    for file in files:
        createJSON(file)

def test():
    files = helper.getAllFile()
    for file in files:
        # print(file)
        createJSON(file)
    

test()
