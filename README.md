# Compiler design

## Graphical Input Compiler 
Simple compiler created for the Compiler Design Course of August - December 2020. 
## Table of contents
- [Team](#team)
- [Technology Stack](#technology-stack)
- [How to use PLY](#How-to-Use-PLY)
- [Requirements of PLY](#Requirements-of-PLY)
- [Management Tools](#management-tools)
- [Manual de Usuario](#manual-de-usuario)
- [Bitacora de Avances](#bitacora-de-avances)

Team
======
| Name            |      Id     | Email              |
|:-:              |:-:          |:-:                 | 
| Omar Lopez      |A01282035    | A01282035@itesm.mx | 
| Carlos Tamez    |A00817514    | A00817514@itesm.mx |

Technology Stack
=================
| Technology   | Version  |
|:-:           |:-:       |
| Python       | 3.8.3    |

How to Use PLY
==============

PLY consists of two files : lex.py and yacc.py.  These are contained
within the `ply` directory which may also be used as a Python package.
To use PLY, simply copy the `ply` directory to your project and import
lex and yacc from the associated `ply` package as in this project. For example:

```python
from .ply import lex
from .ply import yacc
```

Alternatively for future projects, you can copy just the files lex.py and yacc.py
individually and use them as modules however you see fit.  For example:

```python
import lex
import yacc
```

If you wish, you can use the install.py script to install PLY into
virtual environment.

PLY has no third-party dependencies. 

The docs/ directory contains complete documentation on how to use
the system.  Documentation available at https://ply.readthedocs.io
  

Requirements of PLY
===================
PLY requires the use of Python 3.6 or greater.  However, you should
use the latest Python release if possible.  It should work on just
about any platform.  

Note: PLY does not support execution under `python -OO`.  It can be
made to work in that mode, but you'll need to change the programming
interface with a decorator.  See the documentation for details.

Management Tools
================
You should ask for access to this tools if you don't have it already:

- [Backlog](https://trello.com/b/aSU8Q6P8/compiladores)
- [Documentation](https://drive.google.com/drive/folders/1QNZR0BwuejZxBOVS2LcruMwqnEL-zrOb?usp=sharing)

Manual de Usuario
===================

## Empezar un programa
El lenguaje Kiseki esta estrucutrado para que de forma sencilla empezar a programar

Primero es necesario crear un programa de la siguiente forma:
```
program Example;
main {

}
```

## Declarando variables 
Para declarar una variable en lenguaje Kiseki es necesario iniciar con la palabra "var" y despues con las variables teniendo su respectivo tipo separadas por punto y coma y teniendo un punto al terminar su declaracion de variables.

El lenguaje Kiseki soporta una declaracion de tipos int, float aunque solamente globales. Esto significa que es despues de declarar el nombre del programa y no dentro de funciones o dentro del main.

Una vez sabiendo esto podemos empezar a declarar nuestras variables.

```
program Example;
var aux1: int; aux2: int; aux3: int; aux4: int.

main {
}
```
## Asignar valor a una variable 
El objetivo de una variable es para poder almacenar datos, entonces para poder asignar estos datos a nuestras variables se tiene la siguiente sintaxis: el nombre de la variable, signo de =, el valor que se quiere almacenar (teniendo en cuenta el tipo de la variable) y terminar con punto y coma.

```
program Example;
var aux1: int; aux2: int; aux3: int; aux4: int.

main {
  aux1 =5;
  aux2 =3; 
  aux3 =4;
  aux4 =2;

}

```
## Uso de Condicionales 
En el lenguaje kiseki se soporta el uso de condicionales, funciona de manera que si se cumple la expresion que se le da antes del if te hara las operaciones que escribas despues de la expresion y sino podria haber un else dando otra instruccion o no.

La manera de escribir nuestro condicional es IF, parentesis que abre, la expresion, parentesis que cierra, abrir llaves, operaciones y si es que hay un else, agregarlo para terminar con un punto y coma como en el siguiente ejemplo.

```
program Example;
var aux1: int; aux2: int; aux3: int; aux4: int.

main {
  aux1 =5;
  aux2 =3; 
  aux3 =4;
  aux4 =2;

  if(aux1 > aux2 && aux1 == 5){
    aux2 = aux2 +1;
  }else {

  };
  
}

```

## Ciclo while 
En el lenguaje kiseki se permite el uso de ciclo while, este ejecutara una instruccion hasta que se cumpla la condicion que se inserte.

Tomando en cuenta el ejemplo siguiente para poder escribir nuestro codigo while: 

```
program Example;
var aux1: int; aux2: int; aux3: int; aux4: int.

main {
  aux1 =5;
  aux2 =3; 
  aux3 =4;
  aux4 =2;

  while(aux1 > aux4){
      aux4 = aux4 + 1;
  };
  
}
```

## Ver los valores dentro de una variable (Print)
Para poder ver los datos que guarda una variable podemos realizar la operacion print, que desplegara en consola los datos almacenados en la variable a imprimir. Tambien podemos imprimir numeros, o mensajes.
```
program Example;
var aux1: int; aux2: int; aux3: int; aux4: int.

main {
  aux1 =5;
  aux2 =3; 
  aux3 =4;
  aux4 =2;

  if(aux1 > aux2 && aux1 == 5){
    aux2 = aux2 +1;
};

print(aux2);
print(aux4);
print("hola");
print(5+4);
}
```
## Finalmente, Compilar y Ejecutar.
Para poder compilar el programa escrito es necesario usar la siguiente instruccion. 

```
python lexerparser.py test.txt
```

Siendo el test.txt el file de tu codigo y dependiendo de donde se encuentre tendras que hacer ligeras variaciones para poder compilarlo.

Para poder ejecutar el codigo escrito es necesario usar la siguiente isntruccion 
```
python MaquinaVirtual/maquina.py test.txt.o
```

Teniendo como diferencia que tu archivo se le agrega la extension ".o"


Bitacora de Avances 
===================

## Avance 1
Se trabajó en el Lexer y el parser en su primera versión. 

## Avance 2 
Se investigó acerca de la GUI para poder generar el código y probarlo en el compilador. 

## Avance 3 
Se termino de corregir el lexer y se modifico el parser para que funcionara, se creo el cubo semántico y la tabla de variables. Tambien se definió el como se puede hacer la gui.

## Avance 4
Se corrigieron y completaron todas las reglas de parseo asi como se creo la tabla de varibles y funciones neuralgicas para ello.

## Avance 5
Se termino la tabla de variables locales y globales y puntos neuralgicos para guarda cada una de esta asi como las funciones.

## Avance 6 
Se agrego la constante char, ademas de que se termino la tabla de constantes y se iniciaron los cuadruplos teniendo un error al generarlos

## Avance 7 
En el avance 7 se trabajaron los cuadruplos de decision y de ciclos, tambien se trabajo en la documentacion del compilador.