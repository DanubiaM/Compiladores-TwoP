class Dicionarios:
    def __init_ (self):
        self.producoes = {
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

        self.nao_terminais = {
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

        self.terminais = {
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

    def getProducoes(self):
        return self.producoes