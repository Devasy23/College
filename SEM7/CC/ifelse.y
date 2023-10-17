%{
/* Definition Section*/
#include<stdio.h>
#include <stdlib.h>
%}
%token VAR NUMBER IF THEN ELSE LE GE NE EQ AND OR
%right '='
%left '<' '>' LE GE NE EQ AND OR
%left '+' '-' '*' '/' '%' '!'
%right UMINUS
%%

S:STMT {printf("Correct input\n");exit(0);};
STMT:IF '(' EXPR2 ')' THEN STMT1';' ELSE STMT1';'|IF '(' EXPR2 ')' THEN STMT1';';
STMT1:STMT|E;
E:VAR'='E|E'+'E|E'-'E|E'*'E|E'/'E|E'<'E|E'>'E|E LE E|E GE E|E EQ E|E NE E|E OR E|E AND E|VAR|NUMBER;
EXPR2:E'<'E|E'>'E|E LE E|E GE E|E EQ E|E NE E|E OR E|E AND E|VAR|NUMBER;
%%
#include "lex.yy.c"

main()
{
printf("\nEnter expr:\n");
yyparse();
}
void yyerror()
{
printf("Invalid EXPR\n\n");
}


