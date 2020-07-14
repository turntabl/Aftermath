import requests
import json
import time

from collections import defaultdict
from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box
from rich.measure import Measurement
from rich.text import Text


url = requests.get('https://petstore.swagger.io/v2/swagger.json')
urlLink = url.json()

description = urlLink['info']['description']

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

finalList = []
def getPaths():
    url = requests.get('https://petstore.swagger.io/v2/swagger.json')
    urlLink = url.json()
    for key, value in urlLink['paths'].items():
        getChildPath(key,value)

    return 

def getChildPath(parentkey, data):
    ran = False
    for key, value in data.items():
        shape = {}
        shape['path']= parentkey
        shape['request_methods']= key
        shape['description']= value['summary']
        shape['tag'] = value['tags'][0]
        if "parameters" in value and not ran:
            rowObject = [] if not value['parameters'] else value['parameters'][0]
            if "type" in rowObject:
                shape['data_type'] = rowObject['type']
            else:
                shape['data_type'] = '---'
            ran 
        else:
            shape['data_type'] = '---'
        final(shape)
    
    return 

def final(shape):
    finalList.append(shape)
    

getPaths()
# print(json.dumps(finalList, indent=4, sort_keys=True))


console = Console()





table = Table(show_header=True, header_style="bold magenta", title_style="green", box=box.HEAVY, border_style="bright_green")

console.clear()
console.show_cursor(False)

try:
    table.add_column("Request Method")
    console.print(table, justify="center")

    table.add_column("Path")
    console.print(table, justify="center")

    table.add_column("Description")
    console.print(table, justify="center")

    table.add_column("Controller")
    console.print(table, justify="center")

    table.add_column("Data Type")
    console.print(table, justify="center")

    table.title = description
    console.print(table, justify="center")

    table.caption = "Aftermath: turntabl swagger cli"
    console.print(table, justify="center")

    table.caption = "Aftermath: [b]turntabl swagger cli[/b]"
    console.print(table, justify="center")

    table.caption = "Aftermath: [b magenta not dim]turntabl swagger cli[/]"
    console.print(table, justify="center")
    
    # table_width = Measurement.get(console, table, console.width).maximum

    # print(finalList)
    for row in finalList:
        if row['request_methods'] == "post":
            method_color = "[green]" + row['request_methods'] + "[/green]" + (":postbox:")
        
        if row['request_methods'] == "get":
            method_color = "[blue]" + row['request_methods'] + "[/blue]" + (":dart:")
        
        if row['request_methods'] == "put":
            method_color = "[yellow]" + row['request_methods'] + "[/yellow]" + (":memo:")

        if row['request_methods'] == "delete":
            method_color = "[red]" + row['request_methods'] + "[/red]" + (":x:")
             
        table.add_row(
        method_color,
         row['path'],
         row['description'],
         row['tag'],
         row['data_type']
        )
        console.print(table, justify="center")

    # console.print(":smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: ",table,":thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley:")

finally:
    console.show_cursor(True)
