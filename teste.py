pilha = [1, 2, 3 ,4]
print(pilha)

pilha.append(5)
pilha.append(7)
print(pilha)

pilha.pop()
print(pilha)

print(pilha[-1])




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
