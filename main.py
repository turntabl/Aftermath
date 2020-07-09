import requests
from collections import defaultdict
import json

from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box
from contextlib import contextmanager
import time


url = requests.get('https://petstore.swagger.io/v2/swagger.json')
urlLink = url.json()

description = urlLink['info']['description']

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

finalList = []
def getPaths():
    url = requests.get('http://petstore.swagger.io/v2/swagger.json')
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
        data_type = rowObject = [] if not value['parameters'] else value['parameters'][0]
        if "type" in rowObject:
            shape['data_type'] = rowObject['type']
        else:
            shape['data_type'] = '---'
        final(shape)
    
    return 

def final(shape):
    # for t in finalList:
       # print(t)
    finalList.append(shape)
    

getPaths()
# print(json.dumps(finalList, indent=4, sort_keys=True))


console = Console()

table = Table(show_header=True, header_style="bold magenta", title=description, title_style="green", box=box.HEAVY, border_style="bright_green")
table.add_column("Request Method")
table.add_column("Path", justify="right")
table.add_column("Description", justify="right")
table.add_column("Tag", justify="right")
table.add_column("Type", justify="right")


for row in finalList:
   
    table.add_row(
    "[red]" + row['request_methods'] +"[/red]",
    "[cyan]" + row['path'] + "[/cyan]",
    "[blue]" + row['description'] + "[/blue]",
    "[green]" + row['tag'] + "[/green]",
    "[yellow]" + row['data_type'] + "[/yellow]",

    )

console.print(":smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: ",table,":thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley:")





