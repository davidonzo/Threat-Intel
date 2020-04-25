#!/usr/bin/env python3
import sys
if (sys.version_info < (3, 0)):#NO MORE PYTHON 2!!! https://pythonclock.org/
    print(" ################# ERROR ################")
    print(" ========================================")
    print("   Invalid python version detected: "+str(sys.version_info[0])+"."+str(sys.version_info[1]))
    print(" ========================================")
    print(" It seems your are still using python 2 even if you should now it will be retire next 2020.")
    print(" For more info please read https://pythonclock.org/")
    print(" ========================================")
    print(" Try again typing: python3 /path/to/"+sys.argv[0])
    print(" ################# ERROR ################")
    exit(0)
import requests
import re
import json
try:
    from urllib.parse import urlparse
except ImportError as ierror:
    print(ierror)
    print("To run this script you need to install the \"urllib\" module")
    print("Try typing: \"pip3 install urllib3\"")
    exit(0)
try:
    import validators
except ImportError as e:
    print(e)
    print("To run this script you need to install the \"validators\" module")
    print("Try typing: \"pip3 install validators\"")
    exit(0)

results = {"item": "undefined",
           "item_type": "undefined",
           "response": False,
           "response_text": "undefined",
           "related_urls": [],
           "list_date": "undefined",
           "list_link": "undefined"}

def scriptinfo():
    scriptinfo = {"scriptname": "DigitalSide-API",
                  "majorversion": "0",
                  "minorversion": "1",
                  "license": "MIT",
                  "licenseurl": "https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/LICENSE",
                  "author": "Davide Baglieri",
                  "mail": "info[at]digitalside.it",
                  "pgp": "30B31BDA",
                  "fingerprint": "0B4C F801 E8FF E9A3 A602  D2C7 9C36 93B2 30B3 1BDA",
                  "git": "https://github.com/davidonzo/Threat-Intel/tools/DigitalSide-API",
                  "DSProjectHP": "https://osint.digitalside.it",
                  "DSGitHubHP": "https://github.com/davidonzo/Threat-Intel"}
    return scriptinfo

def config():
    config = {
              "master_url": "https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latest",
              "slave_url": "https://osint.digitalside.it/Threat-Intel/lists/latest"
    }
    return config

def help():
    info = scriptinfo()
    htext = " "+info["scriptname"]+" v."+info["majorversion"]+"."+info["minorversion"]+"\n"
    htext += "\n"
    htext += " Usage: python3 /path/to/"+sys.argv[0]+" [IPv4|Domain|Url]\n"
    htext += "\n"
    htext += " Description: on demand query API for OSINT.digitalside.it project.\n"
    htext += "              You can query for souspicious IPs (just IPv4 supported\n"
    htext += "              at the moment), domains and urls.\n"
    htext += "\n"
    htext += " Example response for a listed item:\n"
    htext += " {\n"
    htext += "     \"item\": \"120.142.181.110\",\n"
    htext += "     \"item_type\": \"ip\",\n"
    htext += "     \"response\": true,\n"
    htext += "     \"response_text\": \"Item found in ips.txt list\",\n"
    htext += "     \"related_urls\": [\n"
    htext += "         \"http://120.142.181.110:48329/.i\"\n"
    htext += "     ],\n"
    htext += "     \"list_date\": \"2019-10-08 12:14:18\",\n"
    htext += "     \"list_link\": \"https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestips.txt\"\n"
    htext += " }\n\n"
    htext += "\n"
    htext += " Example response for an unlisted item:\n"
    htext += " {\n"
    htext += "     \"item\": \"120.142.181.109\",\n"
    htext += "     \"item_type\": \"ip\",\n"
    htext += "     \"response\": false,\n"
    htext += "     \"response_text\": \"Item not found\",\n"
    htext += "     \"related_urls\": []\n"
    htext += "     \"list_date\": \"2019-10-08 12:14:18\",\n"
    htext += "     \"list_link\": \"https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestips.txt\"\n"
    htext += " }\n\n"
    htext += " For more information read the README.md file and the JSON schema hosted on GitHub.com:\n"
    htext += "         - "+info["git"]+"/README.md\n"
    htext += "         - "+info["git"]+"/schema.json\n"
    htext += "\n"
    htext += " This file is part of the OSINT.digitalside.it project.\n"
    htext += " For more information about the project please visit the following links:\n"
    htext += "         - "+info["DSProjectHP"]+"\n"
    htext += "         - "+info["DSGitHubHP"]+"\n"
    htext += "\n"
    htext += " This software is released under the "+info["license"]+" license\n"
    htext += "         - "+info["licenseurl"]+"\n"
    htext += "\n"
    htext += " Coded with love by "+info["author"]+"\n"
    htext += "                    Email       <"+info["mail"]+">\n"
    htext += "                    PGP         "+info["pgp"]+"\n"
    htext += "                    Fingerprint "+info["fingerprint"]
    htext += "\n"
    return htext

