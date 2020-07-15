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

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

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
            rowObject = [] if not value['parameters'] else value['parameters'][0]
            if "type" in rowObject:
                jsonData['data_type'] = rowObject['type']
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

table = Table(
        show_header=True,
        header_style="bold magenta", 
        title_style="green", 
        box=box.HEAVY,
        border_style="bright_green")

console.show_cursor(False)

try:
    table.add_column("Request Method")
    table.add_column("Path")
    table.add_column("Description")
    table.add_column("Controller")
    table.add_column("Data Type")

    table.title = description

    table.caption = "Aftermath: turntabl swagger cli"
    table.caption = "Aftermath: [b]turntabl swagger cli[/b]"
    table.caption = "Aftermath: [b magenta not dim]turntabl swagger cli[/]"
    
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

finally:
    console.show_cursor(True)
