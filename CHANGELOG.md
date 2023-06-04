# CHANGELOG 2023
| CHLID | Date	    | Type      | Details |
| - | --------- | :-------: | ------- |
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
