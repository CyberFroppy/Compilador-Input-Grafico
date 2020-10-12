from .ply import lex

# Language's reserved keywords.
reserved = {
    'program': 'PROGRAMA',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE'
}

# Tokens
tokens = [
    'ID', 'DDOT', 'DOTCOMA', 'LBRACKET', 'RBRACKET', 'EQUALS', 'GREATERT', 'LESST', 'GRLESST', 'LPAREN', 'RPAREN', 'DOT', 'COMA', 'CTESTRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'CTEI', 'CTEF',
] + list(reserved.values())

t_DDOT = r':'
t_DOTCOMA = r';'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_EQUALS = r'='
t_GREATERT = r'>'
t_LESST = r'<'
t_GRLESST = r'<>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMA = r'\,'
t_CTESTRING = r'".*"'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_CTEI = r'[1-9][0-9]*'
t_CTEF = r'[1-9][0-9]*\.[0-9]'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check if matched id is a reserved keyword.
    t.type = reserved.get(t.value, 'ID')
    return t

# Track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters
t_ignore = ' \t'

# Error handling rule for lexer


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
