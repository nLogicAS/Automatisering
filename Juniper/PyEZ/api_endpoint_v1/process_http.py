#!/usr/bin/env python3

#
# imports
#
from http.server import BaseHTTPRequestHandler
import re
import json

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys

#
# Global variables
#
netconf_username = 'xxx'
netconf_password = 'yyy'




#
# parse_url() function
#
def parse_url(url):
    '''
        Function used to find the type of URL the client is asking

	Accepted URL's:
            /<node>/interface_mtu/<interface>
            /<node>/route/<subnet>

    '''

    print('parsing %s' % url)
    match_strings = {
        '/([a-zA-Z0-9\-\.]+)/interface_mtu/([a-zA-Z0-9]+\-[0-9]+/[0-9]+/[0-9]+)': 'interface_mtu',
        '/([a-zA-Z0-9\-\.]+)/route/([a-fA-F0-9\:\.]+)': 'route'
    }

    for x, y in match_strings.items():
        match = re.findall(x, url)
        if len(match) == 1:
            print(' -> matching %s' % y)
            return {'type': y, 'params': match[0]}
    return

#
# xmlrpc() function
# will return a custom dictionary for each type
#
def xmlrpc(type, params = None):
    dev = Device(host=params[0], user=netconf_username, password=netconf_password).open()
    dev.open()

    #
    # route
    #
    if type == 'route':
        try:
            rsp = dev.rpc.get_route_information(destination=params[1])
            nh = []
            for rsp_xpath in rsp.xpath("//route-information/route-table/rt"):
                prefix = rsp_xpath.find('rt-destination').text
                for rsp_xpath in rsp.xpath("//route-information/route-table/rt/rt-entry/nh"):
                    nh.append(rsp_xpath.find('to').text)
            # return variables        
            ret = {}
            ret['status'] = 'ok'
            ret['data'] = {}
            ret['data']['prefix'] = prefix
            ret['data']['next_hop'] = nh
        except Exception:
            # not a good practice to "catch all"
            ret = {}
            ret['status'] = 'error'
        return ret
    #
    # interface_mtu
    #
    elif type == 'interface_mtu':
        try:
            rsp = dev.rpc.get_interface_information(interface_name=params[1])
            for rsp_xpath in rsp.xpath("//interface-information/physical-interface"):
                mtu = rsp_xpath.find('mtu').text
            # return variables        
            ret = {}
            ret['status'] = 'ok'
            ret['data'] = {}
            ret['data']['mtu'] = int(mtu.strip())
        except Exception:
            # not a good practice to "catch all"
            ret = {}
            ret['status'] = 'error'
        return ret




#
# handler for "HTTPServer"
#
class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parse_result = parse_url(self.path)
        if parse_result != None:
            print(parse_result)
            result = xmlrpc(parse_result['type'], parse_result['params'])
            
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))

#
# MAIN
#
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
