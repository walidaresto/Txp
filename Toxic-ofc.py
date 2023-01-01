#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Script by Toxic Dz OFC!!
#I Love Free fire!!
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

print "  _                                                                             "

print "_|_ o thes script by toxic dz ofc_|insta toxic_dz_ofc|   png and jpg picture finder on free fire  |   "

print " |  Toxic Tool |first tool of gettin link on free fire|please garena i need my old account hahaha, my UID is 48571916 "

print "                                                       |                        "

def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print (req_link)

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#    Script by Toxic dz ofc         #"
	Space(9); print "#     instagram @toxic_dz_ofc       #"
	Space(9); print "#####################################"

Credit()
findAdmin()
