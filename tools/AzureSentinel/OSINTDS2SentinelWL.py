#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Davide Baglieri"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Davide Baglieri"
__email__ = "info@digitalside.it"
__status__ = "Dev"


import sys
from msrestazure.azure_active_directory import AADTokenCredentials

from azure.mgmt.datalake.analytics.job import DataLakeAnalyticsJobManagementClient
from azure.mgmt.datalake.analytics.job.models import JobInformation, JobState, USqlJobProperties

import adal, uuid, time

import requests
import re
import json

#########################################################
###################USER CONFIGURATION####################
#########################################################
watchlist_alias = "osintds" #can change the default
displayName = "OSINT-DigitalSide.it" #can change the default
source = "https://osint.digitalside.it" #can change the default
description = "Watchlist from OSINT-Digitalside.it lists" #can change the default
tenant_id = "<the Azure tenant id>"
client_id = "<the registered app client id>"
client_secret = "<the registered app client secret>"
subscription_id = "<your Azure subscription id>"
resource_group = "<the Resource Group where the Sentinel workspace is mapped>"
workspace = "<the name of the workspace used by Sentinel>"
api_version = "2019-01-01-preview" #actual valid version
#########################################################
#########################################################
#############DON'T CHANGE THE COSE BELOW#################
######UNLESS YOU DON'T KNOW WHAT ARE YOU GOING TO DO#####
#########################################################
#########################################################

azure_ad_token = {}
watchlist_items = []

def configurl():
    url = {
              "master_url": "https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latest",
              "slave_url": "https://osint.digitalside.it/Threat-Intel/lists/latest"
    }
    return url
    
def listItems(items):
    reslist = []
    for i in items.splitlines():
        if not re.match('^#', i):
            reslist.append(i)
    
    return reslist

def getItems(entity):
    c = configurl()
    
    r = requests.get(c['master_url']+entity+'.txt')
    
    if r.status_code != 200:
        print("Error downloading lastes"+entity+".txt from GitHub repository.")
        print("Try downloading file from osint.digitalside.it")
        r = requests.get(c['slave_url']+entity+'s.txt')
        if r.status_code != 200:
            print("Error downloading lastes"+entity+".txt both from GitHub repository and OSINT.digitalside.it")
            print("Returned HTTP status code is: "+str(r.status_code))
        return 1
    
    text = r.text
    if len(text) == 0: #just because I'm a very paranoid man, but same time a lazy one ^_^'''
        print("The downloaded list seems to be empty!")
        return 1
    
    return listItems(text)

