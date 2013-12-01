import requests
import json

from StringIO import StringIO



#DO NOT MESS WITH THE FOLLOWING HARD CODED INDEXES UNLESS YOU KNOW WHAT YOU ARE DOING AND BLOCKCHAIN.INFO HAS CHANGED ITS API
INPUTS = 0
HASH = 1
ADDRESS = 2 
TRANS_VALUE = 3
TIME = 7
OUT = 10 #Addresses that received btc in this transaction

def verifyHash(receive_address, trans_hash, value=None):

	URL= 'http://blockchain.info/tx-index/'
	params = { 'format': 'json'}
	URL = URL + trans_hash
	json_txt = requests.get(URL,params = params)
	io = StringIO(json_txt.text)
	json_io = json.load(io)
	keys = json_io.keys()
	
	out = json_io[keys[OUT]]
	counter  = 0

	while counter < len(out):
		address = str(out[counter]).find(receive_address)
		if address != -1:
			break
		counter = counter + 1

	keys = out[counter].keys()
	out = out[counter]

	address = out[keys[ADDRESS]]
	trans_value = float(out[keys[TRANS_VALUE]])



	if value == None:
		#print 'Transaction Value: ' + str(trans_value)
		return trans_value
	else:
		if value != trans_value:
			print 'Original Value Entered: ' + str(value)
			print 'Transaction Actual Value: ' + str(trans_value)


if __name__ == '__main__':
#The following are dummy, test values, should return 0.14905
	receive_address = '15LYSZvdF46MeV3MsxjU7XbTkGvQiATQX5'
	trans_hash = 'c7cb0ea5934b2019ef8aec3c4f2c0bb8b6b52cda751e51427a96c8e60a3a87e0'
	value = verifyHash(receive_address=receive_address, trans_hash=trans_hash)
	print str(value / 100000000) + 'BTC'
