# DigitalSide Threat-Intel
This repository contains a set of Open Source Cyber Threat Intelligence information, mostly based on malware analysis and compromised URLs, IPs and domains.

The purpose of this project is to develop and test new ways to hunt, analyze, collect and share relevant sets of IoCs to be used by SOC/CSIRT/CERT with minimum effort.

## Sharing formats
Three formats are available to download the reports:

* [MISP](https://www.misp-project.org/) feed and events (retention: 7 days) - [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/digitalside-misp-feed)
* Structured Threat Information Expression - [STIX™ v2](https://oasis-open.github.io/cti-documentation/stix/intro.html) (retention: 30 days) [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/stix2)
* Comma Separated Values (retention: 30 days) [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/csv)
* [Public API](https://apiosintds.readthedocs.io) using [apiosintDS](https://github.com/davidonzo/apiosintDS) library - [[DOCS]](https://apiosintds.readthedocs.io)
* IoC lists of unique indicators in squid like format (retention: 7 days) splitted in:
* * [URLs](https://osint.digitalside.it/Threat-Intel/lists/latesturls.txt)
* * [IPs](https://osint.digitalside.it/Threat-Intel/lists/latestips.txt)
* * [Domains](https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt)
* [TAXII2](https://oasis-open.github.io/cti-documentation/resources#taxii-21-specification) server implementation containing STIX2 bundles shared reports (retention: 24 hours) - [[GO TO]](https://osint.digitalside.it/taxiiserver.html)
* [apiosintDS MISP Module](https://github.com/MISP/misp-modules) available in any up to dated MISP instance - [[DOCS]](https://apiosintds.readthedocs.io/en/latest/userguidemisp.html)

The majority of the information is stored in the MISP data format. So, best way to collect data is to subscribe to the [Digitalside-misp-feed](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/).

All sharing formats, except for STIX2.1 reports, are based on MISP export format. **All reports in any format can be consumed by any up-to-dated MISP instance**.

## Sharing endpoints
Reports shared by two sharing endpoints:
* This repository: you can clone, subscribe, download managing it with the power of git!
* [OSINT.DigitalSide.it](https://osint.digitalside.it): You can crawl it for free and permit you to subscribe tp the MISP feed.

## How to subscribe to the [Digitalside-misp-feed](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/)
Since 2019-09-23 OSINT.digitalside.it MISP feed has been added to the "Default feeds" list available in MISP default installation. The easy way to subscribe to the feed is to select the dedicated activation button.

1. Login to MISP with a user having the right permissions to manage feeds
2. Go to `Sync Actions -> List Feeds -> Default feeds`
3. Find the OSINT.digitalside.it row
![DigitalSide MISP Feed](https://raw.githubusercontent.com/davidonzo/host/master/list.png)
4. Select the row and click on "Enable selected" button at the top of the table<br>
![List feeds](https://raw.githubusercontent.com/davidonzo/host/master/button.png)

You can also subscribe to the feed manually, following the below instructions.

1. Login to MISP with a user having the right permissions to manage feeds
2. Go to `Sync Actions -> List Feeds -> Add Feed`
3. Add the MISP feed by using the URL https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/

![DigitalSide MISP Feed](https://raw.githubusercontent.com/davidonzo/host/master/digitalsidemispfeed.png)

## Domain white list and MISP Warning List
For more information about domain white list applied to the project, please refer to [OSINT.DigitalSide.IT Threat-Intel Domains White List](https://github.com/davidonzo/Threat-Intel-Domain-WL).

## Public API
Please visit the [DigitalSide-API project page](https://github.com/davidonzo/apiosintDS).

## Sharing samples
Malware samples are not included in the reports. If you need some binary file for further analysis and investigation, send an email to info[at]digitalside.it, qualifying yourself as member of a SOC/CSIRT/CERT or other cyber security organization working on public safety. No commercial company will be supported at all.

Only PGP signed and encrypted emails from a valid sender will have feedback.

My PGP key ID [30B31BDA](http://pgp.key-server.io/pks/lookup?op=get&search=0x9C3693B230B31BDA). Fingerprint: [0B4C F801 E8FF E9A3 A602 D2C7 9C36 93B2 30B3 1BDA](https://pgp.key-server.io/pks/lookup?op=get&search=0x9C3693B230B31BDA).

## Workflow Automation Input/Output
Reports shared here are the result of my personal Malware Analysis Lab. In this first stage of the project I'll focus the activity to find the best way to share IoC. Report contents should change in time. Anyway, backward compatibility will be granted. The goal is to create an external know how to be used for correlation, digital forensics activities, threat intelligence processes, inside a workflow automation process for Incident Response. 

In a second phase I'll share information about my Malware Analysis Lab. This way I hope to cover the two main IoC sharing topics:
* How to use OSINT data
* How to produce OSINT data

## Credits are granted!
Many reports shared are based on OSINT and CLOSINT sources. All applicable credits are granted. If something wrong, please contact me at info[at]digitalside[dot]it.

## About Me
My name is Davide Baglieri and I'm an independent security researcher and consultant. You can find more information at the following links:
* [LinkedIn](https://www.linkedin.com/in/davidebaglieri/)
* [Twitter](https://twitter.com/davidonzo)

My personal purpose about this project is basically for Research & Developing in a continue education and training process I started the 23rd of September 1979.
