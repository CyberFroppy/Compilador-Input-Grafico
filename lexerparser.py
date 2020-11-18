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
    'CTEC'
    # Agregando CTEC
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
t_AND = r'&&'  # Revisar Regex
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
#Agregando constante
t_CTEC = r'(\'[^\']*\')'

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


############### CUBO SEMANTICO ###############

def return_type_cubo(left_oper,right_oper,operator):
    return cubo_semantico[left_oper][right_oper][operator]
cubo_semantico = {
   'int':{
        'int':{
            '+': 'int',
            '-': 'int',
            '/': 'int',
            '*': 'int',
            '<': 'bool',
            '>': 'bool',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'bool',
            '>=': 'bool'
        },
        'float':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'bool',
            '>=': 'bool'

        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'

        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'

        }
    },
    'float':{
        'int':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'bool',
            '>=': 'bool'
        },
        'float':{
            '+': 'float',
            '-': 'float',
            '/': 'float',
            '*': 'float',
            '<': 'bool',
            '>': 'bool',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'bool',
            '>=': 'bool'
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        }
    },
    'bool':{
        'int':{
           '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'float':{
           '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'bool':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'bool',
            '>': 'bool',
            '&&': 'bool',
            '|': 'bool',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'char':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '<>': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        }
    },
    'char':{
        'int':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'float':{
            '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'bool':{
             '+': 'err',
            '-': 'err',
            '/': 'err',
            '*': 'err',
            '<': 'err',
            '>': 'err',
            '&&': 'err',
            '|': 'err',
            '<>': 'bool',
            '==': 'bool',
            '<=': 'err',
            '>=': 'err'
        },
        'char':{
            '+': 'char',
            '-': 'char',
            '/': 'char',
            '*': 'char',
            '<': 'bool',
            '>': 'bool',
            '&&': 'err',
            '|': 'err',
            '!=': 'bool',
            '==': 'bool',
            '<=': 'bool',
            '>=': 'bool'
        }
    }
}

############### ESTRUCTURAS ###############


current_func = '#global'
current_var = None
current_type = None
symbol_table = {
    '#global': {
        'vars': {},
    }
}

constant_table = {}
next_constant_int = 0
next_constant_float = 1000
next_constant_char = 2000
next_local_int = 3000
next_local_float = 4000
next_local_char = 5000
next_global_int = 6000
next_global_float = 7000
next_global_char = 8000


