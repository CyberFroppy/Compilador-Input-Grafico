import sys

def error(message):
  print(message)

program_name = sys.argv[1]
with open(program_name, 'r') as file:
    global symbol_table, cuadruplos, raw_constant_table
    input = eval(file.read())
    symbol_table = input['symbol_table']
    cuadruplos = input['cuadruplos']
    raw_constant_table = input['constant_table']


global mem_global, mem_local, constant_table
mem_global = {}
mem_local = []
constant_table = {}
for key, val in raw_constant_table.items():
    constant_table[val['address']] = key

global current 

def read(address, depth=-1):
    # val = mem_local[depth].get(address, None)
    # if not val:
    val = mem_global.get(address, None)
    if not val:
        val = constant_table.get(address, None)
        if not val:
            error('Acceso a variable no asignada')
            current = -1
            return
    return val


def write(address, value, depth=-1):
    global mem_local, mem_global
    # if address >= 3000 and address < 6000:
    #     mem_local[depth][address] = value
    # else: 
    mem_global[address] = value


current = [0]
while current[-1] != -1:
    if cuadruplos[current[-1]][0] == 'START':
        current[-1] = cuadruplos[current[-1]][3]
    elif cuadruplos[current[-1]][0] == 'END':
        current[-1] = -1
    elif cuadruplos[current[-1]][0] == '+':
        #print('hola')
        valor1 = int(read(cuadruplos[current[-1]][1]))
        #print(valor1)
        valor2 = int(read(cuadruplos[current[-1]][2]))
        #print(valor2)
        res = valor1 + valor2
        #print(res)
        write(cuadruplos[current[-1]][3], res)
        #print(cuadruplos[current[-1]][3])
        current[-1] = current[-1]+1
    elif cuadruplos[current[-1]][0] == '-':
        #print('hola')
        valor1 = int(read(cuadruplos[current[-1]][1]))
        #print(valor1)
        valor2 = int(read(cuadruplos[current[-1]][2]))
        #print(valor2)
        res = valor1 - valor2
        #print(res)
        write(cuadruplos[current[-1]][3], res)
        #print(cuadruplos[current[-1]][3])
        current[-1] = current[-1]+1
    elif cuadruplos[current[-1]][0] == '*':
        valor1 = int(read(cuadruplos[current[-1]][1]))
        valor2 = int(read(cuadruplos[current[-1]][2]))
        res = valor1 * valor2
        write(cuadruplos[current[-1]][3], res)
        #print(cuadruplos[current[-1]][3])
        current[-1] = current[-1]+1
    elif cuadruplos[current[-1]][0] == '/':
        valor1 = int(read(cuadruplos[current[-1]][1]))
        valor2 = int(read(cuadruplos[current[-1]][2]))
        res = valor1 / valor2
        write(cuadruplos[current[-1]][3], res)
        #print(cuadruplos[current[-1]][3])
        current[-1] = current[-1]+1
    elif cuadruplos[current[-1]][0] == '=':
        valor1 = int(read(cuadruplos[current[-1]][1]))
        write(cuadruplos[current[-1]][3], valor1)
        #print(cuadruplos[current[-1]][3])
        current[-1] = current[-1]+1
    elif cuadruplos[current[-1]][0] == 'PRINT':
        valor1 = int(read(cuadruplos[current[-1]][3]))
        print(valor1)
        current[-1] = current[-1]+1
    else:
        print('Instruccion no implementada: ', cuadruplos[current[-1]][0])
        current[-1] = -1