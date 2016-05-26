#!/bin/ash
curl http://ip.tyk.nu > /volume1/script/ip 2>/dev/null
scp /volume1/script/ip root@hostname:/home/ip_syn
