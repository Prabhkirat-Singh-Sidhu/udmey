'''package: folder
from-> means load folder 
import-> means load file
'''


from prettytable import PrettyTable

table = PrettyTable()
# table ->{object} = PrettyTable() ->{class}

table.add_column("Pokemon Name", ["Pikachu","Squirtel"])
table.add_column("Pokemon Type", ["Thunder","Water"])



print(table)

table.align = "l"

print(table)