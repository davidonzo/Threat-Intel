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

