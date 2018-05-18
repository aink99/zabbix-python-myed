#!/usr/bin/python
#Set connect and read timeout for ZabbixAPI requests
import sys
import logging
from pyzabbix import ZabbixAPI

#Debug
#stream = logging.StreamHandler(sys.stdout)
#stream.setLevel(logging.DEBUG)
#log = logging.getLogger('pyzabbix')
#log.addHandler(stream)
#log.setLevel(logging.DEBUG)
print ""

# Check if it has a less the argument no arguments count for 1
if len(sys.argv) < 2:
                # Print usage %s is denfine outside de quotes has aarguments 0 the script
	print("Usage: %s [enable of disable or list]" % sys.argv[0] )
        sys.exit()



# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://10.30.10.151'

# Timeout (float) in seconds
# By default this timeout affects both the "connect" and "read", but
# if you are using Requests library > v2.4.0 you can specify the timeout as a tuple (connect, read)
# to set individual timeouts.
TIMEOUT = 3.5


zapi = ZabbixAPI(ZABBIX_SERVER,timeout=TIMEOUT)

# Login to the Zabbix API
#zapi.login('api_username', 'api_password')
zapi.login('admin', 'Adm1nz@bbix!')
# Or you can re-define it after
zapi.timeout=TIMEOUT
print "Connected to Zabbix REGINA API Version %s" % zapi.api_version()

#for h in zapi.host.get(output="extend"):
#    print h['hostid']

#print sys.argv[1]
#Disable mediatype 1
if sys.argv[1] == "disable":
	zapi.mediatype.update(mediatypeid="1",status="1")

#enable mediatyp 1
if sys.argv[1] == "enable":
	zapi.mediatype.update(mediatypeid="1",status="0")

#List all media type  0 for  andble 1 for disable
for MEDIA in zapi.mediatype.get(output="extend"):
    #print MEDIA
   #print MEDIA['description'] , MEDIA['status'] , MEDIA['mediatypeid']
    print "NAME:",MEDIA['description']
    print "Media ID:",MEDIA['mediatypeid']
    if  MEDIA['status'] == '0':
        print MEDIA['description'],"is Enabled"
    else:
    	print MEDIA['description'],"is Disabled"


