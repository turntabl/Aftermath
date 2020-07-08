import requests
from collections import defaultdict
import json

from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box


url = requests.get('https://employeeservice002.herokuapp.com/v2/api-docs')
urlLink = url.json()

description = urlLink['info']['description']

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

finalList = []
def getPaths():
    url = requests.get('https://employeeservice002.herokuapp.com/v2/api-docs')
    urlLink = url.json()
    for key, value in urlLink['paths'].items():
        getChildPath(key,value)

    return None

def getChildPath(parentkey, data):

    for key, value in data.items():
        shape = {}
        shape['path']= parentkey
        shape['request_methods']= key
        shape['description']= value['summary']
        shape['tag'] = value['tags'][0] 
        final(shape)
    
    return 

def final(shape):
    # for t in finalList:
    #     print(t)
    finalList.append(shape)
    

getPaths()
# print(json.dumps(finalList, indent=4, sort_keys=True))


console = Console()

table = Table(show_header=True, header_style="bold magenta", title=description, title_style="green", box=box.HEAVY)
table.add_column("Request Method")
table.add_column("Path", justify="right")
table.add_column("Description", justify="right")
table.add_column("Tag", justify="right")

print(finalList)
for row in finalList:
   
    table.add_row(
    row['request_methods'],
    row['path'],
    row['description'],
    row['tag']
    )

console.print(table)
    




