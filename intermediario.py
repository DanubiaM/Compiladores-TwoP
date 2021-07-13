from infix_postfix import infix_to_postfix
class Intermediario:
    def __init__(self, list_tokens, list_id):
        self.lista_tokens = list_tokens
        self.lista_id = list(list_id.keys())
        self.cod_intermediario = []
        self.log_intermediario = open("log_intermediario.txt","w")

    def inicia_geracao(self):
        #Declarações de variaveis
        for id in self.lista_id:
           self.cod_intermediario.append('_Var {0}'.format(id))
           self.log_intermediario.write("Declarado variavel {0}\n".format(id))
        #Gramática
        i=0
        for token in self.lista_tokens:

            if token[0] == 'tk_read' :
               self.cod_intermediario.append("leia {0}".format(self.lista_tokens[i+2][1]))
               self.log_intermediario.write("Comando de leitura da variavel {0} \n".format(self.lista_tokens[i+2][1])) 
            
            elif token[0] == 'tk_screen':
                self.cod_intermediario.append("escreva {0}".format(self.lista_tokens[i+2][1]))
                self.log_intermediario.write("Comando de escrita da variavel ou string {0}\n ".format(self.lista_tokens[i+2][1])) 


            elif token[0] == 'tk_atribuicao':
                j=i+1
                atribuicao =""
                while self.lista_tokens[j][0] != ';':
                    atribuicao += " "+self.lista_tokens[j][1]
                    j+=1
                  
                self.cod_intermediario.append("{0} = {1}".format(self.lista_tokens[i-1][1], infix_to_postfix(atribuicao)))     
                self.log_intermediario.write("Atribuido à {0} a expressão {1}\n ".format(self.lista_tokens[i-1][1], infix_to_postfix(atribuicao))) 

            elif token[0] == 'tk_while':
                j=i+1
                condicao = ""
                while self.lista_tokens[j][0] != ':':
                    condicao +=" "+ self.lista_tokens[j][1]
                    j+=1
                self.cod_intermediario.append("enquanto {0}".format(condicao))
                self.log_intermediario.write("Laço de repetição `while` reconhecido\n ") 
            
            elif token[0] == 'tk_end_while':
                self.cod_intermediario.append("fim_enquanto")

            elif token[0] == 'tk_if':
                j=i+1
                condicao = ""
                while self.lista_tokens[j][0] != ':':
                    condicao += " "+self.lista_tokens[j][1]
                    j+=1
                self.cod_intermediario.append("se {0} entao".format(condicao))
                self.log_intermediario.write("Comando condicional `if` reconhecido\n ") 

            elif token[0] == 'tk_end_if':
                self.cod_intermediario.append("fim_se")     

            elif token[0] == 'tk_else':
                self.cod_intermediario.append("senao")
                self.log_intermediario.write("Comando condicional `else` reconhecido\n ") 


            i+=1
        self.write_intermediario(self.cod_intermediario)
        self.log_intermediario.close()     

    def write_intermediario(self, cod):
        intermediario = open("cod_intermediario.txt","w")
        for line in cod:
            intermediario.write(line+"\n")
        intermediario.close()

    def read_intermediario(self):
        intermediario = open("cod_intermediario.txt","r")
        for line in intermediario:
            print(line)
        intermediario.close()

    def log_intermediary(self):
        log_int = open("log_intermediario.txt","r")
        for log in log_int:
            print(log)
        log_int.close()