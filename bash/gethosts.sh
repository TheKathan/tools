#!/bin/bash

nmap -PN -p 9000 --open -oG - 192.168.1.* | awk '$NF~/tcp/{print $3}' > /var/www/host"
#sed -i 's/(//g' /var/www/hosts.txt
#sed -i 's/)//g' /var/www/hosts.txt
#sed -i 's/.lan//g' /var/www/hosts.txt
