# CHANGELOG 2024 #1
| ID | Date         | Type      | Details |
|:-:| --------- | :-------: | ------- |
| 1 | 2024-06-02 | **ADDED** | Added OSINT enrichments data to `core system` |
| 2 | 2024-06-02 | **CHANGED** | `VirusTotal` data ingestion |
| 3 | 2024-06-02 | **ADDED** | Data enrichment to [MISP events](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/) (where available) added as `Tag` attributes |
| 4 | 2024-06-02 | **ADDED** | Data enrichment to [HTML](https://osint.digitalside.it/report/) and [STIX2](https://osint.digitalside.it/Threat-Intel/stix2/) reports (where available). Enrichment has been added as `labels` attribute attached to the `Report` object |
| 5 | 2024-06-02 | **IMPROVED** | STIX reports available via [TAXII server](https://osint.digitalside.it/taxiiserver.html) can be filtered by `Report:labels` |



# CHANGELOG 2023 #4
| ID | Date	    | Type      | Details |
|:-:| --------- | :-------: | ------- |
| 1 | 2023-06-22 | **FIXED** | TAXII2 Endpoint moved to `https://osint.digitalside.it/taxii2reports/` |
| 2 | 2023-06-22 | **ADDED** | New TAXII2 collection added: `OSINT.DigitalSide.it Network IoCs Collected (24h)` | 
| 3 | 2023-06-22 | **CHANGED** | IoCs included in `lists/latestdomains.json`, `lists/latestips.json` and `lists/latesturls.json` are coordinated with reports included in `stix2` directory in a way the `STIXOBJECT.id` is persistence even if included in different reports. This should help against unwanted data duplication |
| 4 | 2023-06-22 | **ADDED** | Added 3 new lists in STIX2.1 format related to the Newtwork IoCs collected in the latest 24 hours. Lists are `lists/latestdomainsdaily.json`, `lists/latestdomainsdaily.json` and `lists/latestdomainsdaily.json`. They are also used as source for the `OSINT.DigitalSide.it Network IoCs Collected (24h)` TAXII2 collection |
| 5 | 2023-06-22 | **ADDED** | New example script file to interact with the `OSINT.DigitalSide.it Network IoCs Collected (24h)` TAXII2 collection => [`taxiigetdomains.py`](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/taxiigetdomains.py) |
| 6 | 2023-06-22 | **CHANGED** | Updated local [README.md](https://github.com/davidonzo/Threat-Intel/blob/master/tools/TAXII2/README.md) and official website [TAXII2 support page](https://osint.digitalside.it/taxiiserver.html) |

## CHANGELOG 2023 #3
| ID | Date         | Type      | Details |
|:-:| --------- | :-------: | ------- |
| 1 | 2023-06-16 | **ADDED** | TAXII2 server. For details please read the instructions pages available on [this repository](https://github.com/davidonzo/Threat-Intel/tree/master/tools/TAXII2/README.md) and on the official [project website](https://osint.digitalside.it/taxiiserver.html) |
| 2 | 2023-06-10 | **CHANGED** | Example python [scripts to interact](https://github.com/davidonzo/Threat-Intel/tree/master/tools/TAXII2/) with the TAXII server |


## CHANGELOG 2023 #2
| ID | Date	    | Type      | Details |
|:-:| --------- | :-------: | ------- |
| 1 | 2023-06-10 | **FIXED** | HOST and DOMAIN indicators duplicated in single report |
| 2 | 2023-06-10 | **CHANGED** | Outdated indicators, based on `valid_until` datetime, are removed from [STIX2](https://osint.digitalside.it/Threat-Intel/stix2/) report. Full list with no retention is available via [MISP Feed subscription](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/) | 
| 3 | 2023-06-10 | **ADDED** | STIX object `Malware` added to the report, with external references to OSINT.DigitalSide.it [report page](https://osint.digitalside.it/report/) and, when available, the [VirusTotal](https://www.virustotal.com/) report page and detection ratio |
| 4 | 2023-06-10 | **ADDED** | STIX objects `Relationship` added. `Indicators <=> ObservedData` and `Indicators <=> Malware` |
| 5 | 2023-06-10 | **FIXED** | Enabled JSON indentation STIX reports |
| 6 | 2023-06-10 | **ADDED** | Minor changes on `Identity` |

## CHANGELOG 2023 #1
| ID | Date	    | Type      | Details |
|:-:| --------- | :-------: | ------- |
| 1 | 2023-06-04| **ADDED** | File MIME type now included in the [online reports](https://osint.digitalside.it/report/) |
| 2 | 2023-06-04| **FIXED** | File MIME type now included in [STIX2 reports](https://osint.digitalside.it/Threat-Intel/stix2/). No more extended file type in the STIX `File.mime_type` attribute |
| 3 | 2023-06-04| **FIXED** | All IDs generated in any STIX2 report are now immutable. Even if an update is applied to an existing STIX2 file, previous generated IDs related to Bundle, Report, ObservedData and Indicator objects won't be updated, so you can use `STIXOBJECT.id` with an hight level of confidence |
| 4 | 2023-06-04| **ADDED** | Indicator objects included in STIX2 files now have the `valid_until` date available. As policy the `valid_until` date is 7 days grater than the `valid_from` field |
| 5 | 2023-06-04| **FIXED** | [Project whitelisted domains](https://github.com/davidonzo/Threat-Intel-Domain-WL) included in STIX2 reports are highlighted with the following description: `Domain included in the Osint.DigitalSide.IT whitelist. Possible false positive` |
| 6 | 2023-06-04| **FIXED** | [Project whitelisted domains](https://github.com/davidonzo/Threat-Intel-Domain-WL) included in MISP events are shared with the `"to_ids" : False` flag configured, plus a standard comment: `Domain listed as False Positive in OSINT.DigitalSide.IT whitelist` |
| 7 | 2023-06-04| **FIXED** | Dozens of minor bug fix |

## CHANGELOG (Archived)
* 2019-05-15: source tag now includes reference to the OSINT source for automated download via crawling
* 2019-05-15: updated link to VirusTotal to the new default permalink
* 2019-05-15: added support to virustotal report update on backend and frontend
* 2019-09-23: OSINT.digitalside.it MISP feed added to the default feeds list available in MISP default (https://github.com/MISP/MISP/pull/5200)
* 2019-09-25: added PE sections analysis for the PE Executable files 
* 2019-09-28: retention restricted to 7 days for all formats
* 2019-10-04: updated https://osint.digitalside.it
* 2019-10-04: Added lists of uniques IPs, domains and urls collected in squid like format
* 2019-10-04: updated GitHub repository README.md file
* 2019-10-13: Added new API version https://github.com/davidonzo/apiosintDS
