import sys

class Analisador_Semantico:
    def __init__ (self, lista_tokens):
        self.list_tokens = list(lista_tokens)
        self.symbol_table = {} #inicia a tabela de simbolos
        self.arquivo = open("log_ops.txt",'w')

    def inicia_analise(self):
        list_t = []
        i = 0
        
        for list_t in self.list_tokens:
            atribuicao = ""           
                                 
            if(list_t[0] == 'tk_int'):                    
                self.verifica_declaracao(self.list_tokens[i+1])
                
            elif list_t[0] == 'tk_atribuicao':   
                self.busca(self.list_tokens[i-1][1])
                #caso seja num ou id  
                if self.list_tokens[i+2][0] == ";":
                    self.atualiza(self.list_tokens[i-1], self.list_tokens[i+1][1],1)

                #para atribuições que nao seja num ou id 
                else:
                    c = i +1
                    while self.list_tokens[c][1] != ';':
                        atribuicao += ""+ self.list_tokens[c][1] 
                        c+=1    
                    
                    
                    self.atualiza(self.list_tokens[i-1], atribuicao,2)                                     
                                    
            if list_t[1] == "/":  
                self.divisao_zero(self.list_tokens[i+1])                               
            i+=1 
        print("Semantic analysis performs successfully.")
        self.arquivo.close()
        
        
    #Método responsavel por verificar se a variavel existe.
    def busca(self, valor):      
        if self.symbol_table.get(valor):
            return 1                                  
        else:
            print("Erro Semântico: variavel ´{0}´ nao declarada".format(valor))
            sys.exit()

    #Método responsavel por verificar se já existe declarado  a variavel
    def verifica_declaracao(self, token):
       
        if self.symbol_table.get(token[1]):
            print("Erro Semântico: variavel ´{0}´ já declarada [l{1}:c{2}]".format(token[1], token[2], token[3] ))
            sys.exit()
        else:
            self.inserir(token)

    #Método responsavel por inserir dados na tabela
    def inserir(self, token):        
        #dic{lexema: token, declarado[1/0], atribuicao}
        self.symbol_table[token[1]] = [token[0], 1, 0]
        self.reg_operacao(1, token[1], token[2])
    
    #Método responsavel por atualizar valores de atribuição das variaveis
    def atualiza (self, val, atribuicao, n ):        
        
        if n == 1:                       
            lista_temp =  self.symbol_table[val[1]]               
            lista_temp[2] = self.busca_atribuicao(atribuicao)             
            self.symbol_table[val[1]]= lista_temp
             
        else:
            lista_temp =  self.symbol_table[val[1]]  
            lista_temp[2] = atribuicao
            self.symbol_table[val[1]]= lista_temp
                                
        self.reg_operacao(2,val[1], atribuicao)

    #Método responsavel por buscar as atribuições das variaveis
    def busca_atribuicao(self, valor):
        #Enquanto o valor nao receber um digito, ou seja ser um id  
        while (valor.isdigit() == False):
                #verifico se o id existe na tabela         
                self.busca(valor)
                #crio uma lista temporaria para receber os valores da chave
                lista_temp = self.symbol_table[valor]
                valor = str(lista_temp[2])               
                
                #Se a atribuicao for um numero
                if valor.isdigit():                    
                    #retorno ele
                    return valor
        
        return valor

    #Método responsavel por verificar se é uma divisão por zero
    def divisao_zero(self, valor):         
        if self.busca_atribuicao(valor[1]) == '0':
            print("Erro Semântico: divisão por zero não permitida [l{0}:c{1}]".format(valor[2], valor[3]))            
            sys.exit()
    #Método que escreve o log em um arquivo de texto   
    def reg_operacao(self, val, variavel, valor = None):        
        if (val ==1):
           self.arquivo.write("Variavel ´{0}´ declarada\n".format(variavel))

        elif (val == 2):
            self.arquivo.write("Variavel ´{0}´ atualizada o valor para ´{1}´\n".format(variavel, valor))
    
    #Método que imprimri o resultado
    def log_operacoes(self):
        arquivo = open("log_ops.txt","r")
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()    
            