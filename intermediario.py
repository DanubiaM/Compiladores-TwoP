from infix_postfix import infix_to_postfix
class Intermediario:
    def __init__(self, list_tokens, list_id):
        self.lista_tokens = list_tokens
        self.lista_id = list(list_id.keys())
        self.cod_intermediario = []


    def inicia_geracao(self):
        #Declarações de variaveis
        for id in self.lista_id:
           self.cod_intermediario.append('_Var {0}'.format(id))
        #Gramática
        i=0
        for token in self.lista_tokens:

            if token[0] == 'tk_read' :
               self.cod_intermediario.append("leia {0}".format(self.lista_tokens[i+2][1])) 
            
            elif token[0] == 'tk_screen':
                self.cod_intermediario.append("escreva {0}".format(self.lista_tokens[i+2][0]))

            elif token[0] == 'tk_atribuicao':
                j=i
                while self.lista_tokens[j][0] != ';':
                    atribuicao = self.lista_tokens[j][1]
                    j+=1
                """
                    Verificar atribuicao que nao esta funcionando
                    Verificar infixpostfix se esta ok, realizar testes
                """
                print("Atribuicao "+atribuicao)    
                print("postfix "+infix_to_postfix('(n1+n2+n3+n4)/4'))    
                self.cod_intermediario.append("{0} = {1}".format(self.lista_tokens[i-1][1], infix_to_postfix(atribuicao)))     
            elif token[0] == 'tk_while':
                j=i
                while self.lista_tokens[j][0] != ':':
                    condicao = self.lista_tokens[j][1]
                    j+=1
                self.cod_intermediario.append("enquanto {0}".format(condicao))
            
            elif token[0] == 'tk_end_while':
                self.cod_intermediario.append("fim_enquanto")

            elif token[0] == 'tk_if':
                j=i
                while self.lista_tokens[j][0] != ':':
                    condicao = self.lista_tokens[j][1]
                    j+=1
                self.cod_intermediario.append("se {0} entao".format(condicao))
           
            elif token[0] == 'tk_end_if':
                self.cod_intermediario.append("fim_se")     

            elif token[0] == 'tk_else':
                self.cod_intermediario.append("senao")

            i+=1
        return self.cod_intermediario     
