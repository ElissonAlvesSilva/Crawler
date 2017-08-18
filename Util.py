class Util:
    # construtor e lista de possiveis id ou classes de not found product
    def __init__(self):
        self._listErrs = [
            'nm-not-found-page',
            'notfound',
            'not-found',
            'not_found',
            'not-found-grid',
            'topbar_no_results',
            'no_results',
            'neemu-not-found',
            'search-error-box',
            'err',
            'not_found_product',
            'busca_vazio'
            'not-found-search'
            'no_search']

    # getter da lista de erros
    def listErrs(self):
        return self._listErrs

    # verifica se existe o arquivo
    def existFile(self, file):
        try:
            with open(file, 'r'):
                return True
        except IOError:
            print("No such file in the directory or the file doesn't have permission to read.")
            return False

    # cria um arquivo
    def makeFile(self, file):
        self._file = open(file, 'w+')
        return self._file

    # escreve em um arquivo
    def write(self, listaUrl, fileOut):
        file = self.makeFile(fileOut)
        for i in range(len(listaUrl)):
            file.write(listaUrl[i]+'\n')

        file.close()

