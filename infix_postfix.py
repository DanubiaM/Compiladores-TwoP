"""
algorithm obtained in https://cppsecrets.com/users/2582658986657266505064717765737646677977/INFIX-TO-POSTFIX-CONVERSION-USING-STACK.php
(modify)
"""

OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
OPERADORES = set(['+','-','/','*'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 

 

def infix_to_postfix(expression): #input expression

    stack = [] # initially stack empty

    output = '' # initially output empty

    
    i = 0
    for ch in expression:
        
            
         
        if ch in OPERADORES:
            output+=" "
                
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            
            output+=""+ch

        elif ch=='(':  # else operators should be put in stack
                
                stack.append('(')

        elif ch==')':
            
            while stack and stack[-1]!= '(':
                
                output+=" "+stack.pop()
                #aqui sai +--*/
            stack.pop()

        else:

                # lesser priority can't be on top on higher or equal priority    

                # so pop and put in output   

            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                
                output+=" "+stack.pop()
            
            #Aqui adiciona o +-*/    
            stack.append(ch)
        
    while stack:
        
        output+=" "+stack.pop()
        
    #print("Saida \t"+output)
    return output

 

#expression = input('Enter infix expression \t')

#print('infix expression: \t',expression)

#print('postfix expression: \t',infix_to_postfix(expression))