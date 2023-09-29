tokens = (
    'IF',
    'ELSE',
    'WHILE',
    'ID',
    'EQ',
    'NE',
    'LT',
    'GT',
    'LE',
    'GE'
)

t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
