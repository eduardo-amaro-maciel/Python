# ----PROGRAMA PRINCIPAL---- #

import LayoutTrabalho
import os
from pyfiglet import figlet_format

os.system("cls")
result = figlet_format("decifrador", font = "isometric1" )
print(result\n)

if __name__ == 'main':
  LayoutTrabalho.lay()

# -> no arquivo uteis é possivel trocar o "dicionariopt.txt" pelo "dicionarioptcompleto", apesar que
# pode haver queda de performance
