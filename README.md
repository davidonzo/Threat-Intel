# DigitalSide Threat-Intel
This repository cointains a set of Open Source Cyber Threat Intellegence information, monstly based on malware analysis and compromised URLs, IPs and domains.

The purpose of this project is to develop and test new wayes to hunt, analyze, collect and share relevants sets of IoCs to be used by SOC/CSIRT/CERT with minimun effort.

## Sharing formats
Three formats are availables to download the reports:

* [MISP](https://www.misp-project.org/) feed and events (retention: 7 days) - [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/digitalside-misp-feed)
* Structured Threat Information Expression - [STIX™ v2](https://oasis-open.github.io/cti-documentation/stix/intro.html) (retention: 30 days) [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/stix2)
* Comma Separated Values (retention: 30 days) [[GO TO]](https://github.com/davidonzo/Threat-Intel/tree/master/csv)
* IoC lists of uniques indicators in squid like format (retention: 7 days) splitted in:
* * [URLs](https://osint.digitalside.it/Threat-Intel/lists/latesturls.txt)
* * [IPs](https://osint.digitalside.it/Threat-Intel/lists/latestips.txt)
* * [Domains](https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt)

The majority of the informations are stored in the MISP data format. So, best way to collect data is subscribe the [Digitalside-misp-feed](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/).
All sharing formats are based on MISP export format. **All reports in any format can be consumed by any up-to-dated MISP instance**.

## Sharing endpoints
Reports shared by two sharing endpoints:
* This repository: you can clone, subscribe, download managing it with the power of git!
* [OSINT.DigitalSide.it](https://osint.digitalside.it): You can crawl it for free and permit you to subscribe the MISP feed.

## How to subscribe the [Digitalside-misp-feed](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/)
Since 2019-09-23 OSINT.digitalside.it MISP feed has been added to the "Default feeds" list availables in MISP default installation. The esasy way to subscribe the feed is select the dedicated activation button.

1. Login to MISP with a user having the right permissions to manage feeds
2. Go to `Sync Actions -> List Feeds -> Default feeds`
3. Find the OSINT.digitalside.it row
![DigitalSide MISP Feed](https://raw.githubusercontent.com/davidonzo/host/master/list.png)
4. Select the row and click on "Enable selected" button at the top of the table<br>
![List feeds](https://raw.githubusercontent.com/davidonzo/host/master/button.png)

You can also subscribe the feed manually, following the below instructions.

1. Login to MISP with a user having the right permissions to manage feeds
2. Go to `Sync Actions -> List Feeds -> Add Feed`
3. Add the MISP feed by using the URL https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/

![DigitalSide MISP Feed](https://raw.githubusercontent.com/davidonzo/host/master/digitalsidemispfeed.png)

## Public API
Please visit the [DigitalSide API project page](https://github.com/davidonzo/apiosintDS).

## Sharing samples
Malware samples are not included in the reports. If you need some binary file for further analysis and investigation send an email to info[at]digitalside.it, qualifing yourself as member of a SOC/CSIRT/CERT or other cyber security organization working on public safety. No commercial company will be supported at all.

Only PGP signed and encrypted emails from a valid sender will have feedback.

My PGP key ID [30B31BDA](http://pgp.key-server.io/pks/lookup?op=get&search=0x9C3693B230B31BDA). Fingerpring: [0B4C F801 E8FF E9A3 A602 D2C7 9C36 93B2 30B3 1BDA](https://pgp.key-server.io/pks/lookup?op=get&search=0x9C3693B230B31BDA).

## Workflow Automation Input/Output
Reports shared here are the result of my personal Malware Analisys Lab. In this first stage of the project I'll focus the activity in find the best way to share IoC. Report contents should change in time. Anyway, backward compatibility will be granted. The goal is create an external know how to be used for correlation, digital forensics activities, threat intelligence processes, inside a workflow automation process for Incident Response. 

In a second phase I'll share information about my Malware Analisys Lab. This way I hope to cover the two main IoC sharing topics:
* How to use OSINT data
* How to produce OSINT data

## Credits are granted!
Many reports shared are based on OSINT and CLOSINT sources. All applicables credits are granted. If something wrong, please contact me at info[at]digitalside[dot]it.

## About Me
My name is Davide Baglieri and I'm an indepented security researcher and consultant. You can find more information at the following links:
* [LinkedIn](https://www.linkedin.com/in/davidebaglieri/)
* [Twitter](https://twitter.com/davidonzo)

My personal purpose about this project is basically for Research & Developing in a continue education and training process I started the 23th of September 1979.
