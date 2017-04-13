# Notater for installering av PyEZ
1) Installere en clean versjon av debian.
2) sudo apt-get update
3) sudo apt-get install python-dev build-essential libssl-dev libffi-dev python3-dev
4) wget https://bootstrap.pypa.io/get-pip.py -O - | sudo python
5) wget https://bootstrap.pypa.io/get-pip.py -O - | sudo python3
6) Putt følgende i en fil på debian-installasjonen og kjør den med `python <fil>` eller `python3 <fil>` for å teste at du får data inn via PyEZ-biblioteket.

    from pprint import pprint
    from jnpr.junos import Device
    dev = Device(host='IP', user='BRUKER', password='PASSORD' )
    dev.open()
    pprint( dev.facts )
    dev.close()

IP, BRUKER og PASSORD skiftes til det du skal teste mot.


## Config som må inn på Juniper-noden for å få NETCONF (og dermed PyEZ) til å fungere
    system {
        services {
            ssh;
            netconf {
                ssh;
            }
        }
    }

## Kilder
* https://github.com/Juniper/py-junos-eznc
* https://github.com/Juniper/py-junos-eznc/blob/master/INSTALL-UBUNTU-DEBIAN.md
* http://stackoverflow.com/questions/35144550/how-to-install-cryptography-on-ubuntu
