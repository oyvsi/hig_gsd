#!/usr/local/bin/python

import datetime
import time
import sys
import logging
from dop.client import Client

logger = logging.getLogger(__name__)

class DOBackup:
	def __init__(self, api_key, client_id): 
		logger.debug("Initializing DOBackup object")
		self.client = Client(client_id, api_key)
		self.droplets = self.client.show_active_droplets()

	def shutdown(self, droplet):
		status = self.client.show_droplet(droplet.id) 
		if(status.status != "off"):
			self.client.shutdown_droplet(droplet.id) 

		i = 1
		while(status.status != "off"):
			logger.info("Waiting for droplet " + droplet.name + " to shutdown...")
			time.sleep(10)	
			status = self.client.show_droplet(droplet.id) 
			if(i > 15):
				return False
			i+=1
		return True

	def backup(self, droplet):
		if(self.shutdown(droplet) == False):
				sys.exit("Timeout while waiting for droplet " + droplet.name + " to shutdown")
		snapshot_name = droplet.name + "_" + datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') 
		logger.info("Asking to create snapshot " + snapshot_name)
		self.client.snapshot_droplet(droplet.id, snapshot_name) 	

	def backup_all(self):
		for droplet in self.droplets:
			self.backup(droplet)

def main():
	do = DOBackup(config["api_key"], config["client_id"])
	do.backup_all()

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	config = {}
	execfile("backup_do.conf", config) 

	main()
