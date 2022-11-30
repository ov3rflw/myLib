#!/bin/bash

for port in {1..254}; do (ping -c 1 172.19.0.${port} | grep "bytes from" | grep -v "Host Unreachable" &);done;
