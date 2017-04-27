# Forklaring
Det vi ser er en pakkedump som er tatt mellom DHCP relay (10.0.100.1) og DHCP server (10.0.100.2).

DHCP-serveren responderer med Option 43 (vendor specific) og 150 ("tftp server"). Option 43 angir configplassering, overføringsmetode og eventuelt Junos-image. Option 150 angir hvilken IP den serveren som holder config og image har.
