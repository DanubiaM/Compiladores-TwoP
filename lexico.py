import errno
import os


class Analisador_Lexico:

    def __init__(self, arquivo_fonte):
        self._cabeca = 0
        self._fita = []
        self._numero_de_linha = 1
        self._tabela_de_simbolos = []
        self._lexema = ''
        self._fim_de_linha = "\n"
        self.caracter_especiais = ['(', ')', '=', ';', '+', '-', '/', '*', '>', '<', '&', '|', ':', '\"']
        self._arquivo_fonte = arquivo_fonte

        
        if not os.path.isfile(self._arquivo_fonte):
            print("Erro Léxico: não foi possivel encontrar arquivo fonte", FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self._arquivo_fonte))

        else:
            self._arquivo = open(self._arquivo_fonte, "r")

    # Sempre que chamado, o lexema é atualizado.
    def _obter_caracter(self):
        if self._cabeca < len(self._fita):
            self._letra = self._fita[self._cabeca]
            self._cabeca += 1

            if self._letra != self._fim_de_linha or not self._letra.isspace():
                self._lexema += self._letra
            return self._letra
        else:
            return '\n'

    # Método chamado no main para iniciar  a leitura do arquivo e a chamada dos estados
    def obter_tabela_tokens(self):
        for self._linha in self._arquivo:
            self._fita = list(self._linha)
            self._q0()
            self._numero_de_linha += 1
            self._cabeca = 0

        self._arquivo.close()
        return self._tabela_de_simbolos         #lista de tokens e seus lexemas

    #Metodos auxiliares
    def volta_um_caracter(self):
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._cabeca -= 1

    def adc_token_fim_de_linha(self, token):
        self._tabela_de_simbolos.append([token, self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''

    def adc_token_espaco(self, token):
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append([token, self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._q0()

    def adc_token_especial(self, token):
        self._lexema = self._lexema[:len(self._lexema) - 1]
        self._tabela_de_simbolos.append([token, self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()

    def _q0(self):
        self._caracter = self._obter_caracter()

        if 's' == self._caracter:
            self._q1()

        elif 'i' == self._caracter:
            self._q11()

        elif 'r' == self._caracter:
            self._q15()

        elif 'w' == self._caracter:
            self._q19()

        elif 'e' == self._caracter:
            self._q24()

        elif self._caracter.isdigit():
            self._q34()

        elif ')' == self._caracter:
            self._q35()

        elif '(' == self._caracter:
            self._q36()

        elif ('+' == self._caracter) or ('-' == self._caracter) or ('*' == self._caracter) or ('/' == self._caracter):
            self._q37()

        elif ('&' == self._caracter) or ('|' == self._caracter):
            self._q38()

        elif ';' == self._caracter:
            self._q39()

        elif '=' == self._caracter:
            self._q40()

        elif '\"' == self._caracter:
            self._q41()

        elif self._caracter.islower():
            self._q44()

        elif self._caracter == ':':
            self._q45()

        elif ('>' == self._caracter) or ('<' == self._caracter):
            self._q46()

        elif self._fim_de_linha == self._caracter:
            pass

        elif self._caracter.isspace():
            self._lexema = ''
            self._q0()
        else:
            print(
                "Erro lexico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca, self._caracter))

    # s
    def _q1(self):
        self._caracter = self._obter_caracter()
        if 't' == self._caracter:
            self._q2()
        elif 'c' == self._caracter:
            self._q6()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":
            self._q44()
        elif self._caracter.isspace():
             self.volta_um_caracter()
             self._q44()
        else:
            print(
                "Erro lexico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca, self._caracter))

    # t
    def _q2(self):
        self._caracter = self._obter_caracter()
        if 'a' == self._caracter:
            self._q3()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":
            self._q44()
        elif self._caracter.isspace():
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca, self._caracter))

    # a
    def _q3(self):
        self._caracter = self._obter_caracter()
        if 'r' == self._caracter:
            self._q4()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":
            self._q44()
        elif self._caracter.isspace():
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca, self._caracter))

    # r
    def _q4(self):
        self._caracter = self._obter_caracter()
        if 't' == self._caracter:
            self._q5()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()
        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca, self._caracter))

    # ESTADO FINAL: lexema start reconhecida
    def _q5(self):
        self._caracter = self._obter_caracter()


        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_start_program")

        elif self._caracter.isspace():
            self.adc_token_espaco("tk_start_program")

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_start_program")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # c
    def _q6(self):
        self._caracter = self._obter_caracter()

        if 'r' == self._caracter:
            self._q7()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()
        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # r
    def _q7(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q8()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()
        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # e
    def _q8(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q9()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()
        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # e
    def _q9(self):
        self._caracter = self._obter_caracter()

        if 'n' == self._caracter:
            self._q10()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()
        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: lexema screen reconhecido
    def _q10(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_screen")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_screen")


        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_screen")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # i
    def _q11(self):
        self._caracter = self._obter_caracter()

        if 'n' == self._caracter:
            self._q12()

        elif 'f' == self._caracter:
            self._q14()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # n
    def _q12(self):
        self._caracter = self._obter_caracter()

        if 't' == self._caracter:
            self._q13()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado Final: reconhecimento to lexema int
    def _q13(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_int")

        elif self._caracter.isspace():
            self.adc_token_espaco("tk_int")

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_int")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado Final: reconhecimento do lexema if
    def _q14(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_if")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_if")

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_if")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # r
    def _q15(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q16()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # e
    def _q16(self):
        self._caracter = self._obter_caracter()

        if 'a' == self._caracter:
            self._q17()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # a
    def _q17(self):
        self._caracter = self._obter_caracter()

        if 'd' == self._caracter:
            self._q18()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Reconhecimento do lexema read
    def _q18(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_read")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_read")

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_read")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # w
    def _q19(self):
        self._caracter = self._obter_caracter()

        if 'h' == self._caracter:
            self._q20()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # h
    def _q20(self):
        self._caracter = self._obter_caracter()

        if 'i' == self._caracter:
            self._q21()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # i
    def _q21(self):
        self._caracter = self._obter_caracter()

        if 'l' == self._caracter:
            self._q22()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # l
    def _q22(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q23()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Reconhecimento do lexema while
    def _q23(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_while")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_while")


        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_while")


        elif self._caracter.isdigit() or self._caracter.islower():  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # e
    def _q24(self):
        self._caracter = self._obter_caracter()

        if 'n' == self._caracter:
            self._q25()

        elif 'l' == self._caracter:
            self._q47()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # n
    def _q25(self):
        self._caracter = self._obter_caracter()

        if 'd' == self._caracter:
            self._q26()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: reconhece o estado final end, porem existem mais estados possiveis apos a letra e
    def _q26(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_end_program")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_end_program")

        # caso seja endwhile
        elif 'w' == self._caracter:
            self._q29()

        # caso seja endif
        elif 'i' == self._caracter:
            self._q27()

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_end_program")


        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # i
    def _q27(self):
        self._caracter = self._obter_caracter()

        if 'f' == self._caracter:
            self._q28()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: encontrado lexema endif
    def _q28(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_end_if")

        elif self._caracter.isspace():
            self.adc_token_espaco("tk_end_if")


        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_end_if")

        elif self._caracter.isdigit() or self._caracter.islower():  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # w
    def _q29(self):
        self._caracter = self._obter_caracter()

        if 'h' == self._caracter:
            self._q30()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # h
    def _q30(self):
        self._caracter = self._obter_caracter()

        if 'i' == self._caracter:
            self._q31()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # i
    def _q31(self):
        self._caracter = self._obter_caracter()

        if 'l' == self._caracter:
            self._q32()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # l
    def _q32(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q33()
        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: encontrado lexema endwhife
    def _q33(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("tk_end_while")


        elif self._caracter.isspace():
            self.adc_token_espaco("tk_end_while")

        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("tk_end_while")


        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Digito
    def _q34(self):
        self._caracter = self._obter_caracter()

        if self._caracter.isdigit():  # caso seja um numero ira continuar chamando o proprio metodo
            self._q34()

        elif self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("num")

        elif self._caracter.isspace():
            self.adc_token_espaco("num")


        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("num")

        else:#Problema: Caso apos o numero vier uma letra, deve tratar essa situação. Ex int 1n1;
            print("Erro Léxcio: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))
            self._lexema = ""
            self.volta_um_caracter()            
            self._q0()

    # Estado final: reconhece )
    def _q35(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha(")")


        elif self._caracter.isspace():
            self.adc_token_espaco(")")


        elif self._caracter in self.caracter_especiais or self._caracter.isdigit() or self._caracter.islower():
            self.adc_token_especial(")")



        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: reconhece (
    def _q36(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("(")


        elif self._caracter.isspace():
            self.adc_token_espaco("(")


        elif self._caracter in self.caracter_especiais or self._caracter.isdigit() or self._caracter.islower():
            self.adc_token_especial("(")
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Operacoes matematicas
    def _q37(self):
        self._caracter = self._obter_caracter()

        if self._caracter.isspace():  # a + b
            self.adc_token_espaco("op_mat")


        elif (self._caracter in self.caracter_especiais) or (self._caracter.isdigit()) or (self._caracter.islower()):
            self.adc_token_especial("op_mat")



        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Reconhece conectores lógicos
    def _q38(self):
        self._caracter = self._obter_caracter()
        """
            Situacoes de uso dos conectores lógicos
                S1 = if a & b   S2 = a | 2
                Sempre após o conector deve ter: numero, id ou espaço. Nunca sera usado em fim de linha e entre caracteres especiais
        """
        if self._caracter.isspace():
            self.adc_token_espaco("c_logico")

        elif self._caracter.isdigit() or self._caracter.isalpha():
            self.adc_token_especial("c_logico")

            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: reconhece ;
    def _q39(self):
        self._caracter = self._obter_caracter()

        if self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha(";")

        elif self._caracter.isspace():
            self.adc_token_espaco(";")


        elif self._caracter in self.caracter_especiais or self._caracter.isdigit() or self._caracter.islower():
            self.adc_token_especial(";")


        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: reconhece =
    def _q40(self):
        self._caracter = self._obter_caracter()

        """
            Situacoes onde o = pode estar
            variavel = 1
            variavel=a
            = é um operador de atribuicao, logo não pode estar no fim de linha e nem ter caracteres especiais após ele.
            Apenas espaco, id ou num.
        """
        if self._caracter.isspace():
            self.adc_token_espaco("tk_atribuicao")

        elif self._caracter.isdigit() or self._caracter.isalpha():  # caso id =4 ou id=a
            self.adc_token_especial("tk_atribuicao")

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # "
    def _q41(self):
        self._caracter = self._obter_caracter()
        """
            SITUACAO DE USO:
             -> é utilizado dentro do tk_screen, screen("string")
             problema: quando for ler algo do tipo "Avatar" a palavra avatar nao vai ser reconhecida  como um string
             por nao ter definido ainda um string, e também nao sera reconhecido como id, pois n pode começar com letra 
             maiuscula.
             Regras: Após " pode ter, espaço, numeros, . , %, , por fim deve ser finalizado com outro ".
        """
        if self._caracter.isdigit() or self._caracter.isalpha() or self._caracter.isspace() or self._caracter == "!" or self._caracter == ",":
            self._q42()

        elif self._caracter == "\"":  # logo nao vai existir texto entre eles, ou seja nao precisa da etapa q42.
            self._q43()
        else:
            print(
                "Erro  Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    def _q42(self):
        self._caracter = self._obter_caracter()

        if self._caracter.isdigit() or self._caracter.isalpha() or self._caracter.isspace() or self._caracter == "!" or self._caracter == ",":
            self._q42()
        elif self._caracter == "\"":
            self._q43()

        else: #Situacao screen("Teste); <- erro, entretando é necessário tratar o erro.
            
            print("Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))
            self._lexema = ""
            self.volta_um_caracter()            
            self._q0()


    # Estado Final: Reconhecimento do token string.
    def _q43(self):
        self._caracter = self._obter_caracter()
        """
            Deve ser finalizado com )
        """
        if self._caracter.isspace():

            self._lexema = self._lexema[:len(self._lexema) - 1]
            self._q43()


        elif self._caracter == ")":
            self.adc_token_especial("string")

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # id
    def _q44(self):
        self._caracter = self._obter_caracter()

        if self._caracter.isdigit() or self._caracter.isalpha() or self._caracter == '_':  # em caso de ter mais caracteres
            self._q44()

        elif self._caracter == self._fim_de_linha:
            self.adc_token_fim_de_linha("id")


        elif self._caracter.isspace():
            self.adc_token_espaco("id")


        elif self._caracter in self.caracter_especiais:
            self.adc_token_especial("id")

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Reconhece :
    def _q45(self):
        self._caracter = self._obter_caracter()

        """
            Situacoes de uso :
            
            if condicao :
            start:
            :end
            
            : deve aparecer sempre no fim de algum comando,seguido por fim de linha, ou seguido por um estado final de uma condicao.
            Não pode ter espaco em sua frente, nem numeros ou caracteres especiais.
        """
        if self._caracter == self._fim_de_linha:

            self.adc_token_fim_de_linha(":")


        elif self._caracter.isspace():
            self.adc_token_espaco(":")


        elif self._caracter.islower():  #:end
            self.adc_token_especial(":")


        else:
            print(
                "Erro  Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    # Estado final: Reconhece operadores lógicos
    def _q46(self):
        self._caracter = self._obter_caracter()

        if self._caracter.isspace():
            self.adc_token_espaco("op_logico")

        elif self._caracter.isdigit() or self._caracter.isalpha():
            self._lexema = self._lexema[:len(self._lexema) - 1]
            self._tabela_de_simbolos.append(["op_logico", self._lexema, self._numero_de_linha, self._cabeca - len(self._lexema)])
            self._lexema = ''
            self._cabeca -= 1
            self._q0()
        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    def _q47(self):
        self._caracter = self._obter_caracter()

        if 's' == self._caracter:
            self._q48()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    def _q48(self):
        self._caracter = self._obter_caracter()

        if 'e' == self._caracter:
            self._q49()

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # pode ser um id
            self._q44()

        elif self._caracter.isspace():  # pode ser um id, desconsiderar o espaço
            self.volta_um_caracter()
            self._q44()

        else:
            print(
                "Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))

    #Estado final: reconhece lexema else
    def _q49(self):
        self._caracter = self._obter_caracter()



        if self._caracter.isspace():
            self.adc_token_espaco("tk_else")

        elif self._caracter == ":":
            self.adc_token_especial("tk_else")

        elif self._caracter.isdigit() or self._caracter.islower() or self._caracter == "_":  # é um id
            self._q44()
        else:
            print("Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(
                    self._numero_de_linha, self._cabeca - len(self._lexema), self._caracter))




