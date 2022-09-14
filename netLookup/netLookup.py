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
        for number in range(32, 8, -1):
            self.lookupTable["v4"][number] = list()
        for number in range(64, 12, -1):
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
        print("Not yet implemented.")
        pass
