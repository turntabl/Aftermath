#!/usr/bin/env python
import requests
import json
import time
import argparse

from collections import defaultdict
from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box
from rich.measure import Measurement
from rich.text import Text

parser = argparse.ArgumentParser()
parser.add_argument('-url', required=True)
args = parser.parse_args()
url = requests.get(f'{args.url}')
urlLink = url.json()

description = urlLink['info']['description']

taglists = {}
for t in range(1, len(urlLink['tags']) + 1):
    for tag in urlLink['tags']:
        taglists[tag['name']] = []

finalList = []
def getPaths():
    for key, value in urlLink['paths'].items():
        getChildPath(key,value)

    return 

def getChildPath(parentkey, data):
    ran = False
    for key, value in data.items():
        jsonData = {}
        jsonData['path'] = parentkey
        jsonData['request_methods'] = key
        jsonData['description'] = value['summary']
        jsonData['tag'] = value['tags'][0]
        if "parameters" in value and not ran:
            dataType = [] if not value['parameters'] else value['parameters'][0]
            if "type" in dataType:
                jsonData['data_type'] = dataType['type']
            else:
                jsonData['data_type'] = '---'
            ran 
        else:
           jsonData['data_type'] = '---'
        final(jsonData)
    
    return 

def final(jsonData):
    finalList.append(jsonData)
    
getPaths()

console = Console()

console.show_cursor(False)

try:
    for newRow in finalList:
        for k,v in taglists.items():
            if newRow['tag'] == k:
                v.append(newRow)
    
    console.print(urlLink['info']['description'], style="green")
    for tags, newfinalist in taglists.items():
        table = Table(
            show_header=True,
            header_style="bold magenta",
            box=box.HEAVY,
            border_style="bright_green")

        table.add_column("Request Method")
        table.add_column("Path")
        table.add_column("Description")
        table.add_column("Data Type")

        table.title = tags

        for row in newfinalist:
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
            row['data_type']
            )
        console.print(table, justify="center")

finally:
    console.show_cursor(True)
