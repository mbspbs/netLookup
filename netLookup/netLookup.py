"""
This tool will help a user cache data about an IP address and then look up the
cached information by subnet to alieveate multiple lookups to a source api.
"""

import ipaddress

class Table:
    """
    This class creates a table that will allow an indexed lookup into stored
    network data.
    """
    
    def __init__(self) -> None:
        routingTable = {}
        pass
    
    def add(self, data: dict) -> bool:
        print("Not yet implemented.")
        pass
    
    def query(self, ip: ipaddress.ip_address) -> dict:
        print("Not yet implemented.")
        pass