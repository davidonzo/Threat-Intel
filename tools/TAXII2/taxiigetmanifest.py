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
