#!/bin/python
# V1 Skibooss (5/4/2014)
# V2 Skibooss (6/4/2014)
# V3 Skibooss + Nono (26/05/2016)

import os, yaml, sys

stream = open("/m0le-o-backup/custom.yaml", "r")
docs = yaml.load(stream)

def server_dir (server):
    folders = []
    if server in docs:
        folders = docs[server] 
    return folders  

handler = open('/m0le-o-backup/ip_syn','r')
ip_syno= handler.readline()

nas_folder="/path/to/backup/dest/folder"
listvm = os.popen("xm list | awk 'NR<2 { next } $5 ~ /^[r]|[-b]*$/ && $1 != \"Domain-0\" {print $1}'").read()
list_vm = listvm.strip().split('\n')

for vm in list_vm:
    folders = []
    custom_rep = server_dir(vm)
    folders = custom_rep
    default_rep =  server_dir('default')
    folders += default_rep
    for rep in folders:
        cmd_mkdir = "ssh "+ip_syno.strip()+" 'mkdir -p "+nas_folder+"/"+vm+rep.strip()+"'"
        print cmd_mkdir
        os.popen(cmd_mkdir)
        cmd = "ssh -A "+vm+" 'rsync -e \"ssh \" -arvz "+rep.strip()+"/* root@"+ip_syno.strip()+":"+nas_folder+"/"+vm+rep.strip()+"'"
        print cmd
        os.popen(cmd)
