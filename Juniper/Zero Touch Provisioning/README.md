# Hva er Zero Touch Provisioning (ZTP)
Det er muligheten for fabrikknytt/zeroized utstyr til å få tildelt config og eventuell software image via DHCP-options.

En usecase er å slippe å forhåndskonfigurere utstyr som skal ut til kunder/i eget nett. Spart tid, og eventuelle local spares kan installeres av installatør som ikke kan Junos.

# Støttet utstyr
Per 2017-04-27 støtter følgende Juniper-utstyr å bli Zero Touch Provisioned:
* EX2200
* EX2200-C
* EX2300
* EX3200
* EX3300
* EX3400
* EX4200
* EX4300
* EX4500
* EX4550
* MX5
* MX10
* MX40
* MX80
* MX104
* MX240
* MX480
* MX960
* MX2010
* MX2020
* NFX250
* OCX1100
* QFX3500
* QFX3600
* QFX5100
* QFX5110
* QFX5200
* QFX10002

Listen kommer fra https://pathfinder.juniper.net

# Hvordan foregår Zero Touch Provisioning?
1. Boks med ZTP-støtte booter
1. DHCP-prosessen på boksen starter opp og begynner å sende DHCP DISCOVER-pakker
1. Om en DHCP-server tilbyr, og gjennomfører, en DHCP-transaksjon med riktige DHCP-verdier satt så starter ZTP-prosessen
1. Boksen henter da config via protokoll satt av DHCP-serveren (FTP, TFTP, HTTP), og eventuelt software image
1. Config committes, eventuelt software-image installeres.
