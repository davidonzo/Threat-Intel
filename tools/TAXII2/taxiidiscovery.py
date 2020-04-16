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
