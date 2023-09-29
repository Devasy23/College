%token IF ELSE WHILE ID EQ NE LT GT LE GE

%%

statement: IF '(' expression ')' '{' statements '}' ELSE '{' statements '}'
         | WHILE '(' expression ')' '{' statements '}'
         ;

expression: ID EQ ID
          | ID NE ID
          | ID LT ID
          | ID GT ID
          | ID LE ID
          | ID GE ID
          ;

statements: statement
          | statement statements
          ;

%%

def p_error(p):
    print("Syntax error in input!")

import ply.yacc as yacc
parser = yacc.yacc()
