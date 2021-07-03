"""
from ExceptionSintatic import ExceptionSintatic
from dicionario import Dicionarios
dic = {
    0 :["tk_start_programa",":", "LISTA_COMANDOS", ":", "tk_end_program"],
    1 :["COMANDO",";", "LISTA_COMANDOS"],
    2 : [],
    3 : ["tk_read", "(", "id", ")"],
    4 : ["tk_screen", "(", "PUTS", ")"],
    5 : ["DECLARACAO_VAR"],
    6: ["id", "tk_atribuicao", "EXPRESSAO"],
    7 : ["CONDICIONAL", ":", "tk_end_while"],
    8 : ["REPETICAO", ":", "tk_end_while"],
    9 : ["tk_int", "id"],
    10 : ["tk_if","EXPRESSAO", ":", "LISTA_COMANDOS", "ELSE_CONDICAO"],
    11 : ["tk_else", ":", "LISTA_COMANDOS"],
    12 : [],
    13 : ["tk_while", "EXPRESSAO",":", "LISTA_COMANDOS", "ELSE_CONDICAO"],
    14 : ["OPERANDO", "TAIL"],
    15 :["(", "EXPRESSAO", ":", "LISTA_COMANDOS"],
    16 :"OPERACAO",
    17 :[],
    18 : ["c_logico", "EXPRESSAO"],
    19 : ["op_logico", "EXPRESSAO"],
    20 :["op_mat", "EXPRESSAO"],
    21 : "id",
    22 : "num",
    23 : "string",
    24: "id"
}
dic2 = {
   'PROGRAMA': 2,
   'LISTA_COMANDOS': [1, 2],
   'COMANDO': [3, 4, 5, 6 , 7, 8],
   'DECLARACAO_VAR' : 9,
   'CONDICIONAL': 10,
   'ELSE_CONDICAO': [11, 12],
   'REPETICAO': 13,
   'EXPRESSAO': [14, 15],
   'OPERANDO': [21,22],
   'TAIL': [16,17],
   'OPERACAO': [18, 19, 20],
   'PUTS': [23, 24]  
}
dic3 = {
    'num': [14,22],
    'op_mat': [16,20],
    'c_logico': [16, 18],
    'op_logico': [16, 19],
    'tk_read': [1,3],
    'tk_screen' :[1,4],
    'tk_if': [1, 7, 10],
    'tk_int': [1, 5, 9],
    'tk_else':[2, 11],
    'tk_while':[1, 8, 13],
    'tk_start_program': 0,
    'tk_end_program': [],
    'tk_end_if': [],
    'tk_end_while': [],
    'tk_atribuicao': [],
    'string': 23,
    'id': [1, 6, 14, 21, 24],
    ';': 17,
    ')': 17,
    '(': 15,
    ':':[2, 12, 17]

}

xm = 'id'
xl = 'COMANDO'
pilha = ['$', "PROGRAMA"] 




for i in dic2.keys():
    if i == xl:
       u = list(dic2[i])

for j in dic3.keys():
    if j == xm:
       v = list(dic3[j])



        
for i in dic2.keys():
    if i == xl:
       u = list(dic2[i])
    for j in dic3.keys():
          if j == xm:
            v = list(dic3[j])


for x in v:
    #print(x)
    for y in u:
        if x == y:
            ts = x             

val_pilha =dic[ts]

for i in val_pilha:
    pilha.append(i)

print(val_pilha)
pilha.pop()
print(pilha)
print(ts)
print("v: ",v)
print("u:",u)
#print(keys1)

    """ 
"""
        print("X:",x)
        print("Y:",y)
        
        for i in x:
            #print(i)
            for j in y:
                print(j)
                if i == j:

            #print("First List: ",self.list_tokens[0][0]) 
            #print("Topo Pilha : ",self.pilha_sintatica[-1])
            #self.leitura_tokens()
             #print("...Desempilhou... ")  
print("X",x)
        print("Y", y)
              #try:
        producao = list(set(x).intersection(y)) # Não deve haver possibilidade de producao ser uma lista
                                                    # pois x e y devem ter apenas 1 valo em comum.
        #except:
            #Caso intersectio não encontre um valor em comum, o tokem não possui uma producao para aquele nao terminal.
            #print("Erro sintático: não possível encontrar uma producao válida para o valor {0} na linha {1} e coluna {2}. [error performing parsing]".format(self.list_tokens[0][1], self.list_tokens[0][2], self.list_tokens[0][3]))
            #sys.exit()
        #print(producao[0])
    """
