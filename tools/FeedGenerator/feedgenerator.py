#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Davide Baglieri"
__credits__ = ["MISP Project"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Davide Baglieri"
__email__ = "info@digitalside.it"
__status__ = "Dev"


import sys
import json
import os
import hashlib
import pymisp
import requests
from datetime import datetime
from feedgeneratorconf import url, key, ssl, mispfeeddir, csvdir, stix2dir, listsdir, filters, valid_attribute_distribution_levels, enabled, listsenabled, listsheader


objectsFields = {
    'Attribute': {
        'uuid',
        'value',
        'category',
        'type',
        'comment',
        'data',
        'timestamp',
        'to_ids',
        'object_relation'
    },
    'Event': {
        'uuid',
        'info',
        'threat_level_id',
        'analysis',
        'timestamp',
        'publish_timestamp',
        'published',
        'date'
    },
    'Object': {
        'name',
        'meta-category',
        'description',
        'template_uuid',
        'template_version',
        'uuid',
        'timestamp',
        'distribution',
        'sharing_group_id',
        'comment'
    },
    'ObjectReference': {
        'uuid',
        'timestamp',
        'relationship_type',
        'comment',
        'object_uuid',
        'referenced_uuid'
    },
    'Orgc': {
        'name',
        'uuid'
    },
    'Tag': {
        'name',
        'colour',
        'exportable'
    }
}

objectsToSave = {
    'Orgc': {},
    'Tag': {},
    'Attribute': {
        'Tag': {}
    },
    'Object': {
        'Attribute': {
            'Tag': {}
        },
        'ObjectReference': {}
    }
}


valid_attribute_distributions = []

attributeHashes = []


def init():
    # If we have an old settings.py file then this variable won't exist
    global valid_attribute_distributions
    try:
        valid_attribute_distributions = valid_attribute_distribution_levels
    except Exception:
        valid_attribute_distributions = ['0', '1', '2', '3', '4', '5']
    return pymisp.ExpandedPyMISP(url, key, ssl)


def recursiveExtract(container, containerType, leaf, eventUuid):
    temp = {}
    if containerType in ['Attribute', 'Object']:
        if (__blockByDistribution(container)):
            return False
    for field in objectsFields[containerType]:
        if field in container:
            temp[field] = container[field]
    if (containerType == 'Attribute'):
        global attributeHashes
        if ('|' in container['type'] or container['type'] == 'malware-sample'):
            split = container['value'].split('|')
            attributeHashes.append([hashlib.md5(split[0].encode("utf-8")).hexdigest(), eventUuid])
            attributeHashes.append([hashlib.md5(split[1].encode("utf-8")).hexdigest(), eventUuid])
        else:
            attributeHashes.append([hashlib.md5(container['value'].encode("utf-8")).hexdigest(), eventUuid])
    children = leaf.keys()
    for childType in children:
        childContainer = container.get(childType)
        if (childContainer):
            if (type(childContainer) is dict):
                temp[childType] = recursiveExtract(childContainer, childType, leaf[childType], eventUuid)
            else:
                temp[childType] = []
                for element in childContainer:
                    processed = recursiveExtract(element, childType, leaf[childType], eventUuid)
                    if (processed):
                        temp[childType].append(processed)
    return temp


def __blockByDistribution(element):
    if element['distribution'] not in valid_attribute_distributions:
        return True
    return False

def saveEvent(misp, uuid):
    event = misp.get_event(uuid)
    if not event.get('Event'):
        print('Error while fetching event: {}'.format(event['message']))
        sys.exit('Could not create file for event ' + uuid + '.')
    event['Event'] = recursiveExtract(event['Event'], 'Event', objectsToSave, event['Event']['uuid'])
    evento = json.dumps(event)
    eventFile = open(os.path.join(mispfeeddir, uuid + '.json'), 'w')
    eventFile.write(evento)
    eventFile.close()

def saveHashes():
    if not attributeHashes:
        return False
    try:
        hashFile = open(os.path.join(mispfeeddir, 'hashes.csv'), 'w')
        for element in attributeHashes:
            hashFile.write('{},{}\n'.format(element[0], element[1]))
        hashFile.close()
    except Exception as e:
        print(e)
        sys.exit('Could not create the quick hash lookup file.')


def saveManifest(manifest):
    try:
        manifestFile = open(os.path.join(mispfeeddir, 'manifest.json'), 'w')
        manifestFile.write(json.dumps(manifest))
        manifestFile.close()
    except Exception as e:
        print(e)
        sys.exit('Could not create the manifest file.')


def __addEventToManifest(event):
    tags = []
    for eventTag in event['EventTag']:
        tags.append({'name': eventTag['Tag']['name'],
                     'colour': eventTag['Tag']['colour']})
    return {'Orgc': event['Orgc'],
            'Tag': tags,
            'info': event['info'],
            'date': event['date'],
            'analysis': event['analysis'],
            'threat_level_id': event['threat_level_id'],
            'timestamp': event['timestamp']
            }


def deleteall(directory):
    for the_file in os.listdir(directory):
        file_path = os.path.join(directory, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
            
def getevent(ide, uide, formato):
    headers = {'Authorization': key}
    r = requests.get(url + '/events/restSearch/'+formato+'/eventid:' + ide, headers=headers, verify=ssl)
    
    responseCode = r.status_code
    
    if responseCode == 200:
        if formato == 'stix2':
            content = r.json()
            eventfile = json.dumps(content, indent=4, sort_keys=True)
            thefile = stix2dir+uide+".json"
            
        if formato == 'csv':
            eventfile = r.text
            thefile = csvdir+uide+".csv"
    
    f = open(thefile, "w")
    f.write(str(eventfile))
    f.close()   
    
    
def getLists(thelist):
    headers = {'Authorization': key}
    
    if thelist == "domains":
        misptype = "domain"
    if thelist == "ips":
        misptype = "ip-dst"
    if thelist == "urls":
        misptype = "url"
    if thelist == "piHole":
        misptype = "domain"

    postdata = {"returnFormat":"text","type":misptype, "category":"Network activity", **filters}
    r = requests.post(url + '/attributes/restSearch', headers=headers, verify=ssl, data=postdata)
    
    responseCode = r.status_code
    
    if responseCode == 200:
        content = r.text
        thefile = listsdir+thelist+".txt"
    
        if thelist == 'piHole':
            ioc = content.split("\n")
            newcontent = ""
        
            for i in ioc:
                if len(i) > 0:
                    newcontent += '0.0.0.0 '+i+'\n'
            content = newcontent
        
        f = open(thefile, "w")
        f.write(str(listsheader[thelist])+"\n"+str(content))
        f.close()
    else:
        print("Bad http code detected: " + responseCode)
        print("Unable to generate the " + thelist + " list.")


if __name__ == '__main__':
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Started at =", dt_string)	
    
    
    if enabled["csv"]:
        deleteall(csvdir)
    if enabled["stix2"]:
        deleteall(stix2dir)
    if enabled["mispfeed"]:
        deleteall(mispfeeddir)
    if enabled["lists"]:
        deleteall(listsdir)
    
    misp = init()
    
    try:
        r = misp.search_index(**filters)
        events = r
        
    except Exception as e:
        print(e)
        sys.exit("Invalid response received from MISP.")
    if len(events) == 0:
        sys.exit("No events returned.")
    
    if enabled["mispfeed"]:
        manifest = {}
        counter = 1
        total = len(events)
        
        for event in events:
            saveEvent(misp, event['uuid'])
            manifest[event['uuid']] = __addEventToManifest(event)
            print("Event " + str(counter) + "/" + str(total) + " exported.")
            counter += 1
        saveManifest(manifest)
        print('Manifest saved.')
        saveHashes()
        print('Hashes saved. Feed creation completed.')
    
    if enabled["stix2"]:
        print("Starting STIX2 export")
        stixcounter = 1
        for event in events:
            getevent(event['id'], event['uuid'], 'stix2')
            print("STIX2 event " + str(stixcounter) + "/" + str(total) + " exported.")
            stixcounter += 1
        print("STIX2 events exported")
    
    if enabled["csv"]:
        print("Starting CSV export")
        csvcounter = 1
        for event in events:
            getevent(event['id'], event['uuid'], 'csv')
            print("CSV event " + str(csvcounter) + "/" + str(total) + " exported.")
            csvcounter += 1
        print("CSV events exported")
    
    if enabled["lists"]:
        if listsenabled["domains"]:
            getLists("domains")
        if listsenabled["urls"]:
            getLists("urls")
        if listsenabled["ips"]:
            getLists("ips")
        if listsenabled["piHole"]:
             getLists("piHole")
        
    noww = datetime.now()
    dt_stringw = noww.strftime("%d/%m/%Y %H:%M:%S")
    print("Started at =", dt_stringw)

