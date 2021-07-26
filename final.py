import re
import os
class Codigo_Final:

    def __init__(self, cod_intermediario):
        self.codigo_final = []         
        self.variaveis = []
        self.addr_var = []
        self.cont_string = 0
        self.cont_label = 0
        self.label_if= 0 
        self.label_endif = 0
        self.label_else = 0
        self.stack_label = []
        self.codigo_intermediario = []
        self.log_final = open("log_final.txt","w")
        self._arquivo = open(cod_intermediario, "r")

        for line in self._arquivo:
            self.codigo_intermediario.append(line)
        self._arquivo.close()

    def inicia_geracao(self):
        """Variaveis"""
        self.obter_tabela_variaveis()           #Obtem as variaveis 
        self.getAddr_var()                      #Cria endereços para as variaveis
        self.log_final.write("Declaração de variaveis realizada\n")

        self.codigo_final.append(".global main")
        self.codigo_final.append("{0}       @empilhamento endereco de retorno".format("main:\npush {ip, lr}"))
        self.log_final.write("Empilhamento de endereco de retorno\n")

        for line in  self.codigo_intermediario:
            
            if line.split()[0] == 'leia':
                    self.log_final.write("Comando read executado\n")
                    self.codigo_final.append("{0}       @load addres of pattern number".format("LDR R0, =format"))
                    self.codigo_final.append("{0}       @load addres of variable".format("LDR R1, ="+line.split()[1]))
                    self.codigo_final.append("BL scanf  @call function for read")                    
            elif line.split()[0] == 'escreva':
                self.log_final.write("Comando screen executado\n")
                self.codigo_final.append("{0}           @load addres of pattern number".format("LDR R0, ="+self.getAddr_var(line.split()[1:len(line.split())])))
                self.codigo_final.append("BL printf      @call function for write")
                    
            elif line.split()[0] == 'se':
                self.log_final.write("Comando if executado\n")
               
                self.label_if = self.getLabel()
                self.label_else = self.getLabel() 
                self.label_endif = self.getLabel()         
                #self.stack_label.append(self.label_endif) #Label for endif
                exp = []
                con = None
                i=0                
                for atr in line.split()[1:len(line.split())-1]:
                    exp.append(atr)
                    if atr == "&":
                       self.calc_expLogic(exp, atr)
                       con = atr
                       exp.clear()
                    if atr == "|":
                        self.calc_expLogic(exp, atr)
                        con = atr
                        exp.clear()                              
               
                self.calc_expLogic(exp, con)
                self.getExpBool(exp)   

                self.stack_label.append(self.label_else)
                self.codigo_final.append("{0}:      @label content if".format(self.label_if))

            elif line.split()[0] == 'fim_se':
                self.log_final.write("Fim do comando if \n")

                self.codigo_final.append("{0}:      @label for endif".format(self.stack_label.pop()))
  
            elif  line.split()[0] == 'senao':
                self.log_final.write("Comando else executado\n")

                self.codigo_final.append("B {0}      @jump for endif".format(self.label_endif))
                self.codigo_final.append("{0}:      @label for else".format(self.stack_label.pop()))
                self.stack_label.append(self.label_endif)                

            
            elif line.split()[0] == "enquanto":
                self.log_final.write("Comando while executado\n")

                self.label_if = self.getLabel()                
                self.label_else = self.getLabel()         
                self.stack_label.append(self.label_else) #Label for endif
                label_while = self.getLabel()
                self.stack_label.append(label_while)

                self.codigo_final.append("{0}:      @label for while".format(label_while))
                exp = []
                con = None
                i=0                
                for atr in line.split()[1:len(line.split())]:
                    exp.append(atr)
                    if atr == "&":
                       self.calc_expLogic(exp, atr)
                       con = atr
                       exp.clear()
                    if atr == "|":
                        self.calc_expLogic(exp, atr)
                        con = atr
                        exp.clear()                              
               
                self.calc_expLogic(exp, con)
                self.getExpBool(exp)

                self.codigo_final.append("{0}:      @label content while".format(self.label_if))

            elif line.split()[0] == "fim_enquanto":
                self.log_final.write("Fim do comando while\n")

                self.codigo_final.append("B {0}      @jump loop while".format(self.stack_label.pop()))
                self.codigo_final.append("{0}:      @label for endwhile".format(self.stack_label.pop()))

            elif  line.split()[1] == '=':
                self.log_final.write("Atribuicoes de variaveis executado\n")
                self.calcula_expressao(line.split(" ",2)[2].strip())
                self.codigo_final.append("pop {R1}          @pops in R1")
                self.codigo_final.append("LDR R0, ={0}      @load address".format(line.split()[0]))
                self.codigo_final.append("STR R1, [R0]      @store  result")
        
        self.codigo_final.append("pop {ip, pc}")
        self.addr_var.append(".global printf")
        self.addr_var.append(".global scanf")

        self.log_final.close()
        self.getFinal()          
        print("Final code generation performed successfully.")
        
        
    def getFinal(self):
        arquivo_final = open ("arquivo_saida.s","w")
        for line in self.codigo_final:            
            arquivo_final.write(line+"\n")
        for line in self.addr_var:            
            arquivo_final.write(line+"\n")    
        arquivo_final.close() 

    def log_finalCode(self):
        log_f = open("log_final.txt","r")
        for log in log_f:
            print(log)
        log_f.close()

    def calc_expLogic(self, exp, op = None):
        i=0
        expressao= ""
        c_log = ""       
        
        while i != len(exp):         
            
            if exp[i] == '>':                
                self.calcula_expressao(expressao)
                self.codigo_final.append("pop {R0}          @pops R0")        
                self.codigo_final.append("MOV R1, R0        @mov content for R1")                
                c_log = exp[i]
                expressao = ""

            elif exp[i] == "<":                
                self.calcula_expressao(expressao)
                self.codigo_final.append("pop {R0}          @pops R0")        
                self.codigo_final.append("MOV R1, R0        @mov content for R1")                
                c_log = exp[i]
                expressao = ""

            expressao +=" "+exp[i]                      
            i+=1

        self.calcula_expressao(expressao)
        self.codigo_final.append("pop {R0}      @pops R0")   
        self.codigo_final.append("MOV R2, R0        @mov content for r2")
        self.codigo_final.append("CMP R1, R2        @compar contents")               
        self.getExpBool(c_log , op)


    def getExpBool(self, conector,op = None ):        
        if op == "&" or op == None:
            self.codigo_final.append("@AND OPERATION")
            if conector == ">":
                 self.codigo_final.append("BLE {0}      @case Val1<Val2".format(self.label_else))
            elif conector == "<":                
                self.codigo_final.append("BGE {0}       @case Va1>Val2".format(self.label_else))
        elif op == "|":
            self.codigo_final.append("@OR OPERATION")
            if conector == "<":
                self.codigo_final.append("BLE {0}      @case Val1<Val2".format(self.label_if))
            elif  conector == ">":
                self.codigo_final.append("BGE {0}       @case Va1>Val2".format(self.label_if))


             
    #Metodo para obter variaveis
    def obter_tabela_variaveis(self):        
        for line in self.codigo_intermediario:                     
            if re.search("^_Var", line):               
                self.variaveis.append(line.split()[1])


    def getAddr_var(self, atr = None):
        
        #É chamado apenas uma vez no inicio, cria todos as variaveis
        if atr == None:
            self.addr_var.append(".data")
            self.addr_var.append(".balign 8")
            self.addr_var.append("format: .asciz \"%d\"")
            #print (self.variaveis)
            for var in self.variaveis:                
                self.addr_var.append(".balign 8")
                self.addr_var.append("{0}: .word 0".format(var.strip()))
        #Chamado para printar, caso tenha alguma string do tipo "text"        
        elif re.search("^\"", atr[0]):                        
            self.cont_string += 1
            self.addr_var.append(".balign 8")
            string =""
            for world in atr:
                string += world +" "
            self.addr_var.append("string_{0}: .asciz {1}".format(self.cont_string,string))
            return "string_"+str(self.cont_string)

        #caso seja uma atribuicao ja declarada
        else:
            self.calcula_expressao(atr[0])
            self.codigo_final.append("pop {R1}         @pops in R1")
            return "format"
            
    def getLabel(self):
        self.cont_label +=1
        return "L{0}".format(self.cont_label)

    def calcula_expressao(self, expressao):        
        
        _expressao =[]
        _expressao.append(expressao)      
 
        if len(expressao) > 1:
            for atr in _expressao[0].split(" "): 
                   
                if atr.strip().islower():
                    
                    self.codigo_final.append("LDR R0, ={0}      @load addres for variable".format(atr.strip()))
                    self.codigo_final.append("LDR R0, [R0]      @load data of variable")
                    self.codigo_final.append("push {R0}         @stack variable content")
                elif atr.strip().isdigit():
                    self.codigo_final.append("MOV R0, #{0}      @load number".format(atr.strip()))
                    self.codigo_final.append("push {R0}         @stack variable content")
                elif atr.strip() == "+":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("ADD R0, R0, R1    @sum operation")
                    self.codigo_final.append("push {R0}         @stack result content")
                elif atr.strip() == "-":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("SUB R0, R0, R1    @subtraction operation")
                    self.codigo_final.append("push {R0}         @stack result content")   
                elif atr.strip() == "*":
                    self.codigo_final.append("pop {R1}          @pops in R1")
                    self.codigo_final.append("pop {R0}          @pops in R0")
                    self.codigo_final.append("MUL R0, R0, R1    @multiplication operation")
                    self.codigo_final.append("push {R0}         @stack result content")
                elif atr.strip() == "/":   
                    self.codigo_final.append("pop {R2}          @pops in R1")
                    self.codigo_final.append("pop {R1}          @pops in R2")
                    self.codigo_final.append("MOV R0, #0        @init variable for resultable")
                    self.codigo_final.append("_division:        @create label")
                    self.codigo_final.append("SUBS R1, R1, R2    @subtraction operation")
                    self.codigo_final.append("ADD R0, R0,#1     @result division")
                    self.codigo_final.append("BHI _division     @jump case R1>R2")
                    self.codigo_final.append("push {R0}         @stack result content")
        else:
            if expressao.isdigit():           
                self.codigo_final.append("MOV R0, #{0}      @load addres for variable".format(expressao))              
                self.codigo_final.append("push {R0}         @stack result content")

            else:
                self.codigo_final.append("LDR R0, ={0}      @load addres for variable".format(expressao))
                self.codigo_final.append("LDR R0, [R0]      @load data of variable")
                self.codigo_final.append("push {R0}         @stack result content")

