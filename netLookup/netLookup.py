"""
This tool will help a user cache data about an IP address and then look up the
cached information by subnet to alieveate multiple lookups to a source api.
"""

import ipaddress


class Table:
    """This class creates a table that will allow an indexed lookup into stored
    network data.
    """
    
    def __init__(self) -> None:
        self.lookupTable = {"v4": {}, "v6": {}}
        for number in range(32,8,-1):
            self.lookupTable['v4'][number] = list()
        for number in range(64,12,-1):
            self.lookupTable['v6'][number] = list()
    
    def add(self, data: dict) -> bool:
        print("Not yet implemented.")

        pass
    
    def query(self, ip: ipaddress.ip_address) -> dict:
        print("Not yet implemented.")
        pass
