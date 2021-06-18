from lexico import Analisador_Lexico
from sintatico import Analisador_Sintatico
from sintatico2 import Analisador_Sintatico2
analisador_lexico = Analisador_Lexico("C:\\Users\\danub\\OneDrive\\Área de Trabalho\\git\\Compiladores-TwoP\\arquivo_fonte.txt")

analisador_lexico.obter_tabela_tokens()
list_tokens = analisador_lexico._tabela_de_simbolos

print("*"*50)
print("\t\t\t ANALISADOR LÉXICO \t\t\t")
print("*"*50)
print("[Token, Lexema, Linha, Coluna]")

for v in (list_tokens):
  print(v)

print("*"*50)

###############Sintático###########
print()
print()
#analisador_sintatico = Analisador_Sintatico(list_tokens)
analisador_sintatico = Analisador_Sintatico2(list_tokens)
#analisador_sintatico.valor_producao()
analisador_sintatico.verificacao_sintatica()
analisador_sintatico.log_operacoes()
print()
#analisador_sintatico.leitura_tokens()




