#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taxii2client import Collection
from stix2 import TAXIICollectionSource, Filter


collection = Collection("https://osint.digitalside.it/taxii2reports/collections/c1f43330-103b-11ee-9ee3-4b022e286589/", user="guest", password="guest")
tc_source = TAXIICollectionSource(collection)


f1 = Filter("type","=", "indicator")
f2 = Filter("pattern","contains", "url:value =")

urls = tc_source.query([f1, f2])

urlz = urls[0].pattern[1:-1].split("OR")

print("====================================================")
print("Detected "+str(len(urlz))+" url objects")
print("====================================================")


for url in urlz:
    print(url.strip()[13:-1])


