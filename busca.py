from Util import Util
from service import Service
import sys

# instancia as classes
util = Util()
service = Service()

# recupera os parametros passados pelo terminal
file = sys.argv[1]
fileOut = sys.argv[2]


# verifica se existe o arquivo
if util.existFile(file):
    # inicia o arquivo
    service.initFile(file)
    # le as urls passadas
    listUrl = service.readDataOfFile()
    # verifica as urls que nao trazem produtos e retorna uma lista
    lista = service.searchUrlNotFoundProduct(listUrl)
    # escreve a lista de urls que nao encontraram nenhum produto em um arquivo
    util.write(lista, fileOut)
else:
    print('Please send a new file')




