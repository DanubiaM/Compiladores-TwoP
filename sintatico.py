import sys

class Analisador_Sintatico:

    #construtor
    def __init__(self, lista_tokens):
        #pilha sintatica iniciada com termo inicial da gramatica e $.
        self.pilha_sintatica = ['$', 'PROGRAMA']
        #iniciando lista com a lista de tokens seguida de $.        
        self.list_tokens = list(lista_tokens)
        self.list_tokens.append('$')

        #contadores de log
        self.empilhamento = 0
        self.desempilhamento = 0
        self.reducao_pilha_lista = 0
        self.producoes_aplicadas = []
        self.n_producoes_aplicadas= 0

        self.arquivo = open("log_op.txt",'w')
        
        self.producoes = {
            0 :  ["tk_start_program",":", "LISTA_COMANDOS", ":", "tk_end_program"],
            1 :  ["COMANDO",";", "LISTA_COMANDOS"],
            2 :  [],
            3 :  ["tk_read", "(", "id", ")"],
            4 :  ["tk_screen", "(", "PUTS", ")"],
            5 :  ["DECLARACAO_VAR"],
            6:   ["id", "tk_atribuicao", "EXPRESSAO_ARITMETICA"],
            7 :  ["CONDICIONAL", ":", "tk_end_if"],
            8 :  ["REPETICAO", ":", "tk_end_while"],
            9 :  ["tk_int", "id"],
            10 : ["tk_if","EXPRESSAO_BOOLEANA", ":", "LISTA_COMANDOS", "ELSE_CONDICAO"],
            11 : ["tk_else", ":", "LISTA_COMANDOS"],
            12 : [],
            13 : ["tk_while", "EXPRESSAO_BOOLEANA",":", "LISTA_COMANDOS"],
            14 : ["OPERANDO", "TAIL"],
            15 : ["(", "EXPRESSAO_ARITMETICA", ")", "TAIL"],
            16 : ["OPERACAO"],
            17 : [],
            18 : ["op_mat", "EXPRESSAO_ARITMETICA"],
            19 : ["EXPRESSAO_ARITMETICA","CONECTOR_LOGICO"],            
            20 : ["CONECTOR"],
            21 : [],
            22 : ["op_logico", "EXPRESSAO_BOOLEANA"],             
            23 : ["c_logico", "EXPRESSAO_BOOLEANA"],
            24 : ["id"],
            25 : ["num"],
            26 : ["string"],
            27:  ["id"]
        }

        self.nao_terminais = {
        'PROGRAMA': [0],
        'LISTA_COMANDOS': [1, 2],
        'COMANDO': [3, 4, 5, 6 , 7, 8],
        'DECLARACAO_VAR' : [9],
        'CONDICIONAL': [10],
        'ELSE_CONDICAO': [11, 12],
        'REPETICAO': [13],
        'EXPRESSAO_ARITMETICA': [14, 15],
        'OPERANDO': [24,25],
        'TAIL': [16,17],
        'OPERACAO': [18],
        'PUTS': [26, 27],
        'EXPRESSAO_BOOLEANA': [19],
        'CONECTOR': [22, 23],
        'CONECTOR_LOGICO': [20, 21]  
        }

        self.terminais = {
            'num': [14,25,19],
            'op_mat': [16,18],
            'c_logico': [17,20,23],
            'op_logico': [17,20, 22],
            'tk_read': [1,3],
            'tk_screen' :[1,4],
            'tk_if': [1, 7, 10],
            'tk_int': [1, 5, 9],
            'tk_else':[2, 11],
            'tk_while':[1, 8, 13],
            'tk_start_program': [0],
            'tk_end_program': [],
            'tk_end_if': [],
            'tk_end_while': [],
            'tk_atribuicao': [],
            'string': [26],
            'id': [1, 6, 14, 19, 24, 27],
            ';': [17],
            ')': [17],
            '(': [15,19],
            ':':[2, 12,17, 21]
        }


    def verificacao_sintatica(self):      
        
        while ( self.list_tokens[0][0] != '$' and self.pilha_sintatica[-1] != '$' ):
           
            if self.list_tokens[0][0] == self.pilha_sintatica[-1]:
                self.reg_operacoes(3,-1)
                del self.list_tokens[0]  
                self.pilha_sintatica.pop()  
                self.reducao_pilha_lista += 1
                self.desempilhamento += 1                
            elif len(self.list_tokens) == 0 and len(self.pilha_sintatica)>0:
                print("Erro Sintático: Pilha sintática possui dados e lista sintática  está vazia [error performing parsing] ", self.pilha_sintatica )
                sys.exit()   
            elif len(self.list_tokens) > 0 and (self.pilha_sintatica) == 0:   
                print("Erro Sintático: Lista sintática possui dados e pilha sintatica vazia [error performing parsing]", self.list_tokens)               
                sys.exit()
            else:
                self.tabela_sintatica()               
                        
        print("SUCESS: syntatic analysis completed.")
        self.arquivo.close()

    #Método para verificar regras de produção
    def tabela_sintatica(self):
        try:
            producao = self.verifica_producao() 
        except:
            print("Erro Sintático: não possível encontrar uma producao válida para o valor {0} na linha {1} e coluna {2}.[error performing parsing]".format(self.list_tokens[0][1], self.list_tokens[0][2], self.list_tokens[0][3]))
            sys.exit()
        else:
            self.aplica_producao(producao)

    #Metodo reponsavel por verificar se existe producao válida
    def verifica_producao (self):
        producao = []  

        x, y = self.valor_producao()            
        producao = list(set(x).intersection(y)) 
        return producao[0]
      
   
    #Método responsabel por retornar a chave dos dicionarios.
    def valor_producao(self):        
        key_stack  = [-1] 
        key_list = [-1]  

        #Procurando a chave correspondente da Pilha       
        for i in self.nao_terminais.keys():            
            if i == self.pilha_sintatica[-1]:                
                key_stack = self.nao_terminais[i]               
      
        #Procurando a chave correspondente da Lista.       
        for j in self.terminais.keys():            
            if j == self.list_tokens[0][0]:
                key_list = self.terminais[j]
                
        return (key_stack,key_list)       
                    
    #Método responsavel por aplicar a producao
    def aplica_producao(self, producao):
        try:
            valor_producao = self.producoes[producao]
            self.producoes_aplicadas.append(producao)            
           
            self.reg_operacoes(1, producao)
            self.pilha_sintatica.pop()  
            self.desempilhamento += 1

            #producoes vazias 2, 12 e 17
            if any([valor_producao != 2, valor_producao != 12, valor_producao != 17, valor_producao != 21]):                     
                
                for i in reversed(valor_producao):                    
                    self.pilha_sintatica.append(i)
                    self.empilhamento += 1
                    self.reg_operacoes(2, producao)
              
        except:
            print("Erro Sintático: valor foi possivel encontrar uma producao valida para o valor  {0} na linha {1} e coluna {2}. [error performing parsing]".format(self.list_tokens[0][1], self.list_tokens[0][2], self.list_tokens[0][3]))            
         
    def reg_operacoes(self,n, producao):
      
        #operacoes de desempilhamento
        if n == 1:
            self.arquivo.write("DESEMPILHANDO:...... Topo Pilha: {0} ->  producao a ser inserida {1}. \n".format(self.pilha_sintatica[-1], producao))
        #operacoes de empilhamento
        elif n == 2:
            self.arquivo.write("EMPILHANDO:......... Topo Pilha: {0} -> producao aplicada {1}. \n".format(self.pilha_sintatica[-1], producao))
        #reducao
        elif n ==3:  
            self.arquivo.write("REDUCAO APLICADA:.... Topo Pilha: {0} First List: {1}\n".format(self.pilha_sintatica[-1],self.list_tokens[0][0] ))
      
        
    def log_operacoes (self):
        print("-=-"*20)
        print("\t\t\tLOG DE OPERACOES")
        print("-=-"*20)
        print("Empilhamentos.........................:",self.empilhamento)
        print("Desempilhamento.......................:", self.desempilhamento)
        print("Producoes utilizadas..................:", self.producoes_aplicadas)
        print("Redução de Pilha e Lista..............:", self.reducao_pilha_lista)
        print("Quantidade de producoes utilizadas ...:", len(self.producoes_aplicadas))
        print("-"*20)
        arquivo = open("log_op.txt","r")
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()