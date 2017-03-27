# OpenConfig
Junipers Junos har hatt støtte for OpenConfig siden release 16.1, og har fått utvidet støtte i release 17.1.

> OpenConfig is a collaborative effort in the networking industry to move toward a more dynamic, programmable method for configuring and managing multivendor networks.
> OpenConfig supports the use of vendor-neutral data models to configure and manage the network. These datamodels define the configuration and operational state of network devices for common network protocols or services.
> The data models are written in YANG, a standards-based, data modeling language that is modular, easy to read, and supports remote procedure calls (RPCs). Using industry standard models greatly benefits anoperator with devices in a network from multiple vendors.
> The goal of OpenConfig is for operators to be able to use a single set of data models to configure and manage all the network devices that supportthe OpenConfig initiative.



# Krav for å kunne bruke OpenConfig på en Juniper-enhet
OpenConfig-modul må installeres på enheten som skal støtte OpenConfig. Gjøres på samme vis som når man skal installere Junos-versjon.
> request system software add junos-openconfig-x86-32-XX.YY.ZZ.JJ.tgz

NETCONF må aktiveres på enheten for å kunne kommunisere med enheten via RPC.
    system {
        services {
            netconf {
                ssh;
            }
        }
    }


# Linker
* http://openconfig.net
* [Juniper OpenConfig Feature Guide](https://www.juniper.net/techpubs/en_US/junos/information-products/pathway-pages/open-config/open-config-feature-guide.pdf)
* [OpenConfig on GitHub](https://github.com/openconfig/public)
* [Video on how to add OpenConfig BGP support on a Junos system](https://vimeo.com/139447948)
