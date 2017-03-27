# OP scripts
OP-scripts (Junos Operational scripts) er scripts som enten lagres lokalt på enheten, eller hentes fra en sentral server ved eksekvering. Eksekvering utføres som en brukerstyrt kommando på enheten.

Et OP-script kjører kommandoer, sjekker output, og tar handlinger basert på outputen. Handlinger kan være å endre config på enheten, eller printe output på en spesifikk måte for å øke lesbarheten.

> Op scripts can be written in Python, Extensible Stylesheet Language Transformations (XSLT), or Stylesheet Language Alternative Syntax (SLAX). Op scripts use XML Path Language (XPath) to locate the operational objects to be inspected and automation script constructs to specify the actions to perform on the operational objects. The actions can change the configuration or output or execute additional commands based on the output.

OP-scripts var fra tidligere av skrevet i SLAX og XSLT, men fra Junos 16.1 er i tillegg Python støttet.

# Eksempel Op-script
Scriptet i dette eksempelet viser kun interfaces som har fått confet spesifikke adressefamilier. 
Inspirasjon/kode: [juniper.net](https://www.juniper.net/techpubs/en_US/junos/topics/example/junos-script-automation-op-script-customizing-output.html)

## Config for å tilgjengeliggjøre scriptet
    system {
        scripts {
            op {
                file interface-address-families.slax;
            }
        }
    }

## Hvor legges scriptet
Scriptet lagres i /var/db/scripts/op/ på enheten

## Scriptet - skrevet i SLAX
Op-scriptet ligger óg i helhet i denne mappa som [interface-address-families.slax]

    version 1.0;

    ns junos = "http://xml.juniper.net/junos/*/junos";
    ns xnm = "http://xml.juniper.net/xnm/1.1/xnm";
    ns jcs = "http://xml.juniper.net/junos/commit-scripts/1.0";
    import "../import/junos.xsl";
     
    var $arguments = {
        <argument> {
            <name> "interface";
            <description> "Name of interface to display";
        }
        <argument> {
            <name> "protocol";
            <description> "Protocol to display (inet, inet6)";
        }
    }
    param $interface;
    param $protocol;

    match / {
        <op-script-results> {
            var $rpc = {
                <get-interface-information> {
                    <terse>;
                    if ($interface) {
                        <interface-name> $interface;
                    }
                }
            }
            var $out = jcs:invoke($rpc);
            <interface-information junos:style="terse"> {
                if ($protocol='inet' or $protocol='inet6' or $protocol='mpls' or
                                   $protocol='tnp') {
                    for-each ($out/physical-interface/
                          logical-interface[address-family/address-family-name = $protocol]) {
                        call intf();
                    }
                } else if ($protocol) {
                    <xnm:error> {
                        <message> {
                            expr "invalid protocol: ";
                            expr $protocol;
                        }
                    }
                } else {
                    for-each ($out/physical-interface/logical-interface) {
                        call intf();
                    }
                }
            }
        }
    }
    intf () {
        var $status = {
            if (admin-status='up' and oper-status='up') {
            } else if (admin-status='down') {
                expr "offline";
            } else if (oper-status='down' and ../admin-status='down') {
                expr "p-offline";
            } else if (oper-status='down' and ../oper-status='down') {
                expr "p-down";
            } else if (oper-status='down') {
                expr "down";
            } else {
                expr oper-status _  '/' _  admin-status;
            }
        }
        var $desc = {
            if (description) {
                expr description;
            } else if (../description) {
                expr ../description;
            }
        }
        <logical-interface> {
            <name> name;
            if (string-length($desc)) {
                <admin-status> $desc;
            }
            <admin-status> $status;
            if ($protocol) {
                copy-of address-family[address-family-name = $protocol];
            } else {
                copy-of address-family;
            }
        }
    }
## Eksempeloutput på scriptet
    demo@ex4300> op interface-address-families protocol inet 
    Interface               Admin Link Proto    Local                 Remote
    pfe-0/0/0.16383                    inet
    pfh-0/0/0.16383                    inet
    bme0.0                             inet     128.0.0.1/2
                                                128.0.0.4/2     
                                                128.0.0.16/2    
                                                128.0.0.32/2    
    irb.0                              inet
    jsrv.1                             inet     128.0.0.127/2
    lo0.16385                          inet
    me0.0                              inet     192.168.22.126/24
    vme.0                   p-down     inet


# Linker
* [juniper.net: Op script overview](https://www.juniper.net/techpubs/en_US/junos/topics/concept/junos-script-automation-op-script-overview.html)
* [juniper.net: How Op Scripts Work](https://www.juniper.net/documentation/en_US/junos/topics/concept/junos-script-automation-op-script-works.html)
