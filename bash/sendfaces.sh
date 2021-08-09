#!/bin/bash

host=$HOSTNAME

/usr/bin/expect ./filetransfer.sh /home/pi/bin/faces/ $host
rm -r /home/pi/bin/faces/*
