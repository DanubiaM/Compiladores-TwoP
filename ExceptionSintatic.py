class ExceptionSintatic (Exception):
    def __init__(self, linha, coluna):
        self._linha = linha
        self._coluna = coluna

    def __str__(self):
        return "Erro Sintatico: Nao foi possivel reconhecer uma producao" + \
        " válida na linha {0} coluna {1}".format(self._linha, self._coluna)
            
            
    