""" 
#arquivo = open("arquivo_fonte.fon","r")

#print(arquivo.readlines())
#l1 = -1
#l2 = 0
#try:    
#    #l1 = [7]
from lexico import Analisador_Lexico
from sintatico import Analisador_Sintatico
analisador_lexico = Analisador_Lexico("C:\\Users\\danub\\OneDrive\\Área de Trabalho\\git\\Compiladores-TwoP\\arquivo_fonte.fon")
analisador_lexico.obter_tabela_tokens()  
lista_tokens = analisador_lexico._tabela_de_simbolos
class Teste:
    
    def __init__ (self, lista_tokens):
        self.dic = {}  
        self.lista_tokens =  lista_tokens
        self.le()

    def le(self):    
        for list_t in self.lista_tokens:
            if (list_t[0] == 'id'):
                self.dic[list_t[1]] = [list_t[0],'4','5']
                self.teste(list_t)
        print(self.dic)        
    #print(list_t[1])
    def teste(self, list_t):
        list_atual =  self.dic[list_t[1]]
        list_atual[1] =  list_atual[1] +1
        self.dic.update(list_t[1]== list_atual)
        print(self.dic) 
   """
dic = {'BRA':["Brazil", "BRAZUCA", 4],
        "EUA":"Estados unidos"}

lista = dic['BRA']
lista[2] = lista[2] +1
dic['BRA'] = lista
lista2 = ['BR', 'EUA']
if dic.get(lista2[0]):
    print("SDFS")
if dic[lista2[1]]:
    print("EUA")
#print(lista)
#print(dic)





#    print(list(set(l2).intersection(l1)))
#except :
#    raise ExceptionSintatic(l1,l2)


"""pilha = [1, 2, 3 ,4]
print(pilha)

pilha.append(5)
pilha.append(7)
print(pilha)

pilha.pop()
print(pilha)

print(pilha[-1])


"""

"""
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append([token, self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()

 
                 self._lexema = self._lexema[:len(self._lexema) - 1]
                 self._cabeca -= 1
             
           

        if self._caracter == self._fim_de_linha:
        self._tabela_de_simbolos.append(
            ["tk_screen", self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''

    elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append(
            ["tk_screen", self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._q0()

          self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append(
            ["tk_start_program", self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._q0()


    elif self._caracter in self.caracter_especiais:
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append(
            ["tk_sreen", self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os



class Analisador_Lexico:

    def __init__(self, arquivo_fonte):
        self._cabeca = 0 #ok
        self._fita = []
        self._numero_de_linha = 1 #ok
        self._tabela_de_simbolos = []
        self._lexema = ''
        self._fim_de_linha = "\n"
        self._especiais = ['(', ')', '=', ';', ['+', '-', '/', '*'], ['>', '<'], ['&', '|']]
        self._arquivo_fonte = arquivo_fonte #ok
        
        if not os.path.exists(self._arquivo_fonte):
            print("Erro ao encontrar arquivo fonte: ")

        else:
            self._arquivo = open(self._arquivo_fonte, "r")

    def _avancar_cabeca(self):
        self._cabeca += 1

    #seria a coluna
    def _posicao_cabeca(self):
        return self._cabeca

    def _atualizar_numero_linha(self):
        self._numero_de_linha += 1

    #obtendo caracter onde  a cabeca esta posicionada
    def _obter_caracter(self):
        if self._cabeca < len(self._fita):
            self._letra = self._fita[self._cabeca]
            self._avancar_cabeca()
            if self._letra != self._fim_de_linha or not self._letra.isspace():
                self._lexema += self._letra
            return self._letra
        else:
                return '\n'

    def obter_tabela_tokens (self):
        for self._linha in self._arquivo:
            self._fita = list(self._linha)
            self._q0()
            self._atualizar_numero_linha()
            self._cabeca = 0
        self._arquivo.close()
        return self._tabela_de_simbolos

    def _q0(self):
        self._caracter =  self._obter_caracter()
        if 's' == self._caracter:
            print("aceito")
            #self._q1()
        elif 'i' == self._caracter:
            print("aceito")
            #self._q11()
        elif 'r' == self._caracter:
            #self._q15()
            print("aceito")
        elif 'w' == self._caracter:
            #self._q19()
            print("aceito")
        elif 'e' == self._caracter:
            #self._q24()
            print("aceito")
        elif self._caracter.isdigit():
            #self._q34()
            print("aceito")
        elif ')' == self._caracter:
            #self._q35()
            print("aceito")
        elif '(' == self._caracter:
            #self._q36()
            print("aceito")
        elif ('+' or '-' or'*' or '/') == self._caracter:
            #self._q37()
            print("aceito")
        elif ( '&' or '|') == self._caracter:
            #self._q38()
            print("aceito")
        elif ';' == self._caracter:
            #self._q39()
            print("aceito")
        elif '=' == self._caracter:
            #self._q40()
            print("aceito")
        elif '"' == self._caracter:
            #self._q41()
            print("aceito")
        elif self._caracter.islower():
            #self._q44()
            print("aceito")
        elif self._fim_de_linha == self._caracter:
            pass
        elif self._caracter.isspace():
            self._lexema = ''
            self._q0()
        else:
            print ("erro lexico")

"""
