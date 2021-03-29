# DigitalSide Threat-Intel to Azure Sentinel Watchlist

[Microsoft Azure Sentinel](https://docs.microsoft.com/it-it/azure/sentinel/overview) is a cloud-native Security Information Event Management (SIEM). [Azure Sentinel Watchlists](https://docs.microsoft.com/it-it/azure/sentinel/watchlists) is a preview feature that enable the collection of data from external data sources for correlation with the events in your Azure Sentinel environment.

The script `OSINTDS2SentinelWL.py` is a ready to use tool able to create and manage a Sentinel watchlist containing the IoCs shared by the project.

In order to use it, assuming you already have your Azure Sentinel instance up and running, please follow the instructions below.

## Microsoft Azure Configurations

* Create a new registered app in you tenant through the `Azure App Registrations`
* In the `API permissions` tab add the following permissions:
	
Category | Name | Type | Admin consent
-------- | ---- | ---- | -------------
Log Analytics API | Data.Read | Application | Yes
Microsoft Graph | SecurityActions.ReadWrite.All | Delegated | Yes
Microsoft Graph | SecurityActions.ReadWrite.All | Application | Yes
Microsoft Graph | SecurityEvents.ReadWrite.All | Delegated | Yes
Microsoft Graph | SecurityEvents.ReadWrite.All | Application | Yes

* Give the following roles through Azure RBAC to the `Resource Group` where the Sentinel workspace is mapped:
 * Azure Sentinel Contributor
 * Azure Sentinel Reader
 * Azure Sentinel Responder
 
**IMPORTANT**: make sure to give the app the least privileges required to run correctly the script, according your Organization's security policies. [More info](https://techcommunity.microsoft.com/t5/azure-sentinel/azure-sentinel-api-101/ba-p/1438928)
 
## Install required libraries

```
pip install adal==0.4.7
pip install azure-mgmt-datalake-analytics==0.2.0
```

 
## Configure the script

Once you Azure environment is configured, download the `OSINTDS2SentinelWL.py` file and open it with your preferred text editor.

Edit the variable value from `line 30` to `line 40`:

```
watchlist_alias = "osintds" #can change the default
displayName = "OSINT-DigitalSide.it" #can change the default
source = "https://osint.digitalside.it" #can change the default
description = "Watchlist from OSINT-Digitalside.it lists" #can change the default
tenant_id = "`<the Azure tenant id>`"
client_id = "`<the registered app client id>`"
client_secret = "`<the registered app client secret>`"
subscription_id = "`<your Azure subscription id>`"
resource_group = "`<the Resource Group where the Sentinel workspace is mapped>`"
workspace = "`<the name of the workspace used by Sentinel>`"
api_version = "2019-01-01-preview" #actual valid version
```

## Run the script

Give the script executable permission and run it.
Schedule the execution no more than one time a day, since the OSINT.digitalside.it repository is updated daily.

## Notes

The script increment the watchlist any time new IoC will be release by the service. To delete old entries, make your own procedure related to the retention policies of your Organization.
For more informations about Azure Sentinel watchlists API [refer to Microsoft documentation](https://docs.microsoft.com/it-it/azure/sentinel/watchlist-with-rest-api#add-or-update-a-watchlist-item).

