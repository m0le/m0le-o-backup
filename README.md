m0le-o-backup
=============

m0le-o-backup is a simply backup script using rsync & python (with bash component).

***Purpose:***

The purpose of the script is to list the current running Xen VM, 
backup them following the yaml instruction file and sent them to a NAS Synology.


***How to install:***

* Copy *send_ip.sh* on your NAS Sylogy and create a scheduled task
* Copy *backup_to_syno.py* & *custom.yaml* on your server


***How it works:***
* *send_ip.sh*: Send his public IP (using curl) to the server
* *backup_to_syno.py*:
	* List the running VM (using xm list)
	* Read the backup instruction from the yaml file
	* Send the selected folders to the NAS Synology (using rsync)
* *custom.yaml*: List the selected folders for all and specifics VM.
