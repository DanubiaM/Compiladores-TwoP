import re
class Codigo_Final:

    def __init__(self, cod_intermediario):
        self.codigo_intermediario = cod_intermediario
        self.codigo_final = []
        self.variaveis = []
        self.addr_var = []
        self.cont_string = 0
    def inicia_geracao(self):
        """Variaveis"""
        self.obter_tabela_variaveis()           #Obtem as variaveis 
        self.getAddr_var()                      #Cria endereços para as variaveis
        self.codigo_final.append(".global main")
        self.codigo_final.append("{0} @empilhamaento endereço de retorno".format("main:\n push{ip, lr}"))
        
        #self.codigo_final.append("main:\n push{ip, lr} '{0}".format("@empilhamaento endereço de retorno"))
        print(self.codigo_intermediario)
        for line in  self.codigo_intermediario:
            
            if line.split()[0] == 'leia':
                self.codigo_final("{0} @load addres of pattern number".format("LDR R0, =format"))
                self.codigo_final("{0} @load addres of variable".format("LDR R1, ="+line.split()[1]))
                self.codigo_final("BL scanf @call function for read")
                """
                Outras opções do livro seria:
                LDR R0, addr_format
                MOV R1, SP
                BL scanf
            
                """
            elif line.split()[0] == 'escreva':

                #Chama metodo para obter endereço da variavel ou string
                
                self.codigo_final("{0} @load addres of pattern number".format("LDR R0, ="+self.getAddr_var(line.split()[1])))
                self.codigo_final("BL print @call function for write")
                """
                Outras opções do livro seria:
                LDR R1, [SP] @pega o endereço da entrada scanf
                LDR R0, addr_messageout               
                BL print

                ou 
                LDR R0, =format
                BL print
                """
            elif  line.split()[0] == '=':
                print()
    #Metodo para obter variaveis
    def obter_tabela_variaveis(self):
        
        for line in self.codigo_intermediario:            
            if re.search("^Var", line):
                self.variaveis.extend( re.search("^Var", line))


    def getAddr_var(self, atr = None):
        if atr == None:
            self.addr_var.append(".data")
            for var in self.variaveis:
                self.addr_var.append(".baling 8")
                self.addr_var.append("{0}: .word 0".format(var))

        elif re.search("^\" ", atr):
            self.addr_var.append(".baling 8")
            self.addr_var.append("string_{0}: .asciz\"{1}\"".format(self.cont_string +1,atr))
            return "string_"+self.cont_string
        else:
            return atr