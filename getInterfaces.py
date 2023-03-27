import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth
from pprint import pprint

USER = input("Enter your username for DNAC: ")
PASS = getpass("Enter your password for DNAC: ")

BASEURL    = 'https://sandboxdnac.cisco.com'
authAPI    = '/dna/system/api/v1/auth/token'
getIntAPI = '/dna/intent/api/v1/interface'

authURL = BASEURL + authAPI

authPayload = {}
authHeaders = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

authResponse = requests.request("POST", authURL, auth=HTTPBasicAuth(USER, PASS), headers=authHeaders, data=authPayload, verify=False)

tokenJSON = authResponse.json()

TOKEN = tokenJSON['Token']

getURL = BASEURL + getIntAPI

getPayload = {}
getHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Auth-Token': TOKEN
}

getResponse = requests.get(getURL, headers=getHeaders, data=getPayload, verify=False)

getJSON = getResponse.json()

pprint(getJSON)
