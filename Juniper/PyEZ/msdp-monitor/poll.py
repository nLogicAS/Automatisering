from lxml import etree
from jnpr.junos import Device
import datetime
from pprint import pprint

#
# Custom functions
#
def log(msg):
    date = datetime.datetime.now().isoformat()
    log_file = open('log.txt', 'a')
    log_file.write('%s: %s\n' % (date, msg))
    print('%s: %s' % (date, msg))
    log_file.close()

def pprint_msdp(input):
    return 'multicast-group-address %s -> multicast-source-address %s' % (input.split('-')[0], input.split('-')[1])

#
# Connect to Junos host and run XML RPC over NetCONF
#
log('Connecting to MSDP source')
dev = Device(host='1.1.1.1', user='j')
dev.open()
rsp = dev.rpc.get_msdp_source_active_information(local=True)


#
# Fetch previous MSDP sources into list
#
try:
    with open('temp') as f:
        prev_sources = [x.replace('\r', '').replace('\n', '') for x in f.readlines()]

except:
    prev_sources = []


#
# Fetch current MSDP sources into list (and also save them into the file "temp"
#
current_file = open('temp', 'w')
current_sources = []
for rsp_xpath in rsp.xpath("//msdp-source-active-information/msdp-instance/msdp-route"):
    mcga = rsp_xpath.find('multicast-group-address').text
    mcsa = rsp_xpath.find('multicast-source-address').text
    temp_value = '%s-%s' % (mcga, mcsa)
    temp_value = temp_value.replace('\r', '').replace('\n', '')
    current_sources.append('%s' % temp_value)
    current_file.write('%s\n' % temp_value)
dev.close()
current_file.close()


#
# Compare revisions
#
log('Comparing MSDP sources')
prev_sources_temp = []
current_sources_temp = []
for item in prev_sources:
    item = item.strip()
    if item not in current_sources:
        prev_sources_temp.append(item)

for item in current_sources:
    item = item.strip()
    if item not in prev_sources:
        current_sources_temp.append(item)

if len(prev_sources_temp) > 0:
    for item in prev_sources_temp:
        item = item.strip()
        log('The following MSDP active route have been removed: %s' % pprint_msdp(item))

if len(current_sources_temp) > 0:
    for item in current_sources_temp:
        item = item.strip()
        log('The following MSDP active route have been added: %s' % pprint_msdp(item))

if len(current_sources_temp) == 0 and len(prev_sources_temp) == 0:
    log('No changes')
