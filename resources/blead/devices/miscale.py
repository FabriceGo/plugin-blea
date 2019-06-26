from bluepy.btle import Scanner, DefaultDelegate, Peripheral
import time
import logging
import globals
import struct

class MiScale():
	def __init__(self):
		self.name = 'miscale'
		self.ignoreRepeat = False

	def isvalid(self,name,manuf='',data='',mac=''):
		if name[0:8] == 'MI_SCALE':
			return True

	def parse(self,data,mac,name,manuf):
		action={}
		action['present'] = 1
		if data[4:6] in ['22','12','03']:
			logging.debug('Miscale this is a real measure')
			measured = round(int((data[8:10] + data[6:8]), 16) * 0.01 / 2,2)
			action['poids'] = measured
		else :
			logging.debug('MISCALE------Miscale this is a dummy measure')
		return action

globals.COMPATIBILITY.append(MiScale)