cuadruplos = []
pila_operadores = []
pila_operandos = []
pila_tipos = []
pila_saltos = [] 
contador = 0

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
    '''main : MAIN n_seen_func_name bloque_module'''


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
            | FLOAT n_seen_type
            | CHAR n_seen_type'''
        # Agregando char

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
    '''expresion : exp n_gen_and AND n_add_operator expresion
                 | exp n_gen_and '''


def p_exp(p):
    '''exp : exp_aux n_gen_or OR n_add_operator exp
           | exp_aux n_gen_or '''


def p_exp_aux(p):
    '''exp_aux : exp_aux2 n_gen_relational GREATERT n_add_operator exp_aux2
               | exp_aux2 n_gen_relational LESST n_add_operator exp_aux2
               | exp_aux2 n_gen_relational NOTEQUAL n_add_operator exp_aux2
               | exp_aux2 n_gen_relational DBEQUALS n_add_operator exp_aux2
               | exp_aux2 n_gen_relational '''


def p_exp_aux2(p):
    '''exp_aux2 : term n_gen_term PLUS n_add_operator exp_aux2 
                | term n_gen_term MINUS n_add_operator exp_aux2
                | term n_gen_term'''


def p_term(p):
    '''term : factor n_gen_factor MULTIPLY n_add_operator term 
            | factor n_gen_factor DIVIDE n_add_operator term 
            | factor n_gen_factor'''


def p_factor(p):
    '''factor : LPAREN n_push_fake_bottom expresion RPAREN n_pop_fake_bottom
              | CTEINT n_seen_factor_int
              | CTEF n_seen_factor_float
              | CTEC n_seen_factor_char
              | ID n_seen_factor_id'''
            #   Se agrego CTEC a factor


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
    '''condicion : IF LPAREN expresion RPAREN n_check_exp bloque ELSE n_else bloque n_fill_end
                 | IF LPAREN expresion RPAREN n_check_exp bloque n_fill_end'''


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
    aux = 0
    if current_func == '#global':
        if current_type == 'int':
            if next_global_int > 6999: 
                error('Exceso de variables')
            aux = next_global_int
            next_global_int += 1
        elif current_type == 'float':
            if next_global_float > 7999: 
                error('Exceso de variables')
            aux = next_global_float
            next_global_float += 1
        elif current_type == 'char':
            if next_global_char > 8999: 
                error('Exceso de variables')
            aux = next_global_char
            next_global_char += 1
    else:
        if current_type == 'int':
            if next_local_int > 3999: 
                error('Exceso de variables')
            aux = next_local_int
            next_local_int += 1
        elif current_type == 'float':
            if next_local_float > 4999: 
                error('Exceso de variables')
            aux = next_local_float
            next_local_float += 1
        elif current_type == 'char':
            if next_local_char > 5999: 
                error('Exceso de variables')
            aux = next_local_char
            next_local_char += 1
    return aux

#Funcion para agregar las direcciones a las constantes
def get_next_const_address(constant_type):
    global current_type,constant_table, next_constant_int, next_constant_float, next_constant_char
    aux = 0
    if constant_type == 'int':
        if next_constant_int > 999: 
                error('Exceso de constantes')
        aux = next_constant_int
        next_constant_int += 1
    elif constant_type == 'float':
        if next_constant_float > 1999: 
                error('Exceso de constantes')
        aux = next_constant_float
        next_constant_float += 2
    elif constant_type == 'char':
        if next_constant_char > 2999: 
                error('Exceso de constantes')
        aux = next_constant_char
        next_constant_char += 1
    return aux


def p_n_set_var_type(p):
    'n_set_var_type : '
    global symbol_table, current_func, current_var, current_type
    symbol_table[current_func]['vars'][current_var] = {
        'type': current_type,
        'address': get_next_var_address()
    }


def search_type(id):
    global symbol_table, current_func
    if id in symbol_table[current_func]['vars']:
        return symbol_table[current_func]['vars'][id]['type']
    elif id in symbol_table['#global']['vars']:
        return symbol_table['#global']['vars'][id]['type']
    else:
        error('No se encontró la variable ' + id)


#Funcion para comprobar que no se repite un ID 
def search_address(id):
    global symbol_table, current_func
    if id in symbol_table[current_func]['vars']:
        return symbol_table[current_func]['vars'][id]['address']
    elif id in symbol_table['#global']['vars']:
        return symbol_table['#global']['vars'][id]['address']
    else:
        error('No se encontró el address de la variable ' + id)

#Funcion para poder agregar a sus respectivas pilas los operandos y los tipos
def p_n_seen_factor_id(p):
    'n_seen_factor_id : '
    global pila_operandos, pila_tipos
    pila_operandos.append(search_address(p[-1]))
    pila_tipos.append(search_type(p[-1]))


def p_n_seen_factor_int(p):
    'n_seen_factor_int : '
    global pila_operandos, pila_tipos, constant_table, next_constant_int
    ### asignar la dirección constante
    if (p[-1] not in constant_table):
        constant_table[p[-1]] = { 
            'address': get_next_const_address('int'),
            'type': 'int'
        }
    pila_operandos.append(constant_table[p[-1]]['address'])
    pila_tipos.append('int')


#Agregando punto neuralgico para los tipos float
def p_n_seen_factor_float(p):
    'n_seen_factor_float : '
    global pila_operandos, pila_tipos, constant_table, next_constant_float 
    if (p[-1] not in constant_table):
        constant_table[p[-1]] = { 
            'address': get_next_const_address('float'),
            'type' : 'float'
        }
    pila_operandos.append(constant_table[p[-1]]['address'])
    pila_tipos.append('float')


#Agregando punto neuralgico para los tipos char
def p_n_seen_factor_char(p):
    'n_seen_factor_char : '
    global pila_operandos, pila_tipos, constant_table, next_constant_char
    if (p[-1] not in constant_table):
        constant_table[p[-1]] = { 
            'address': get_next_const_address('char'),
            'type' : 'char'
        }
    pila_operandos.append(constant_table[p[-1]]['address'])
    pila_tipos.append('char')


#Funcion para agregar los operadores a la pila de operadores
def p_n_add_operator(p):
    'n_add_operator : '
    global pila_operadores
    pila_operadores.append(p[-1])

# Punto neuralgico para los operadores de suma y resta
def p_n_gen_term(p):
    'n_gen_term : '
    operator_ident(['+','-'])

# Punto neuralgico para los operadores de multiplicacion y division
def p_n_gen_factor(p):
    'n_gen_factor : '
    operator_ident(['*','/'])

def p_n_gen_relational(p):
    'n_gen_relational : '
    operator_ident(['>', '<', '!=', '=='])

def p_n_gen_or(p):
    'n_gen_or : '
    operator_ident(['|'])

def p_n_gen_and(p):
    'n_gen_and : '
    operator_ident('&&')

def p_n_push_fake_bottom(p):
    'n_push_fake_bottom : '
    global pila_operadores
    pila_operadores.append('(')

def p_n_pop_fake_bottom(p):
    'n_pop_fake_bottom : '
    global pila_operadores
    top = pila_operadores.pop()
    if top != '(':
        error('n_pop_fake_bottom')

#Funcion para poder generar cuadruplos
def operator_ident(ops):
    global pila_operadores, pila_tipos, cuadruplos, current_type
    if len(pila_operadores) > 0:
        if pila_operadores[-1] in ops:
            right_operand = pila_operandos.pop()
            right_type =  pila_tipos.pop()
            left_operand = pila_operandos.pop()
            left_type =  pila_tipos.pop()
            operator = pila_operadores.pop()
            result_type = return_type_cubo(left_type,right_type,operator)
            if result_type != 'err':
                current_type = result_type
                result = get_next_var_address()
                cuadruplos.append([operator, left_operand, right_operand, result])
                pila_operandos.append(result)
                pila_tipos.append(result_type)
            else: 
                error('Error en el cuadruplo')  

# 1 - Punto neuralgico para revisar que la expresion tenga un valor bool y genera el cuadruplo GotoF
def p_n_check_exp(p):
    '''n_check_exp : '''
    global pila_operadores, contador, pila_tipos, pila_saltos, cuadruplos, current_type
    exp_type = pila_tipos.pop()
    print(exp_type)
    if exp_type != 'bool':
        error('Type Mismatch')
    else:
        result = pila_operandos.pop()
        quad = ['GOTOF',result,'-',0]
        cuadruplos.append(quad)
        contador += 1 
        pila_saltos.append(contador - 1)
        
# 2 - Punto neuralgico para completar el cuadruplo 
def p_n_fill_end(p):
    '''n_fill_end : '''
    global pila_saltos, contador 
    end = pila_saltos.pop()
    cuadruplos[end][3] = contador

# 3 - Punto neuralgico para crear el GOTO al else 
def p_n_else(p):
    '''n_else : '''
    global pila_saltos, contador, cuadruplos
    goto_aux = ['GOTO', '-', '-', 0]
    contador += 1 
    cuadruplos.append(goto_aux)
    false = pila_saltos.pop()
    pila_saltos.append(contador - 1)
    cuadruplos[false][3] = contador


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
        parser.parse(file.read())
        print('FINISHED')
        print_todo()
