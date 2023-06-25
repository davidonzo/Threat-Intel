# DigitalSide Threat-Intel TAXII2 Server

Instructions for [TAXII2](https://oasis-open.github.io/cti-documentation/taxii/intro.html) server implementation of the [OSINT.digitalside.it](https://osint.digitalside.it/) project. The repository contains the latest 24 hours reports shared in the context of the project. Reports are shipped in STIX2 bundle format.

For people who know what a TAXII2 server is, follows the base instructions:

* Discovery: `https:/osint.digitalside.it/taxii2/`
* Username: `guest`
* Password: `guest`
* Authentication: basic access
* TAXII version: `TAXII2.1`

# Discovery output
```
=============================
DigitalSide.IT TAXII2 Server
=============================
This repository cointains a set of Open Source Cyber Threat Intellegence information, monstly based on malware analysis and compromised URLs, IPs and domains. The purpose of this project is to develop and test new wayes to hunt, analyze, collect and share relevants sets of IoCs to be used by SOC/CSIRT/CERT with minimun effort. For more information please visit OSINT.digitalside.it website.

Discovery URL: https://osint.digitalside.it/taxii2

Available API(s): 1

ROOT API: https://osint.digitalside.it/taxii2reports/
	  Collection: OSINT.DigitalSide.it Malware Reports
	  Description: Set of Open Source Cyber Threat Intellegence information, monstly based on malware analysis and compromised URLs, IPs and domains, related to OSINT.digitalside.it project.
	  ID: e98d6c94-fbce-11ed-b5dd-3bad2ffe9ebf
	  Media type: application/stix+json;version=2.1
=======================================

	  Collection: OSINT.DigitalSide.it Network IoCs Collected (24h)
	  Description: The collection contains IPv4 addresses collected over the last 24 hours by OSINT.digitalside.it. The list is released without any warranty to the end users.
	  ID: c1f43330-103b-11ee-9ee3-4b022e286589
	  Media type: application/stix+json;version=2.1
=======================================
```

For the others, please, before read the technical specifications for [TAXII2](https://oasis-open.github.io/cti-documentation/resources#taxii-20-specification) and [STIX2](https://oasis-open.github.io/cti-documentation/resources#stix-21-specification).

## STIX objects shared via TAXII2
* `identity`
* `marking-definition`
* `report`
* `malware`
* `file`
* `observed-data`
* `indicator`
* `relationship`

## How to and examples
Since TAXII2.1 is basically a RESTful API there are no mandatory requirements to interact with it. Anyway, follows the instructions using official supported and developed [STIX](https://github.com/oasis-open/cti-python-stix2)/[TAXII](https://github.com/oasis-open/cti-taxii-client) client tools by [OASIS](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti).

```
$ pip3 install stix2
$ pip3 install taxii2-client 
```

### Example 1: get TAXII server infos and collections ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiidiscovery.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Server

discovery="https://osint.digitalside.it/taxii2"
username="guest"
password="guest"

server = Server(discovery, user=username, password=password)
print("=============================")	
print(server.title)
print("=============================")
print(server.description+"\n")
print("Discovery URL: "+discovery+"\n")

print("Available API(s): "+str(len(server.api_roots))+"\n")

for api in server.api_roots:
    print("ROOT API: "+api.url)
    for coll in api.collections:
        print("\t  Collection: "+coll.title)
        print("\t  Description: "+coll.description)
        print("\t  ID: "+coll.id)
        
        for media in coll.media_types:
            print("\t  Media type: "+media)
        
        print("=======================================\n")

print("For info please contact: "+server.contact+"\n")
```

### Example 2: get the collection's manifest ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetmanifest.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from taxii2client import Server

discovery="https://osint.digitalside.it/taxii2"
username="guest"
password="guest"

server = Server(discovery, user=username, password=password)

api_root = server.api_roots[0]
collection = api_root.collections[0]
test = collection.get_manifest()
print(json.dumps(test, indent=4, sort_keys=True))
```

### Example 3: get collection's objects ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetobjects.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from taxii2client import Server

discovery="https://osint.digitalside.it/taxii2"
username="guest"
password="guest"

server = Server(discovery, user=username, password=password)

api_root = server.api_roots[0]
collection = api_root.collections[0]
test = collection.get_objects()
print(json.dumps(test, indent=4, sort_keys=True))
```

### Example 4: get collection's objects ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetmalware.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2/collections/e98d6c94-fbce-11ed-b5dd-3bad2ffe9ebf/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "malware")

malwares = tc_source.query([f1])

for malware in malwares:
    print(malware)

print("===============================================")
print("Detected "+str(len(malwares))+" malware objects")
print("===============================================")
```

### Example 5: get latest 24 hours domain-names ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetdomains.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2reports/collections/c1f43330-103b-11ee-9ee3-4b022e286589/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "indicator")
f2 = Filter("pattern","contains", "domain-name:value =")

domains = tc_source.query([f1, f2])

domainz = domains[0].pattern[1:-1].split("OR")

print("====================================================")
print("Detected "+str(len(domainz))+" domain-name objects")
print("====================================================")

for domain in domainz:
    print(domain.strip()[25:-1])
```

### Example 5: get latest 24 hours detected urls ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigeturls.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2reports/collections/c1f43330-103b-11ee-9ee3-4b022e286589/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "indicator")
f2 = Filter("pattern","contains", "domain-name:value =")

domains = tc_source.query([f1, f2])

domainz = domains[0].pattern[1:-1].split("OR")

print("====================================================")
print("Detected "+str(len(domainz))+" domain-name objects")
print("====================================================")

for domain in domainz:
    print(domain.strip()[25:-1])
```

### Example 5: get latest 24 hours detected IPs ([download](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetips.py))

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2reports/collections/c1f43330-103b-11ee-9ee3-4b022e286589/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "indicator")
f2 = Filter("pattern","contains", "ipv4-addr:value =")

ips = tc_source.query([f1, f2])

ipz = ips[0].pattern[1:-1].split("OR")

print("====================================================")
print("Detected "+str(len(ipz))+" ipv4-addr objects")
print("====================================================")

for ip in ipz:
    print(ip.strip()[19:-1])
```

For more examples read the [taxii2-client documentation](https://taxii2client.readthedocs.io/en/latest/).

