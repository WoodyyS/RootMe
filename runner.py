#coding:utf-8

import rootme
import sys
import colorama

class Optionnal:
	def __init__(self):
		'''
			I call the options in the params
			file and testing variable
		'''
		self.USER  = rootme.USER
		self.LANG  = rootme.LANG
		self.CHAT  = rootme.CHAT
		self.STAT  = rootme.STAT
		self.CHAL  = rootme.CHAL
		self.MACH  = rootme.MACH
		self.POINT = rootme.POINT

	def __str__(self):
		'''
			Here we will test our variables
			and go the necessary functions.
		'''
		if(self.LANG != None):
			sys.exit(rootme.PollersLangs())

		elif(self.CHAT != None):
			sys.exit(rootme.PollersChat())

		# So concretely here we will test the variables and options.
		# The options are call in the params.py file.

		elif(self.STAT != None):
			sys.exit(rootme.PollersStatus())

		elif(self.CHAL != None):
			sys.exit(rootme.PollersChallenge())

		# In the conditions we call the functions and
		# then execute that on the servers 

		elif(self.POINT != None):
			sys.exit(rootme.PollersPoint())

		elif(self.MACH != None):
			sys.exit(rootme.PollersMachines())
