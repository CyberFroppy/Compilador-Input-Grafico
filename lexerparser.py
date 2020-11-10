import ply.lex
import ply.yacc
import sys

############### LEXER ###############

# Reserved words
reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'then': 'THEN',
    'to': 'TO',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'void': 'VOID',
    'module': 'MODULE',
    'return': 'RETURN',
    'write': 'WRITE',
    'read': 'READ'
}
# Token List
tokens = [
    'ID',
    'COMMENT',
    'COLON',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'EQUAL',
    'DBEQUALS',
    'NOTEQUAL',
    'GREATERT',
    'LESST',
    'AND',
    'OR',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COMA',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'CTESTRING',
    'CTEINT',
    'CTEF',
] + list(reserved.values())

t_COLON = r':'
t_SEMICOLON = r';'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_EQUAL = r'='
t_DBEQUALS = r'=='
t_NOTEQUAL = r'\!='  # revisar Regex
t_GREATERT = r'>'
t_LESST = r'<'
t_AND = r'&'  # Revisar Regex
t_OR = r'\|'  # Revisar Regex
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_CTESTRING = r'".*"'
t_CTEINT = r'[1-9][0-9]*'
t_CTEF = r'[1-9][0-9]*\.[0-9]'

# Ignorar tabuladores y espacios
t_ignore = ' \t'


# Revisar si el id es una plabra reservada
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Revisar comentarios


def t_comment(t):
    r'\%%.*'
    pass
# Coneo de lineas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Manejo de errores lexicos


def t_error(t):
    # print("Lexical error  {0}  found in line  {1}  ".format(
    #     t.value[0], t.lineno))
    print('Scanner error ', t)
    t.lexer.skip(1)

############### ESTRUCTURAS ###############


current_func = '#global'
current_var = None
current_type = None
symbol_table = {
    '#global': {
        'vars': {},
    }
}

next_constant_int = 0
next_constant_float = 1000
next_constant_char = 2000
next_local_int = 3000
next_local_float = 4000
next_local_char = 5000
next_global_int = 6000
next_global_float = 7000
next_global_char = 8000
constant_table = {}


cuadruplos = []
pila_operadores = []
pila_operandos = []
pila_tipos = []

def print_todo():
    print('tabla de simbolo: ', symbol_table)
    print('tabla de constantes: ', constant_table)
    print('pila operadores: ', pila_operadores)
    print('pila operandos: ', pila_operandos)
    print('pila tipos: ', pila_tipos)
    print('cuadruplos: ', cuadruplos)

############### PARSER ###############

# Productions
start = 'programa'


def p_programa(p):
    '''programa : PROGRAM ID SEMICOLON vars module main
                | PROGRAM ID SEMICOLON module main
                | PROGRAM ID SEMICOLON vars main
                | PROGRAM ID SEMICOLON main'''
    pass


def p_main(p):
    '''main : MAIN bloque_module'''


def p_vars(p):
    '''vars : VAR vars_aux'''


def p_vars_aux(p):
    '''vars_aux : ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux
                | ID n_seen_var_name COLON tipo n_set_var_type DOT'''

def p_vars_func(p):
    '''vars_func : ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func
                 | ID n_seen_var_name COLON tipo n_set_var_type'''

def p_tipo(p):
    '''tipo : INT n_seen_type
            | FLOAT n_seen_type'''


def p_bloque_module(p):
    '''bloque_module : LBRACKET vars estatuto_aux RBRACKET
                     | LBRACKET vars RBRACKET
                     | LBRACKET estatuto_aux RBRACKET
                     | LBRACKET RBRACKET '''


def p_bloque(p):
    '''bloque : LBRACKET estatuto_aux RBRACKET
              | LBRACKET RBRACKET'''


def p_estatuto_aux(p):
    '''estatuto_aux : estatuto estatuto_aux
                    | estatuto'''


def p_estatuto(p):
    '''estatuto : asignacion SEMICOLON
                | condicion SEMICOLON
                | escritura SEMICOLON
                | return SEMICOLON
                | for SEMICOLON
                | while SEMICOLON
                | call_module SEMICOLON'''


def p_asignacion(p):
    'asignacion : ID EQUAL expresion'


def p_expresion(p):
    '''expresion : exp AND expresion
                 | exp'''


def p_exp(p):
    '''exp : exp_aux OR exp
           | exp_aux '''


def p_exp_aux(p):
    '''exp_aux : exp_aux2 GREATERT exp_aux2
               | exp_aux2 LESST exp_aux2
               | exp_aux2 NOTEQUAL exp_aux2
               | exp_aux2 DBEQUALS exp_aux2
               | exp_aux2'''


