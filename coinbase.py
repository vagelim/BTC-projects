#!/usr/bin/python

from subprocess import check_output
from gv import sendTxt

API_key = 'ENTER YOUR API KEY HERE'

URL = 'https://coinbase.com/api/v1/prices/buy?api_key='

chart = check_output (["curl", URL + API_key])

priceURL = 'http://test.com/price'
btc = float(check_output(["curl", priceURL]))

left = chart.find('amount')+9


price = float(chart[left:left+6])

if price < btc:
	sendTxt('123456789',price)
