"""
This tool will help a user cache data about an IP address and then look up the
cached information by subnet to alieveate multiple lookups to a source api.
"""

import ipaddress, pickle, os


class Table:
    """This class creates a table that will allow an indexed lookup into stored
    network data.
    """

    def __init__(self) -> None:
        self.lookupTable = {"version": 1, "v4": {}, "v6": {}}
        for number in range(32, 0, -1):
            self.lookupTable["v4"][number] = list()
        for number in range(64, 0, -1):
            self.lookupTable["v6"][number] = list()

    def add(self, entry: dict) -> bool:
        """Adds entry to lookup table.

        Args:
            entry (dict): Must contain two keys, network and data.
                Keys:
                network: Must be a ipaddress.ip_network variable.
                data: Should be a dict of data about the network, but can store anything.

        Returns:
            bool: Returns true if successful, and false if there is an issue.
        """

        assert isinstance(
            entry["network"], (ipaddress.IPv4Network, ipaddress.IPv6Network)
        ), False
        version = entry["network"].version
        version = f"v{version}"
        netmask = entry["network"].prefixlen

        try:
            self.lookupTable[version][netmask].append((entry["network"], entry["data"]))
            return True
        except:
            return False

    def query(self, ip: ipaddress.ip_address) -> dict:
        """Returns data about the network and IP address is in.

        Args:
            ip (ipaddress.ip_address): IP address to be queried.

        Returns:
            dict: dictionary about the network that the queried IP address is in.
        """
        version = ip.version
        version = f"v{version}"
        
        for netmask in self.lookupTable[version]:
            netList = self.lookupTable[version][netmask]
            for network in netList:
                if ip in network[0]:
                    return network[1]
        raise ValueError("Network not found.")
    
    def save(self, name = 'table.pickle'):
        with open(os.path.join(os.path.dirname(__file__), name), 'wb') as outfile:
            pickle.dump(self.lookupTable, outfile)
        return True

    def load(self, name = 'table.pickle'):
        with open(os.path.join(os.path.dirname(__file__), name), 'rb') as infile:
            self.lookupTable = pickle.load(infile)
        return True