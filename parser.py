from .ply import yacc

# Productions
start = 'PROGRAMA'


def p_empty(p):
    'empty :'
    pass


def p_PROGRAMA(p):
    'PROGRAMA : PROGRAM ID DOTCOMA PROGRAMA_AUX BLOQUE'
    pass


def p_PROGRAMA_AUX(p):
    '''PROGRAMA_AUX : VARS
    | empty'''
    pass


def p_VARS(p):
    'VARS : VAR VARS_AUX DDOT TIPO DOTCOMA VARS_AUX2'
    pass


def p_VARS_AUX(p):
    '''VARS_AUX : ID COMA VARS_AUX
    | ID'''
    pass


def p_VARS_AUX2(p):
    '''VARS_AUX2 : VARS_AUX DDOT TIPO DOTCOMA VARS_AUX2
    | empty'''
    pass


def p_TIPO(p):
    '''TIPO : INT
    | FLOAT'''
    pass


def p_BLOQUE(p):
    'BLOQUE : LBRACKET ESTATUTO_AUX RBRACKET'
    pass


def p_ESTATUTO_AUX(p):
    '''ESTATUTO_AUX : ESTATUTO ESTATUTO_AUX
    | empty'''
    pass


def p_ESTATUTO(p):
    '''ESTATUTO : ASIGNACION
    | CONDICION
    | ESCRITURA'''
    pass


def p_ASIGNACION(p):
    'ASIGNACION : ID EQUALS EXPRESION DDOT'
    pass


def p_EXPRESION(p):
    'EXPRESION : EXP EXPRESION_AUX'
    pass


def p_EXPRESION_AUX(p):
    '''EXPRESION_AUX : GREATERT EXP
    | LESST EXP
    | GRLESST EXPRESION
    | empty'''
    pass


def p_CONDICION(p):
    'CONDICION : IF LPAREN EXPRESION RPAREN BLOQUE CONDICION_AUX DDOT'
    pass


def p_CONDICION_AUX(p):
    '''CONDICION_AUX : ELSE BLOQUE
    | empty'''
    pass


def p_ESCRITURA(p):
    'ESCRITURA : PRINT LPAREN ESCRITURA_AUX RPAREN DOTCOMA'
    pass


def p_ESCRITURA_AUX(p):
    '''ESCRITURA_AUX : EXPRESION ESCRITURA_AUX2
    | CTESTRING ESCRITURA_AUX2'''
    pass


def p_ESCRITURA_AUX2(p):
    '''ESCRITURA_AUX2 : DOT ESCRITURA_AUX
    | empty'''
    pass


def p_EXP(p):
    'EXP : TERMINO EXP_AUX'
    pass


def p_EXP_AUX(p):
    '''EXP_AUX : PLUS EXP
    | MINUS EXP
    | empty'''
    pass


def p_TERMINO(p):
    'TERMINO : FACTOR TERMINO_AUX'
    pass


def p_TERMINO_AUX(p):
    '''TERMINO_AUX : TIMES TERMINO
    | DIVIDE TERMINO
    | empty'''
    pass


def p_FACTOR(p):
    '''FACTOR : LPAREN EXPRESION RPAREN
    | FACTOR_AUX'''
    pass


def p_FACTOR_AUX(p):
    '''FACTOR_AUX : PLUS VARCTE
    | MINUS VARCTE
    | VARCTE'''
    pass


def p_VARCTE(p):
    '''VARCTE : ID
    | CTEI
    | CTEF'''
    pass

# Error handling rule for parser


def p_error(p):
    print("Done")
    if not p:
        print("End of File!")
        return

    while True:
        tok = parser.token()  # Get next token
        if not tok or tok.type == 'closebrac':
            break
    parser.restart()


# Build the parser
parser = yacc.yacc()


# Test it out
aux = int(input("1.Programa que cumple\n2.Programa que no cumple\n3.Documento\n"))

data = ""

if(aux == 1):
    data = '''program Example;
var aux1, aux2: float; aux3: int;
{

}'''

elif(aux == 2):
    data = '''programa ~'''

elif(aux == 3):
    f = open("example.duck", "r")
    if f.mode == 'r':
        data = f.read()
    else:
        print("Error: input File not found or redable")


result = parser.parse(data)
print(result)
