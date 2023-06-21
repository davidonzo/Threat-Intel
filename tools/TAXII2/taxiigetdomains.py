#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2reports/collections/c1f43330-103b-11ee-9ee3-4b022e286589/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "indicator")
f2 = Filter("pattern","contains", "domain-name:value =")

domains = tc_source.query([f1, f2])

for domain in domains:
    print(domain)

print("====================================================")
print("Detected "+str(len(domains))+" domain-name objects")
print("====================================================")