def login_to_azureAD():
    """
    Authenticate using service principal w/ key.
    Reference: https://docs.microsoft.com/en-us/samples/azure-samples/data-lake-analytics-python-auth-options/authenticating-your-python-application-against-azure-active-directory/
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    authority_uri = authority_host_uri + '/' + tenant_id
    resource_uri = 'https://management.core.windows.net/'
    
    try:
        context = adal.AuthenticationContext(authority_uri, api_version=None)
        mgmt_token = context.acquire_token_with_client_credentials(resource_uri, client_id, client_secret)
        credentials = AADTokenCredentials(mgmt_token, client_id)
        return mgmt_token
    except Exception as e:
        print(e)
        sys.exit()
    
def get_token():
    global azure_ad_token
    
    if not azure_ad_token:
        azure_ad_token = login_to_azureAD()
    else:
        ts = time.time()
        expiration = azure_ad_token['expiresOn'] - ts
        
        if expiration < 20:
            azure_ad_token = login_to_azureAD()
            
    return azure_ad_token
    
def get_watchlist():
    mytoken = get_token()
    token = {'Authorization': 'Bearer '+mytoken['accessToken']}
    
    try:
        r = requests.get('https://management.azure.com/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.OperationalInsights/workspaces/'+workspace+'/providers/Microsoft.SecurityInsights/watchlists?api-version='+api_version, headers=token)
        
        if r.status_code != 200:
            print("HTTP response error. Response code is: "+str(r.status_code))
            sys.exit()
        else:
            watchlist = r.json()
            
            ret = []
            for item in watchlist["value"]:
                ret.append(item["name"])
            return ret
            
    except Exception as e:
        print(e)
        sys.exit()
        
def get_watchlist_data(url=False):
    global watchlist_items
    mytoken = get_token()
    token = {'Authorization': 'Bearer '+mytoken['accessToken']}
    
    if not url:
        url = 'https://management.azure.com/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.OperationalInsights/workspaces/'+workspace+'/providers/Microsoft.SecurityInsights/watchlists/'+watchlist_alias+'/watchlistitems?api-version='+api_version
    
    try:
        r = requests.get(url, headers=token)
        
        if r.status_code != 200:
            print("HTTP response error. Response code is: "+str(r.status_code))
            sys.exit()
        else:
            watchlist = r.json()
            
            for item in watchlist["value"]:
                watchlist_items.append(item["properties"]["itemsKeyValue"]["IoC"])
            
            if "nextLink" in watchlist:
                if watchlist["nextLink"] != url:
                    get_watchlist_data(watchlist["nextLink"])
      
    except Exception as e:
        print(e)
        print(r.text)
        sys.exit()
    
    return watchlist_items

def data_type(i):
    if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", i):
        return "ip"
    if re.match("^http:\/\/|^https:\/\/", i):
        return "url"
    
    return "domain"

def get_data_osintds():    
    domains = getItems("domains")
    urls = getItems("urls")
    ips = getItems("ips")
    
    return domains + urls + ips
    
def update_watchlist():
    osintds_data = get_data_osintds()
    watchlist_data = get_watchlist_data()
    
    a = 0;
    for item in osintds_data:
        if item not in watchlist_data:
            post_data = '{"properties": {"itemsKeyValue": {"IoC": "'+item+'","Type": "'+data_type(item)+'"}}}'
            
            mytoken = get_token()
            header = {'Authorization': 'Bearer '+mytoken['accessToken'], 'Content-type':'application/json'}
            
            try:
                update = requests.put('https://management.azure.com/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.OperationalInsights/workspaces/'+workspace+'/providers/Microsoft.SecurityInsights/watchlists/'+watchlist_alias+'/watchlistitems/'+str(uuid.uuid4())+'?api-version='+api_version, headers=header, data=post_data)
        
                if update.status_code != 200:
                    print("HTTP response error. Response code is: "+str(update.status_code))
                    print("Error message is: "+update.text)
                else:
                    a += 1
      
            except Exception as e:
                print(e)
    
    return a
    
def create_data_watchlist():
    res = ""
    domains = getItems("domains")
    if len(domains) > 0:
        for domain in domains:
            res += domain+",domain\n"
    

    urls = getItems("urls")
    if len(urls) > 0:
        for url in urls:
            res += url+",url\n"
    
    ips = getItems("ips")
    if len(ips) > 0:
        for ip in ips:
            res += ip+",ip\n"
        
    return res
        
def create_watchlist():
    mytoken = get_token()
    header = {'Authorization': 'Bearer '+mytoken['accessToken'], 'Content-type':'application/json'}
    
    create_data = create_data_watchlist()
    
    if len(create_data) == 0:
        return "No data found to create watchlist. ABORTED"

    create_list = {
            "properties": {
                "displayName": displayName,
                "source": source,
                "provider": "Microsoft",
                "numberOfLinesToSkip":"1",
                "rawContent": "",
                "contentType": "text/csv",
                "description": description
                }
            }
    
    import_data = {
            "properties": {
                "displayName": displayName,
                "source": source,
                "provider": "Microsoft",
                "numberOfLinesToSkip":"0",
                "rawContent": "IoC,Type\n"+create_data,
                "contentType": "text/csv",
                "description": description
                }
            }
    
    create_list = json.dumps(create_list)
    import_data = json.dumps(import_data)

    try:
        r_first = requests.put('https://management.azure.com/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.OperationalInsights/workspaces/'+workspace+'/providers/Microsoft.SecurityInsights/watchlists/'+watchlist_alias+'?api-version='+api_version, headers=header, data=create_list)
        
        if r_first.status_code != 200:
            print("HTTP response error. Response code is: "+str(r_first.status_code))
            print("Error message is: "+r_first.text)
            sys.exit()
        else:
            try:
                r_second = requests.put('https://management.azure.com/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.OperationalInsights/workspaces/'+workspace+'/providers/Microsoft.SecurityInsights/watchlists/'+watchlist_alias+'?api-version='+api_version, headers=header, data=import_data)
                if r_second.status_code != 200:
                    print("HTTP response error. Response code is: "+str(r_second.status_code))
                    print("Error message is: "+r_second.text)
                    sys.exit()
                else:
                    return "Watchlist created!"
            except Exception as e:
                print(e)
                sys.exit()        
    except Exception as e:
        print(e)
        sys.exit()
    



if __name__ == '__main__':
    watchlist = get_watchlist()
    
    if watchlist_alias not in watchlist:
        print("The watchlist does not exist. Going to create it.")
        wl = create_watchlist()
        print(wl)
    else:
        print("The list exists. Going to update it.")
        data = update_watchlist()
        print(data)
