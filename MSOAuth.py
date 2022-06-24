"""
Created on Fri Jun 24 22:59:01 2022

@author: PunsisiK
"""

import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth
import requests

#got the sandboxkey from mastercard project - couldn't get a private ke insted added the path to the keyfile
consumer_key = 'COGvaX3czfzNRvQq0rS9Fkqb4FQwzdDRPjWdghR3635ae04f!81d1d19015384292ab4c6502d2c359ef0000000000000000'
signing_key = authenticationutils.load_signing_key('TestOAuthProject-sandbox.p12', 'keystorepassword')
uri = 'https://sandbox.api.mastercard.com/billpayAPI/v1/isRoutingValid'
payload = '{"BillPayAccountValidation": {"RppsId": "99887761","BillerId": "9998887771","AccountNumber": "1234567890","TransactionAmount": "250.00","CustomerIdentifier1": "","CustomerIdentifier2": "","CustomerIdentifier3": "","CustomerIdentifier4": "","ResponseString": "Successful"}}'

def getOAuthHeader(consumer_key,signing_key, uri, payload):
    authHeader = OAuth.get_authorization_header(uri, 'POST', payload,consumer_key , signing_key)
    print('OAuth Header::::::'+authHeader)
    return authHeader

authHeader1 = getOAuthHeader(consumer_key,signing_key, uri, payload)

headerdict = {'Authorization' : authHeader1,'Content-type' : 'application/json', 'Accept' : 'application/json'}
response =requests.post(uri, headers=headerdict, data=payload)
print('Response:::::',response.content)
