#!/usr/bin/python
# -- coding: utf-8 --

import SOAPpy
from SOAPpy import Types
from rand import genPass
from create_shell import createShellUser
soap = SOAPpy.WSDL.Proxy('http://localhost:8083/rpc/soap/jirasoapservice-v2?wsdl')
jirauser="oyvsi"
passwd=""
auth = soap.login(jirauser, passwd)

def genUserName(name):
	parts = name.split()
	userName = parts[0][:3] + parts[-1][:2]

	return userName.lower() 

def userExist(userName):
	return soap.getUser(auth, userName)

def newUser(name, email):
	i = 2
	userName = genUserName(name)
	origName = userName
	while(userExist(userName)):
		userName = origName + str(i) 
		if(i > 10):
			exit("Error in gen username. Ended on " + name)
		i += 1
	password = genPass(2)
	user = soap.createUser(auth, userName, password, name, email)
	#def createShellUser(name, userName, password):
	createShellUser(name, userName, password)	
	print "Added user for %s (%s:%s)" % (name, userName, password)

	return user

newUser("Nils Slaen", "spam@bot.com")
