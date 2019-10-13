# FINAL VERSION
## This is a legacy version.
## For new version please visit the project [apiosintDS Project](https://github.com/davidonzo/apiosintDS)

# DigitalSide-API v.0.1
On demand query API for OSINT.digitalside.it project. You can query for souspicious IPs (just IPv4 supported at the moment), domains and urls.

## Requiremets
The script runs using python intepreter at version 3.x. No support will be given to python 2.x.
Running the script it should be advise you in case you don't have installed a required library.

## Usage
```
python3 /path/to/digitest.py [IPv4|Domain|Url]
```

Example response for a listed item
```
{
     "item": "120.142.181.110",
     "item_type": "ip",
     "response": true,
     "response_text": "Item found in ips.txt list",
     "related_urls": [
         "http://120.142.181.110:48329/.i"
     ],
     "list_date": "2019-10-08 12:14:18",
     "list_link": "https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestips.txt"
}
```

Example response for an unlisted item:
```
{
     "item": "120.142.181.109",
     "item_type": "ip",
     "response": false,
     "response_text": "Item not found",
     "related_urls": []
     "list_date": "2019-10-08 12:14:18",
     "list_link": "https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestips.txt"
}
```

[Json schema](https://github.com/davidonzo/Threat-Intel/blob/master/tools/DigitalSide-API/schema.json)
```
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Validator for DigitalSide-API response",
  "id": "https://github.com/davidonzo/Threat-Intel/tools/DigitalSide-API/schema.json",
  "properties": {
    "item": {
      "type": "string",
      "description": "The entity to search using DigitalSide-API"
    },
    "item_type": {
      "type": "string",
      "enum": ["domain", "ip", "url"],
      "description": "The entity type, that can be an URL, an IP or a domain name"
    },
    "response": {
      "type": "boolean",
      "description": "True if a match has been found. False if no match has been found"
    },
    "response_text": {
      "type": "string",
      "description": "Just a human readble representation of the 'response' item"
    },
    "related_urls": {
      "type": "array",
      "items": [
        {
          "type": "string",
          "description": "The related URLs associated to the submitted item. If no related IoC found, the list will be empty"
        }
      ]
    },
    "list_date": {
      "type": "string",
      "description": "The published datetime of the downloaded list"
      
    },
    "list_link": {
      "type": "string"
    }
  },
  "required": [
    "item",
    "item_type",
    "response",
    "response_text",
    "related_urls",
    "list_date",
    "list_link"
  ]
}
```