def p_exp_aux2(p):
    '''exp_aux2 : term PLUS exp_aux2
                | term MINUS exp_aux2
                | term'''


def p_term(p):
    '''term : factor MULTIPLY term
            | factor DIVIDE term
            | factor'''


def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | CTEINT n_seen_factor_int
              | CTEF 
              | ID n_seen_factor_id'''


def p_module(p):
    '''module : MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module
              | MODULE tipo ID n_seen_func_name params bloque_module module
              | MODULE VOID n_seen_type ID n_seen_func_name params bloque_module
              | MODULE tipo ID n_seen_func_name params bloque_module'''

def p_params(p):
    '''params : LPAREN vars_func RPAREN
              | LPAREN RPAREN'''

def p_call_module(p):
    '''call_module : ID LPAREN expresion RPAREN 
                   | ID LPAREN RPAREN'''

def p_return(p):
    '''return : RETURN expresion'''


def p_for(p):
    '''for : FOR asignacion TO CTEINT LBRACKET estatuto RBRACKET'''


def p_while(p):
    '''while : WHILE LPAREN expresion RPAREN LBRACKET estatuto RBRACKET'''


def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque ELSE bloque
                 | IF LPAREN expresion RPAREN bloque'''


def p_escritura(p):
    'escritura : PRINT LPAREN escritura_aux RPAREN'


def p_escritura_aux(p):
    '''escritura_aux : expresion COMA escritura_aux
                     | CTESTRING COMA escritura_aux
                     | expresion
                     | CTESTRING'''


def p_error(p):
    if not p:
        return
    print("Parser error ", p)
    print_todo()
    sys.exit()
    

def error(message):
    print('Error: ', message)
    print_todo()
    sys.exit()

############### PUNTOS NEURALGICOS ###############


def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    current_type = p[-1]


def p_n_seen_var_name(p):
    'n_seen_var_name : '
    global symbol_table,current_var, current_func
    if(current_func != "#global"):
      
        symbol_table[current_func]['vars'][p[-1]] = {
            'type': None,
            'address': None
        }
        current_var = p[-1]
    else:
        symbol_table['#global']['vars'][p[-1]] = {
            'type': None,
            'address': None
        }
        current_var = p[-1]
    

def p_n_seen_func_name(p):
    'n_seen_func_name : '
    global symbol_table, current_func, current_type, next_local_int, next_local_float, next_local_char
    next_local_int = 3000
    next_local_float = 4000
    next_local_char = 5000
    symbol_table[p[-1]] = {
        'vars': {},
        'type': current_type,
    }
    current_func = p[-1]

def get_next_var_address():
    global current_func, current_type, next_global_int, next_global_float, next_global_char,next_local_int, next_local_float, next_local_char
    if current_func == '#global':
        if current_type == 'int':
            aux = next_global_int
            next_global_int += 1
        elif current_type == 'float':
            aux = next_global_float
            next_global_float += 1
        elif current_type == 'char':
            aux = next_global_char
            next_global_char += 1
    else:
        if current_type == 'int':
            aux = next_local_int
            next_local_int += 1
        elif current_type == 'float':
            aux = next_local_float
            next_local_float += 1
        elif current_type == 'char':
            aux = next_local_char
            next_local_char += 1
    return aux

def p_n_set_var_type(p):
    'n_set_var_type : '
    global symbol_table, current_func, current_var, current_type
    symbol_table[current_func]['vars'][current_var] = {
        'type': current_type,
        'address': get_next_var_address()
    }

def search(id):
    global symbol_table, current_func
    if id in symbol_table[current_func]['vars']:
        return symbol_table[current_func]['vars'][id]['type']
    elif id in symbol_table['#global']['vars']:
        return symbol_table['#global']['vars'][id]['type']
    else:
        error('No se encontró la viarable ' + id)

def p_n_seen_factor_id(p):
    'n_seen_factor_id : '
    global pila_operandos, pila_tipos
    pila_operandos.append(p[-1])
    pila_tipos.append(search(p[-1]))

def p_n_seen_factor_int(p):
    'n_seen_factor_int : '
    global pila_operandos, pila_tipos
    ### asignar la dirección constante
    pila_operandos.append(p[-1])
    pila_tipos.append('int')


############### EJECUCION ###############


# Build Lexer
lexer = ply.lex.lex()

# Build the parser
parser = ply.yacc.yacc()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please send a file.')
        raise SyntaxError('mali needs 1 file.')
    program_name = sys.argv[1]

    with open(program_name, 'r') as file:
        try:
            parser.parse(file.read())
            print('FINISHED')
            print_todo()
        except:
            pass
