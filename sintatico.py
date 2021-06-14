
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

        for i in self.list_tokens:
            print(i)

        for i in self.pilha_sintatica:
            print(i)


    #Notas: como tenho uma lista dentro de uma lista, e a lista tem 3 posições e quero acesso ao primeiro item dela
    # uso [0] para acessar entao seu primeiro item.

    def verificacao_sintatica(self):

        while ( self.list_tokens[0][0] != '$' and self.pilha_sintatica[-1] != '$'):

            ##print("primeiro item lista ",self.list_tokens[0][0])
            ##print("Topo pilha ", self.pilha_sintatica[-1])

            #se topo da pilha e primeiro item da lista forem iguais
            if self.list_tokens[0][0] == self.pilha_sintatica[-1]:
                del self.list_tokens[0]  #remove o primeiro item
                self.pilha_sintatica.pop()

               
            else:
                
                #se topo de pilha for diferente do inicio da lista
                self.tabela_sintatica()  
                 

            """    
            #condição invalida, não pode haver lista vazia  e pilha com dados
            if self.list_tokens == None and len(self.pilha_sintatica)>0:
                print("Erro Sintático: Pilha com itens.") #especificar linha, coluna.
                
            elif len(self.list_tokens) > 0 and self.pilha_sintatica == None:
                print("Erro Sintático: Lista de tokens com itens.") #especificar linha, coluna.
            """

    #Método para verificar regras de produção
    def tabela_sintatica(self):


        if self.pilha_sintatica[-1] == 'PROGRAMA':
            #Produção valida 0
            self.pilha_sintatica.pop()
            #adiciona as produções
            self.pilha_sintatica.append('tk_end_program')
            self.pilha_sintatica.append('LISTA_COMANDOS')
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
                print("Erro Sintático: não foi possivel reconhecer producao válida  para a linha {0} e coluna {1}".format(self.list_tokens[0][1], self.list_tokens[0][2]))