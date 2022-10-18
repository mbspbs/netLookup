# netLookup

## Overview
This is a tool that will help limit calls to an IP address lookup tool by reusing data that had been previously collected.

It will take in an network with an arbitrary dataset and add it to a table for later use.

When an IP address is queried it will go through an indexed routing table and the first hit it recieves it will return the arbitrary dataset.
