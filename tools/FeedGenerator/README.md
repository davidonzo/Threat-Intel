# DigitalSide Threat-Intel Feed Generator

The script is coded to generate the same output three of [OSINT.digitalside.it](https://osint.digitalside.it/) project **quering your own [MISP](https://www.misp-project.org/) instance**.

Instructions: 

* Download the feedgenerator directory
* Configure the script editinn the `feedgeneratorconf.py` file
* Launch the script by typing `python3 /path/to/feedgenerator.py`
* All configured output will be generated according the given configuration

## How to configure

Open the `feedgeneratorcon.py` file using your preferred text editor (nano is a good choise, even if some chic unix user is glad to blame it...).

Edit the lines with your MISP url, the associated API key anche the choise for the certificate verification between `True` or `False`.
```
# Your MISP's URL. Refer to MISP setting MISP.external_baseurl
url = 'https://YOUR_MISP_URL'

# The auth key to the MISP user that you wish to use. Make sure that the
# user has auth_key access
key = 'YOUR_MISP_API_KEY'
# Should the certificate be validated?
ssl = False
```

Configure the output directories that must be created by hand before you'll run the script.

**Important**: the script won't create the missed directories, resulting in a fatal error during execution.
```
# Configure the output directories
# WARNING => Must be created manually. The script does not create them for you!
# The directory must ends with slash "/"
mispfeeddir = 'digitalside-misp-feed/'
csvdir = 'csv/'
stix2dir = 'stix2/'
listsdir = 'lists/'
```

Choose the enabled output to produce, the enabled lists to generate and the custom header to be printed in top of any enabled list.

**Important**: in order to enable lists creation the `enabled["list"]` dict item must be `True`.
```
#Enable or disable the feed creation by type. You can choose to enable the MISP feed, che CSV export, the STIX2 export and the lists generation.
enabled = {
		'mispfeed': True,
		'csv': True,
		'stix2': True,
		'lists': True		
		}

#Enable or disable lists by type	
listsenabled = {
			'domains': True,
			'ips': True,
			'urls': True,
			'piHole': True
		}

#Set the header for any list	
listsheader = {
		'domains': "###################\n## Your list header here.\n## The list contains set of domains\n######################",
		'ips': "###################\n## Your list header here.\n## The list contains set of domainsin piHole format\n######################",
		'urls': "###################\n## Your list header here.\n## The list contains set of IPs\n######################",
		'piHole': "###################\n## Your list header here.\n## The list contains set of URLs\n######################"
}
```

Configure the filters to be applied in data generation process.

**Note**: refer to the [official pymisp documentation page](https://pymisp.readthedocs.io/en/latest/modules.html#pymisp.PyMISP.search_index) for more information.
```
filters = {'published':'true', 'timestamp':'2d'}
```

Choose the applied attribute distribution leves.
```
# The levels are as follows:
# 0: Your Organisation Only
# 1: This Community Only
# 2: Connected Communities
# 3: All
# 4: Sharing Group
# 5: Inherit Event
valid_attribute_distribution_levels = ['0', '1', '2', '3', '4', '5']
```
