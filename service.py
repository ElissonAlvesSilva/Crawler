from Util import Util
import requests
from bs4 import BeautifulSoup


class Service:
    # construtor
    def __init__(self):
        self._file = None

    # inicializa o arquivo
    def initFile(self, file):
        self._file = file


    def searchUrlNotFoundProduct(self, listUrl):
        # instacia a classe util
        util = Util()
        #cria um lista vazia
        listResult = []

        for i in range(len(listUrl)):
            # requisita a url
            request = requests.get(listUrl[i])
            # le o DOM
            soup = BeautifulSoup(request.text, 'lxml')
            # obtem a lista de not found produto
            listaNotFound = util.listErrs()
            # lista de urls
            for x in range(len(listaNotFound)):
                # verifica se existe algum id igual a lista de  not found produto
                verifyId = soup.find('div', id=listaNotFound[x])
                # verifica se existe alguma classe igual a lista de  not found produto
                verifyClass = soup.find('div', class_=listaNotFound[x])

                # verifica se existe algum id igual a lista de  not found produto
                if (verifyId != None):
                    # caso exista um id igual a lista passada de not found, a url sera adicionada em uma lista
                    listResult.append(listUrl[i])
                    break
                    # caso exista uma class igual a lista passada de not found, a url sera adicionada em uma lista
                if (verifyClass != None):
                    listResult.append(listUrl[i])
                    break
        return listResult

    def readDataOfFile(self):
        # abre o arquivo para leitura
        files = open(self._file, 'r')
        lista = []
        for data in files:
            data = self._removeBreakWord(data)
            # data um split nos dados tirando quer seja , ; ''

            if self._typeBreak(data) == 1:
                elements = data.split(';')
            elif self._typeBreak(data) == 2:
                elements = data.split(',')
            elif self._typeBreak(data) == 3:
                elements = data.split("'\n'")

            lista.append(elements[0])

        files.close()
        return lista

    #remove quebra de linha
    @staticmethod
    def _removeBreakWord(word):
        x = word.rstrip()
        return x

    #verifica o tipo de separacao entre as urls
    @staticmethod
    def _typeBreak(word):
        if word.find(';'):
            return 1
        elif word.find(','):
            return 2
        elif word.find("'\n'"):
            return 3
