import re
import os
class Codigo_Final:

    def __init__(self, cod_intermediario):
        self.codigo_final = [] 
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
        self._arquivo = open(cod_intermediario, "r")

        for line in self._arquivo:
            self.codigo_intermediario.append(line)
        self._arquivo.close()

    def inicia_geracao(self):
        """Variaveis"""
        self.obter_tabela_variaveis()           #Obtem as variaveis 
        self.getAddr_var()                      #Cria endereços para as variaveis
        self.codigo_final.append(".global main")
        self.codigo_final.append("{0}       @empilhamento endereco de retorno".format("main:\npush {ip, lr}"))
        
        #self.codigo_final.append("main:\n push{ip, lr} '{0}".format("@empilhamaento endereço de retorno"))
        
        
        for line in  self.codigo_intermediario:
            #print(line.split()) 
            if line.split()[0] == 'leia':
                    self.codigo_final.append("{0}       @load addres of pattern number".format("LDR R0, =format"))
                    self.codigo_final.append("{0}       @load addres of variable".format("LDR R1, ="+line.split()[1]))
                    self.codigo_final.append("BL scanf  @call function for read")                    
            elif line.split()[0] == 'escreva':
                
                print(line.split()[1])
                self.codigo_final.append("{0}           @load addres of pattern number".format("LDR R0, ="+self.getAddr_var(line.split()[1])))
                self.codigo_final.append("BL printf      @call function for write")
                    
            elif line.split()[0] == 'se':
                print(line.split())
                self.label_if = self.getLabel()
                self.label_else = self.getLabel() 
                self.label_endif = self.getLabel()         
                self.stack_label.append(self.label_endif) #Label for endif

                self.calcula_expressao(line.split()[1])  
                self.codigo_final.append("pop {R0}")   
                self.codigo_final.append("MOV R1, R0")    
                self.calcula_expressao(line.split()[3])
                self.codigo_final.append("pop {R0}")   
                self.codigo_final.append("MOV R2, R0")
                self.codigo_final.append("CMP R1, R2")
                i=0
                
                if len(line.split()) >5:
                    for item in line.split():
                                                          
                        if item == "&" or item ==  "|":
                            
                            self.getExpBool(line.split()[i-2],item)                                              
                            self.calcula_expressao(line.split()[i+1]) 
                            self.codigo_final.append("pop {R0}")     
                            self.codigo_final.append("MOV R1, R0")    
                            self.calcula_expressao(line.split()[i+3])
                            self.codigo_final.append("pop {R0}")   
                            self.codigo_final.append("MOV R2, R0")
                            self.codigo_final.append("CMP R1, R2")
                            self.getExpBool(line.split()[i+2],item)
 
                        i+=1
                    print(line.split()[i-5])
                    if line.split()[i-5] == "|": self.codigo_final.append("B {0}      @label content else".format(self.label_else))
    
                else:                    
                    self.getExpBool(line.split()[2])    
                    
                self.stack_label.append(self.label_else)
                self.codigo_final.append("{0}:      @label content if".format(self.label_if))
                
                """if(line.split()[2] == ">"):                    
                    self.codigo_final.append("BLE {0}".format(label))
                    self.codigo_final.append("B {0}".format(label_else))
                elif line.split()[2] == "<":
                    self.codigo_final.append("BLT {0}".format(label))
                    self.codigo_final.append("B {0}".format(label_else))
                self.codigo_final.append("{0}:      @label content if".format(label))"""    
            elif line.split()[0] == 'fim_se':
                self.codigo_final.append("{0}:      @label for endif".format(self.stack_label.pop()))
  
            elif  line.split()[0] == 'senao':
                self.codigo_final.append("B {0}      @jump for endif".format(self.label_endif))                
                self.codigo_final.append("{0}:      @label for else".format(self.stack_label.pop()))
            
                  
            elif  line.split()[1] == '=':
                
                self.calcula_expressao(line.split(" ",2)[2].strip())
                self.codigo_final.append("pop {R1}          @pops in R1")
                self.codigo_final.append("LDR R0, ={0}      @load address".format(line.split()[0]))
                self.codigo_final.append("STR R1, [R0]      @store  result")
        self.codigo_final.append("pop {ip, pc}")
        self.addr_var.append(".global printf")
        self.addr_var.append(".global scanf")

        #print(self.codigo_final)   
        intermediary = [str(a) for a in self.codigo_final]
        print( "\n".join(intermediary))
        addr = [str(a) for a in self.addr_var]
        print( "\n".join(addr))
        #print(self.addr_var)
      

    def getExpBool(self, conector,op = None ):
        if op == "&" or op == None:
            self.codigo_final.append("@AND OPERATION")
            if conector == ">":
                 self.codigo_final.append("BLT {0}      @case Val1<Val2".format(self.label_else))
            elif conector == "<":
                print("here")
                self.codigo_final.append("BGT {0}       @case Va1>Val2".format(self.label_else))
        elif op == "|":
            self.codigo_final.append("@OR OPERATION")
            if conector == "<":
                self.codigo_final.append("BLT {0}      @case Val1<Val2".format(self.label_if))
            elif  conector == ">":
                self.codigo_final.append("BGT {0}       @case Va1>Val2".format(self.label_if))


             
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
        elif re.search("^\"", atr):
            #print(atr)            
            self.cont_string += 1
            self.addr_var.append(".balign 8")
            self.addr_var.append("string_{0}: .asciz {1}".format(self.cont_string,atr))
            

            return "string_"+str(self.cont_string)
        #caso seja uma atribuicao ja declarada
        else:
            return "format"

    def getLabel(self):
        self.cont_label +=1
        return "L{0}".format(self.cont_label)

    def calcula_expressao(self, expressao):
        
        _expressao =[]
        _expressao.append(expressao)
        #_expressao.split(" ").trim
        
        if len(expressao) > 1:
            for atr in _expressao[0].split(" "): 
                   
                if atr.strip().islower():
                    #print(atr)
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
                #Ultima alteração
                self.codigo_final.append("push {R0}         @stack result content")

            else:
                self.codigo_final.append("LDR R0, ={0}      @load addres for variable".format(expressao))
                self.codigo_final.append("LDR R0, [R0]      @load data of variable")
