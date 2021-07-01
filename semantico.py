import sys

class Analisador_Semantico:
    def __init__ (self, lista_tokens):
        self.list_tokens = list(lista_tokens)
        self.symbol_table = {} #inicia a tabela de simbolos

    def inicia_analise(self):
        list_t = []
        i = 0
        for list_t in self.list_tokens:
            #Se o token for id
            if list_t[0] == "id":
               #verifico a declaracao previa das variaveis
                
                if(self.list_tokens[i-1][0] == 'tk_int'):                   
                   self.verifica_declaracao(list_t)
                else:
                    self.busca(list_t)
            i+=1 
        print("Semantic analysis performs successfully.")
    def busca(self, list_t):
        #verifuca se a tabeka de simbolos possui o lexema
        if self.symbol_table.get(list_t[1]):
                                                        #Caso possuir, atualizar o "utilizado"
           list_atual =  self.symbol_table[list_t[1]]   #lista recebe os valores daquela chave  
                                                       
           list_atual[1] =  list_atual[1] +1            #Atualiza o segundo campo correspondente ao "utilizado"
    
           self.symbol_table[list_t[1]]= list_atual     #Atualiza os valores da tabela de simbolo daquela chave
        else:
            print("Erro Semântico: variavel ´{0}´ nao declarada".format(list_t[1]))
            sys.exit()


    def verifica_declaracao(self, token):
        #Verifica se o lexema esta condito na tabela de simbolos.
        if self.symbol_table.get(token[1]):
            print("Erro Semântico: a variavel ´{0}´ já declarada.".format(token[1]))
            sys.exit()
        else:
            self.insere(token)

    def insere(self, token):
        #tam = len(self.symbol_table)
        #dic{lexema: token, utilizado, declarado[1/0]}
        self.symbol_table[token[1]] = [token[1],0, 1]