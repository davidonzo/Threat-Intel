# DigitalSide Threat-Intel TAXII2 Server

Instructions for [TAXII2](https://oasis-open.github.io/cti-documentation/taxii/intro.html) server implementation of the [OSINT.digitalside.it](https://osint.digitalside.it/) project. The repository contains the latest 24 hours reports shared in the context of the project. Reports are shipped in STIX2 bundle format.

For people who know what a TAXII2 server is, follows the base instructions:

* Discovery: https:/taxii.digitalside.it/taxii/
* Username: guest
* Password: guest
* Authentication: basic access

For the others, please, before read the technical specifications for [TAXII2](https://oasis-open.github.io/cti-documentation/resources#taxii-20-specification) and [STIX2](https://oasis-open.github.io/cti-documentation/resources#stix-20-specification).

## How to and examples
One way to interact with the TAXII server is using [cti-taxii-client](https://github.com/oasis-open/cti-taxii-client) by [OASIS](https://www.oasis-open.org/).

```
pip install taxii2-client
```

### Example 1: get TAXII server infos and collections

```
#!/usr/bin/env python3

from taxii2client import Server

discovery="http://taxii.digitalside.it/taxii"
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

### Example 2: get the collection's manifest

```
#!/usr/bin/env python3
import json
from taxii2client import Server

discovery="http://taxii.digitalside.it/taxii"
username="guest"
password="guest"

server = Server(discovery, user=username, password=password)

api_root = server.api_roots[0]
collection = api_root.collections[0]
test = collection.get_manifest()
print(json.dumps(test, indent=4, sort_keys=True))
```

### Example 3: get collection's objects

```
#!/usr/bin/env python3
import json
from taxii2client import Server

discovery="http://taxii.digitalside.it/taxii"
username="guest"
password="guest"

server = Server(discovery, user=username, password=password)

api_root = server.api_roots[0]
collection = api_root.collections[0]
test = collection.get_objects()
print(json.dumps(test, indent=4, sort_keys=True))
```

For more examples read the [taxii2-client documentation](https://taxii2client.readthedocs.io/en/latest/).

