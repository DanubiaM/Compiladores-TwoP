
class Analisador_Sintatico:

    #construtor
    def __init__(self, lista_tokens):
        #pilha sintatica iniciada com termo inicial da gramatica e $.
        self.pilha_sintatica = ['$', 'PROGRAMA']

        #iniciando lista com a lista de tokens seguida de $.        
        self.list_tokens = list(lista_tokens)
        self.list_tokens.append('$')

     #metodo auxiliar   
    def leitura_tokens(self):
        print("Lista tokens")
        for i in self.list_tokens:
            print(i)
        print("Pilha Sintatica")
        for i in self.pilha_sintatica:
            print(i)


    def verificacao_sintatica(self):

        while ( self.list_tokens[0][0] != '$' and self.pilha_sintatica[-1] != '$' ):

            #print("primeiro item lista ",self.list_tokens[0][0])
            #print("Topo pilha ", self.pilha_sintatica[-1])
            #self.leitura_tokens()
            #print("- "*20)

            #se topo da pilha e primeiro item da lista forem iguais
            if self.list_tokens[0][0] == self.pilha_sintatica[-1]:

                #Caso seja iguais, porem $ não devera realizar remoção de $
                if self.list_tokens[0][0] == '$' and self.pilha_sintatica[-1] == '$':
                    return

                del self.list_tokens[0]  #remove o primeiro item
                self.pilha_sintatica.pop()
                                
            else:
                
                #se topo de pilha for diferente do inicio da lista
                self.tabela_sintatica()  
                 

             
            #condição invalida, não pode haver lista vazia  e pilha com dados
            if len(self.list_tokens) == 0 and len(self.pilha_sintatica)>0:
                print("Erro Sintático: Pilha com itens.") #especificar linha, coluna.
                return
            elif len(self.list_tokens) > 0 and (self.pilha_sintatica) == 0:
                print("Erro Sintático: Lista de tokens com itens.") #especificar linha, coluna.
                return
        print("Finalizou")
    
    #Método para verificar regras de produção
    def tabela_sintatica(self):

        if self.pilha_sintatica[-1] == 'PROGRAMA':
            #PRODUCAO  0
            self.pilha_sintatica.pop()
            #adiciona as produções
            self.pilha_sintatica.append('tk_end_program')
            self.pilha_sintatica.append(':')
            self.pilha_sintatica.append('LISTA_COMANDOS')
            self.pilha_sintatica.append(':')
            self.pilha_sintatica.append('tk_start_program')

        elif self.pilha_sintatica[-1] == 'LISTA_COMANDOS':
            
            
            #PRODUCAO 1
            if self.list_tokens[0][0] == 'tk_read' or self.list_tokens[0][0] == 'tk_screen' or self.list_tokens[0][0] == 'tk_if' or self.list_tokens[0][0] == 'tk_int' or self.list_tokens[0][0] == 'tk_while' or self.list_tokens[0][0] == 'id':

                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('LISTA_COMANDOS')
                self.pilha_sintatica.append(';')
                self.pilha_sintatica.append('COMANDO')

            #PRODUCAO 2
            elif self.list_tokens[0][0] == 'tk_else' or self.list_tokens[0][0] == ":":
                self.pilha_sintatica.pop()
            
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
            
        elif self.pilha_sintatica[-1] == 'COMANDO':
            #PRODUCAO 3
            if self.list_tokens[0][0] == 'tk_read':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append(')')
                self.pilha_sintatica.append('id')
                self.pilha_sintatica.append('(')
                self.pilha_sintatica.append('tk_read')
            
            #PRODUCAO 4
            elif self.list_tokens[0][0] == 'tk_screen':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append(')')
                self.pilha_sintatica.append('PUTS')
                self.pilha_sintatica.append('(')
                self.pilha_sintatica.append('tk_screen')

            #PRODUCAO 5
            elif self.list_tokens[0][0] == 'tk_int':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('DECLARACAO_VAR')

            #PRODUCAO 6
            elif self.list_tokens[0][0] == 'id':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('tk_atribuicao')
                self.pilha_sintatica.append('id')

            #PRODUCAO 7
            elif self.list_tokens[0][0] == 'tk_if':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('tk_end_if')
                self.pilha_sintatica.append(':')
                self.pilha_sintatica.append('CONDICIONAL')
            
            #PRODUCAO 8
            elif self.list_tokens[0][0] == 'tk_while':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('tk_end_while')
                self.pilha_sintatica.append(':')
                self.pilha_sintatica.append('REPETICAO')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))


        elif self.pilha_sintatica[-1] == 'DECLARACAO_VAR':
            #PRODUCAO 9
            if self.list_tokens[0][0] == 'tk_int':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('id')
                self.pilha_sintatica.append('tk_int')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))


        elif self.pilha_sintatica[-1] == 'CONDICIONAL':
            #PRODUCAO 10
            if self.list_tokens[0][0] == 'tk_if':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('ELSE_CONDICAO')
                self.pilha_sintatica.append('LISTA_COMANDOS')                
                self.pilha_sintatica.append(':')
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('tk_if')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
    
        elif self.pilha_sintatica [-1] == 'ELSE_CONDICAO':
            #PRODUCAO 11
            if self.list_tokens[0][0] == 'tk_else':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('LISTA_COMANDOS')
                self.pilha_sintatica.append(':')                
                self.pilha_sintatica.append('tk_else')
                

            #PRODUCAO 12   
            elif self.list_tokens[0][0] == ':':
                 self.pilha_sintatica.pop()
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
    
        elif self.pilha_sintatica[-1] == 'REPETICAO':
            #PRODUCAO 13
            if self.list_tokens[0][0] == 'tk_while':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('LISTA_COMANDOS')
                self.pilha_sintatica.append(':')                
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('tk_while')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
    
        elif self.pilha_sintatica[-1] == 'EXPRESSAO':
            #PRODUCAO 14
            if self.list_tokens[0][0] == 'num' or self.list_tokens[0][0] == 'id':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('TAIL')
                self.pilha_sintatica.append('OPERANDO')

            #PRODUCAO 15
            elif self.list_tokens[0][0] == '(':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('TAIL')
                self.pilha_sintatica.append(')')  
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('(')                  
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
    
        elif self.pilha_sintatica[-1] == 'OPERANDO':
            #PRODUCAO 21
            if self.list_tokens[0][0] == 'id':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('id')

            #PRODUCAO 22
            elif self.list_tokens[0][0] == 'num':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('num')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
    
        elif self.pilha_sintatica[-1] == 'TAIL':
            #PRODUCAO 16
            if self.list_tokens[0][0] == 'op_mat' or self.list_tokens[0][0] == 'c_logico' or self.list_tokens[0][0] == 'op_logico':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('OPERACAO')

            #PRODUCAO 17
            elif self.list_tokens[0][0] == ';' or self.list_tokens[0][0] == ')' or self.list_tokens[0][0] == ':':
                self.pilha_sintatica.pop()
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
      
        elif  self.pilha_sintatica[-1] == 'OPERACAO':
            #PRODUCAO 18
            if self.list_tokens[0][0] == 'c_logico':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('c_logico')
            
            #PRODUCAO 19
            elif self.list_tokens[0][0] == 'op_logico':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('op_logico')

            #PRODUCAO 20
            elif self.list_tokens[0][0] == 'op_mat':
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('EXPRESSAO')
                self.pilha_sintatica.append('op_mat')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
        
        elif self.pilha_sintatica[-1] == 'PUTS':
        
           
            #PRODUCAO 23
            if self.list_tokens[0][0] == 'string':          
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('string')
            
            #PRODUCAO 24
            elif self.list_tokens[0][0] == 'id':                
                self.pilha_sintatica.pop()
                self.pilha_sintatica.append('id')
            else:
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][2], self.list_tokens[0][3]))
        else:
            print("Erro Sintático: não foi possivel reconhecer o valor  " + self.pilha_sintatica[-1])
            return 

