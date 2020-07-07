import jmespath
import json
import requests

url = requests.get('https://employeeservice002.herokuapp.com/v2/api-docs')
urlLink = url.json()

description = urlLink['info']['description']
print(description)

a_dict = {}
for rest in list(urlLink['paths'].keys()):
    a_dict[rest] = list(urlLink['paths'][rest].keys())
    args = {}
    for summary in list(urlLink['paths'][rest].keys()):
        args[summary] = urlLink['paths'][rest][summary]['summary']
    a_dict[rest] = args
print(a_dict)
    
