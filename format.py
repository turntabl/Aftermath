from rich.console import Console
from rich.table import Column, Table
from main import  a_dict

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Request Method")
table.add_column("Path")
table.add_column("Description", justify="right")
table.add_row(
    
)
table.add_row(
    
)
table.add_row(
   
)

console.print(table)