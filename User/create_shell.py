#!/usr/bin/python

import os
import crypt

if os.getuid() != 0:
	exit("Must be run with root privileges")


def createShellUser(name, userName, password):
	encPass = crypt.crypt(password,"22")
	os.system("useradd -c \"%s\" -p \"%s\" \"%s\" -m -s \"/bin/bash\"" % (name, encPass, userName))
