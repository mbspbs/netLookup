import ipaddress, pytest
from netLookup import netLookup

def test_Table1():
    table = netLookup.Table()
    entry = {
        'network': ipaddress.ip_network('192.168.1.0/24'),
        'data': 'stuff'
    }
    table.add(entry)
    pass

def test_Table2():
    table = netLookup.Table()
    entry = {
        'network': ipaddress.ip_network('2600:100f:b000::/44'),
        'data': 'stuff'
    }
    table.add(entry)
    pass

def test_Table3():
    table = netLookup.Table()
    entry = {
        'network': 'foo',
        'data': 'stuff'
    }
    with pytest.raises(AssertionError):
        table.add(entry)
    
def test_Query1():
    table = netLookup.Table()
    entry = {
        'network': ipaddress.ip_network('2600:100f:b000::/44'),
        'data': 'stuff'
    }
    table.add(entry)
    ip = ipaddress.ip_address('2600:100f:b000:0100::100')
    data = table.query(ip)
    data == entry
    pass