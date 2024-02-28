#!/bin/python3

import sys
from os import system

file = sys.argv[1]

domains = open(f"{file}","r")

domain = domains.readline()

system("cowsay 'Let me get the subdoains'")
while domain:
    #Get the SubDomains
    system(f"subfinder -all -silent --domain {domain.strip()} -o {domain.strip()}.txt")
    system(f"cat {domain.strip()}.txt | httprobe | anew live_{domain.strip()}.txt")
    
    system(f"cat live_{domain.strip()}.txt | cut -d '/' -f3 | sort |uniq | anew active_{domain.strip()}")
    system(f"rm {domain.strip()}.txt live_{domain.strip()}.txt")


    domain = domains.readline()

domains.close()

system("cowsay 'Time to get bounty'")