def getItems(entity, related):
    c = config()
    r = requests.get(c['master_url']+entity+'s.txt')
    if r.status_code != 200:
        print("Error downloading lastes"+entity+".txt from GitHub repository.")
        print("Try downloading file from osint.digitalside.it")
        r = requests.get(c['slave_url']+entity+'s.txt')
        if r.status_code != 200:
            print("Error downloading lastes"+entity+".txt both from GitHub repository and OSINT.digitalside.it")
            print("Returned HTTP status code is: "+str(r.status_code))
            print(status_error(entity))
        else:
            if related == 0 : results["list_link"] = c['slave_url']+entity+'s.txt'
        return 1
    else:
        if related == 0 : results["list_link"] = c['master_url']+entity+'s.txt'
    text = r.text
    if len(text) == 0: #just because I'm a very paranoid man, but same time a lazy one ^_^'''
        print("The downloaded list seems to be empty!")
        print(status_error(entity))
        return 1
    return text

def parselists(entity, item, related):
    r = getItems(entity, related)
    r = r.split('\n')
    return r

def parsedate(r):
    return r[9][16:35]

def parseitem(r, item):
    for line in r:
        if re.search("^"+item+"$", line):
            return 0
    return 1

def parseRelatedUrl(item):
    relatedURLs = []
    resUrls = getItems('url', 1).split('\n')
    for lineurl in resUrls:
        ParseURL = urlparse(lineurl)
        if ParseURL.hostname == item:
            relatedURLs.append(lineurl)
    return relatedURLs
 
def status_error(entity):
    error="Check the following urls using your prefered browser:\n"
    error+="- https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latest"+entity+".txt\n"
    error+="- https://osint.digitalside.it/Threat-Intel/lists/latest"+entity+".txt\n"
    error+="\n"
    error+="Are you able to view the desired IoC list? If not, please, report this opening an issue on Threat-Intel GitHub repository:\n"
    error+="- https://github.com/davidonzo/Threat-Intel/issues\n"
    error+="\n"
    error+="Aren't you familiar with GitHub? No worries. You can send a PGP signed and encrypted email to info@digitalside.it\n"
    error+="PGP key ID: 30B31BDA\n"
    error+="PGP fingerprint: 0B4C F801 E8FF E9A3 A602  D2C7 9C36 93B2 30B3 1BDA\n"
    error+="\n"
    error+="Aren't you familiar with PGP? Be worried... maybe you should not use this script ;-)\n"
    return error
    
def item_error(item):
    error="The item selected seems not to be a valid entity.\n"
    error+="Valids entities are:\n"
    error+="- Domains\n"
    error+="- IPv4\n"
    error+="- URLs\n"
    return error
    
def checkitem(item):
    url = validators.url(item)
    if url == True:
        return "url"
    ip = validators.ipv4(item)
    if ip == True:
        return "ip"
    domain = validators.domain(item)
    if domain == True:
        return "domain"
    print(item_error(item))
    return False

def dosearch(item):
    results["item"] = item
    itemtype = checkitem(item)
    if itemtype in ('domain', 'ip', 'url'):
        results["item_type"] = itemtype
        r = parselists(itemtype, item, 0)
        datelist = parsedate(r)
        searchItem = parseitem(r, item)
        if searchItem != 1:
            results["response"] = True
            results["response_text"] = "Item found in "+itemtype+"s.txt list"
            if itemtype != 'url':
                related = parseRelatedUrl(item)
            else:
                getItem = urlparse(item)
                related = parseRelatedUrl(getItem.hostname)
                related.remove(item)
            results["related_urls"] = related
        else:
            results["response_text"] = "Item not found"
        results["list_date"] = datelist
    return json.dumps(results, indent=4, separators=(",", ": "))

def main():
    if len(sys.argv) < 2:
        print(help())
        exit(0)
    item = sys.argv[1]
    letsgo = dosearch(item)
    print(letsgo)

if __name__ == '__main__':
    main()
