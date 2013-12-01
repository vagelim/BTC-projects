import requests
import json


from StringIO import StringIO

#CRUCIAL NOTE:
#All of these hardcoded indexes are for keys when pulling from blockchain.info/address
INPUTS = 1 #constants for location in list
HASH = 2

url = 'http://blockchain.info/address/'
params = { 'format': 'json'}

def transactionHash(send_address=None, receive_address=None):
	if receive_address == None and value == None:
		return -1

	URL = url + receive_address

	json_txt = requests.get(URL, params=params)
	#print json_txt.text
	io = StringIO(json_txt.text)
	json_io = json.load(io)
	#print json_io
	transactions = json_io['txs']

	#get transactionID

	length = len(transactions)
	keys = transactions[0].keys()
	counter = 0
	location = 0
	index = None

	#for each transaction, search the "u'inputs' for the send_address
	#print 'Searching for address'
	while counter < length:
		address_location= str(transactions[counter][keys[INPUTS]]).find(send_address)
		if address_location > -1:
			index = counter
			#print 'Found address in ' + str( index)
			break
		counter = counter + 1
	
	if index == None :
		print 'Address Not Found'
		return -1

	#print 'Hash found'
	trans_hash = transactions[index][keys[HASH]]
	print trans_hash
	return trans_hash

if __name__ == "__main__":
  """The following are just test addresses that should return 'c7cb0ea5934b2019ef8aec3c4f2c0bb8b6b52cda751e51427a96c8e60a3a87e0
"""
  send_address='1MPwN67aihW6REd8Qh8kUtWCG3cVu6M4w5'
  receive_address = '15LYSZvdF46MeV3MsxjU7XbTkGvQiATQX5'
	transactionHash(send_address=send_address, receive_address = receive_address)
