import sys

class Analisador_Semantico:
    def __init__ (self, lista_tokens):
        self.list_tokens = list(lista_tokens)
        self.symbol_table = {} #inicia a tabela de simbolos

    def inicia_analise(self):
        list_t = []
        i = 0
        atribuicao = ""
        for list_t in self.list_tokens:
            #Se o token for id
            if list_t[0] == "id": 
                                              
                if(self.list_tokens[i-1][0] == 'tk_int'):                   
                   self.verifica_declaracao(list_t)
                
                elif self.busca(list_t[1]) == 1:    
                             
                    if (self.list_tokens[i+1][0] == "tk_atribuicao"):
                        if any([self.list_tokens[i+2][0] == "num",self.list_tokens[i+2][0] == "id"]):
                             
                            self.atualiza(list_t[1], self.list_tokens[i+2][1]) 
                           
                        else:                            
                            self.atualiza(list_t[1], None) 
                            
                    else:
                        
                        self.atualiza(list_t[1], None)                    
            if list_t[1] == "/":  
                self.divisao_zero(self.list_tokens[i+1])                               
            i+=1 
        print("Semantic analysis performs successfully.")
        print(self.symbol_table)

    def busca(self, valor):      
        if self.symbol_table.get(valor):
            return 1                                  
        else:
            print("Erro Semântico: variavel ´{0}´ nao declarada".format(valor))
            sys.exit()


    def verifica_declaracao(self, token):
        if self.symbol_table.get(token[1]):
            print("Erro Semântico: variavel ´{0}´ já declarada.".format(token[1]))
            sys.exit()
        else:
            self.inserir(token)

    def inserir(self, token):
        #dic{lexema: token, utilizado, declarado[1/0], atribuicao}
        self.symbol_table[token[1]] = [token[0],0, 1, 0]
        self.log_operacao(1, token[1], token[3])
    
    def atualiza (self, lexema, atribuicao = None):
        list_atual =  self.symbol_table[lexema]                                                        
        list_atual[1] =  list_atual[1] +1         
        self.symbol_table[lexema]= list_atual 
        
        if atribuicao != None:                       
            lista_temp =  self.symbol_table[lexema]               
            lista_temp[3] = self.busca_atribuicao(atribuicao)             
            self.symbol_table[lexema]= lista_temp
            self.log_operacao(2,lexema, atribuicao) 

        #self.log_operacao(2,lexema, "expressao aritmética")                     
        
    def busca_atribuicao(self, valor):
        #Enquanto o valor nao receber um digito, ou seja ser um id  
        while (valor.isdigit() == False):
                #verifico se o id existe na tabela  
                              
                self.busca(valor)
                #crio uma lista temporaria para receber os valores da chave
                lista_temp = self.symbol_table[valor]
                
                valor = str(lista_temp[3])                
                
                #Se a atribuicao for um numero
                if valor.isdigit():                    
                    #retorno ele
                    return valor
        
        return valor

    def divisao_zero(self, valor):         
        if self.busca_atribuicao(valor[1]) == '0':
            print("Erro Semântico: divisão por zero não permitida")            
            sys.exit()
       
    def log_operacao(self, val, variavel, valor = None):
        if (val ==1):
            print("Variavel ´{0}´ declarada".format(variavel))

        elif (val == 2):
            print("Variavel ´{0}´ atualizada o valor para ´{1}´".format(variavel, valor))  
