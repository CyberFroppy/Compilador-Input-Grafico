import sys

#Funcion para manejar errores
def error(message):
  print(message)

#Funcion para leer el archivo y guardas la tabala de simbolos, cudruplos y tabla de constantes 
program_name = sys.argv[1]
with open(program_name, 'r') as file:
    global symbol_table, cuadruplos, raw_constant_table
    inp = eval(file.read())
    symbol_table = inp['symbol_table']
    cuadruplos = inp['cuadruplos']
    raw_constant_table = inp['constant_table']


#Estructuras de memoria local y constantes
global mem_global, mem_local, constant_table
mem_global = {}
mem_local = []
constant_table = {}

#Loop para voltear los valores de la tabala de constantes
for key, val in raw_constant_table.items():
    constant_table[val['address']] = key

global current

#Funcion para encontrar los valores en la memoria
def read(address, depth=-1):
    #Casteo para la comparacion
    address_n = int(address)
    val = None
    #Leer variables globales y castearlas adecuadamente
    if address_n >= 8000 and address_n < 9000:
        val = int(mem_global.get(address, None))
    elif address_n >= 9000 and address_n < 10000:
        val = float(mem_global.get(address, None))
    elif address_n >= 10000 and address_n < 11000:
        val = chr(mem_global.get(address, None))
    elif address_n >= 11000 and address_n < 12000:
        val = int(mem_global.get(address, None))

    #Leer variables locales y casteralas adecuadamente
    elif address_n >= 4000 and address_n < 5000:
        val = int(mem_local[depth].get(address, None))
    elif address_n >= 5000 and address_n < 6000:
        val = float(mem_local[depth].get(address, None))
    elif address_n >= 6000 and address_n < 7000:
        val = chr(mem_local[depth].get(address, None))
    elif address_n >= 7000 and address_n < 8000:
        val = int(mem_local[depth].get(address, None))

    #Leer constantes y castearlas adecuadamente
    elif address_n >= 0 and address_n < 1000:
        val = int(constant_table.get(address, None))
    elif address_n >= 1000 and address_n < 2000:
        val = float(constant_table.get(address, None))
    elif address_n >= 2000 and address_n < 3000:
        val = chr(constant_table.get(address, None))
    elif address_n >= 3000 and address_n < 4000:
        val = constant_table.get(address, None)
    if val is None:
        print(val)
        error('Acceso a variable no asignada')
        current = -1
        return
    return val

#Funcion para agregttar valores a la memoria
def write(address, value, depth=-1):
    global mem_local, mem_global
    if address >= 3000 and address < 6000:
         mem_local[depth][address] = value
    else: 
        mem_global[address] = value


current = [0]
while current[-1] != -1:
    if cuadruplos[current[-1]][0] == 'START':
        current[-1] = cuadruplos[current[-1]][3]
    elif cuadruplos[current[-1]][0] == 'END':
        print("Memoria Global: ")
        print(mem_global)
        print("Memoria Local: ")
        print(mem_local)
        print("Tabla de Constantes: ")
        print(constant_table)
        current[-1] = -1
    #Sumar    
    elif cuadruplos[current[-1]][0] == '+':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        res = valor1 + valor2
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Restar
    elif cuadruplos[current[-1]][0] == '-':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        res = valor1 - valor2
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Multiplicar
    elif cuadruplos[current[-1]][0] == '*':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        res = valor1 * valor2
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Division
    elif cuadruplos[current[-1]][0] == '/':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor2 == 0:
            error("Divison entre 0")
            current[-1] = -1
        else:
            res = valor1 / valor2
            write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Asignar
    elif cuadruplos[current[-1]][0] == '=':
        
        valor1 = read(cuadruplos[current[-1]][1])
        write(cuadruplos[current[-1]][3], valor1)
        current[-1] = current[-1]+1
    #Imprimir
    elif cuadruplos[current[-1]][0] == 'PRINT':
        valor1 = read(cuadruplos[current[-1]][3])
        print(valor1)
        current[-1] = current[-1]+1
    # #Leer
    elif cuadruplos[current[-1]][0] == 'READ':
        res = input()
        #TODO: verificar que el input esta correcto!
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Menor que
    elif cuadruplos[current[-1]][0] == '>':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 > valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Mayor que
    elif cuadruplos[current[-1]][0] == '<':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 < valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Igual
    elif cuadruplos[current[-1]][0] == '==':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 == valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Mayor igual
    elif cuadruplos[current[-1]][0] == '>=':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 >= valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Menor igual
    elif cuadruplos[current[-1]][0] == '<=':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 <= valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #No igual
    elif cuadruplos[current[-1]][0] == '!=':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 != valor2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #And
    elif cuadruplos[current[-1]][0] == '&&':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 == 2 and valor2 == 2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Or
    elif cuadruplos[current[-1]][0] == '|':
        valor1 = read(cuadruplos[current[-1]][1])
        valor2 = read(cuadruplos[current[-1]][2])
        if valor1 == 2 or valor2 == 2:
            res = 2
        else:
            res = 1
        write(cuadruplos[current[-1]][3], res)
        current[-1] = current[-1]+1
    #Goto en falso
    elif cuadruplos[current[-1]][0] == 'GOTOF':
        valor1 = read(cuadruplos[current[-1]][1])
        if valor1 == 1:
            current[-1] = cuadruplos[current[-1]][3]
        else:
            current[-1] = current[-1] + 1
    #Goto
    elif cuadruplos[current[-1]][0] == 'GOTO':
        current[-1] = cuadruplos[current[-1]][3]
    
    #ERA para la memoria de la funcion
    elif cuadruplos[current[-1]][0] == 'ERA':
         cuadruplos[-1][3]


    #Final de funcion
    elif cuadruplos[current[-1]][0] == 'RETURN':
    


    else:
        print('Instruccion no implementada: ', cuadruplos[current[-1]][0])
        current[-1] = -1
    
    print(cuadruplos[current[-1]][0])