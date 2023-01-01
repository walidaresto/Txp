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

print "_|_ o  __   __|  ___   __    __   __|  __ __  o  __     __   __   __   ___  |   "

print " |  | |  ) (__| (__/_ |  '  (__( (__| |  )  ) | |  )   |__) (__( |  ) (__/_ |_, "

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
	Space(9); print "#   +Toxic Dz OFC   #"
	Space(9); print "#       Script by Toxic dz ofc       #"
	Space(9); print "#####################################"

Credit()
findAdmin()
