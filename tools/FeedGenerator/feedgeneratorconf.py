__author__ = "Davide Baglieri"
__credits__ = ["MISP Project"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Davide Baglieri"
__email__ = "info@digitalside.it"
__status__ = "Dev"

# Your MISP's URL. Refer to MISP setting MISP.external_baseurl
url = 'https://YOUR_MISP_URL'

# The auth key to the MISP user that you wish to use. Make sure that the
# user has auth_key access
key = 'YOUR_MISP_API_KEY'
# Should the certificate be validated?
ssl = False

# Configure the output directories
# WARNING => Must be created manually. The script does not create them for you!
# The directory must ends with slash "/"
mispfeeddir = 'digitalside-misp-feed/'
csvdir = 'csv/'
stix2dir = 'stix2/'
listsdir = 'lists/'


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
			'piHole': True,
			'hashes': True
		}

#Set the header for any list	
listsheader = {
		'domains': "###################\n## Your list header here.\n## The list contains set of domains\n######################",
		'ips': "###################\n## Your list header here.\n## The list contains set of domainsin piHole format\n######################",
		'urls': "###################\n## Your list header here.\n## The list contains set of IPs\n######################",
		'piHole': "###################\n## Your list header here.\n## The list contains set of URLs\n######################",
		'hashes': "###################\n## Your list header here.\n## The list contains the latest hashes lookup.\n######################"
}

# The filters to be used for by the feed. You can use any filter that
# you can use on the event index, such as organisation, tags, etc.
# It uses the same joining and condition rules as the API parameters
# For example:
# filters = {'tag':'tlp:white|feed-export|!privint','org':'CIRCL', 'published':1}
# the above would generate a feed for all published events created by CIRCL,
# tagged tlp:white and/or feed-export but exclude anything tagged privint
# Example filter to fetch published event by DIGITALSIDE.IT organization for the latest 7 days
# filters = {'published':'true', 'org':'DIGITALSIDE.IT', 'last':'7d'}
# The default filter extract all published events for the last 2 days.
# Docs => https://pymisp.readthedocs.io/en/latest/modules.html#pymisp.PyMISP.search_index
filters = {'published':'true', 'timestamp':'2d'}

# By default all attributes will be included in the feed generation
# Remove the levels that you do not wish to include in the feed
# Use this to further narrow down what gets exported, for example:
# Setting this to ['3', '5'] will exclude any attributes from the feed that
# are not exportable to all or inherit the event
#
# The levels are as follows:
# 0: Your Organisation Only
# 1: This Community Only
# 2: Connected Communities
# 3: All
# 4: Sharing Group
# 5: Inherit Event
valid_attribute_distribution_levels = ['0', '1', '2', '3', '4', '5']
