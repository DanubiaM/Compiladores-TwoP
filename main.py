
import argparse

from lexico import Analisador_Lexico
from sintatico import Analisador_Sintatico
from semantico import Analisador_Semantico
#analisador_lexico = Analisador_Lexico("C:\\Users\\danub\\OneDrive\\Área de Trabalho\\git\\Compiladores-TwoP\\arquivo_fonte.fon")

#Método responsavel por retornar a lista de tokens.
def list_tokens(arquivo):
  analisador_lexico = Analisador_Lexico(arquivo)
  analisador_lexico.obter_tabela_tokens()       
  return analisador_lexico._tabela_de_simbolos

#Método do analisador sintático
def _parser(args):
  lista_tokens = list_tokens(args)
  analisador_sintatico = Analisador_Sintatico(lista_tokens)
  analisador_sintatico.verificacao_sintatica()
  analisador_sintatico.log_operacoes()

#Método do analisador léxico
def lexical_analyzer(args):
  lista_tokens = list_tokens(args)   
  print_table_tokens(lista_tokens)

#Metodo do analisador semântico
def semantic_analyzer(args):
  lista_tokens = list_tokens(args)
  analisador_semantico = Analisador_Semantico(lista_tokens)
  analisador_semantico.inicia_analise()

#Impressao da tabela de tokens
def print_table_tokens(list_tokens):
  print("*"*50)
  print("\t\t\t ANALISADOR LÉXICO \t\t\t")
  print("*"*50)
  print("[Token, Lexema, Linha, Coluna]")
  for v in (list_tokens):
    print(v)
  print("*"*50)

def all(args):
  lista_tokens = list_tokens(args)   
  print_table_tokens(lista_tokens)
  analisador_sintatico = Analisador_Sintatico(lista_tokens)
  analisador_sintatico.verificacao_sintatica()
  analisador_sintatico.log_operacoes()

if __name__ == '__main__':

  #criando um objeto parser
  parser = argparse.ArgumentParser(description = "Compilador da Linguagem TwoP!")  
  parser.add_argument('-tudo', metavar="tudo", help="exibe todas as listagens do compilador")
  parser.add_argument('-lt', metavar="listtokens", help="exibe a listagem dos Tokens")
  parser.add_argument('-ls', metavar="parser", help="exibe o LOG do analisador sintático")
  parser.add_argument('-lse', metavar="semanticanalysis", help="exibe o LOG do analisador semântico")

  args = parser.parse_args()  
  if args.tudo:
    all(args.tudo)    
  elif args.lt:
    lexical_analyzer(args.lt)  
  elif args.ls:
    _parser(args.ls)
  elif args.lse:
    semantic_analyzer(args.lse)
  