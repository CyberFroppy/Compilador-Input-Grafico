# Compiler design

## Graphical Input Compiler 
Simple compiler created for the Compiler Design Course of August - December 2020. 
## Table of contents
- [Team](#team)
- [Technology Stack](#technology-stack)
- [How to use PLY](#How-to-Use-PLY)
- [Requirements of PLY](#Requirements-of-PLY)
- [Management Tools](#management-tools)

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

## Bitacora de Avances 
### Avance 1
Se trabajó en el Lexer y el parser en su primera versión. 

### Avance 2 
Se investigó acerca de la GUI para poder generar el código y probarlo en el compilador. 

### Avance 3 
Se termino de corregir el lexer y se modifico el parser para que funcionara, se creo el cubo semántico y la tabla de variables. Tambien se definió el como se puede hacer la gui.

### Avance 4
Se corrigieron y completaron todas las reglas de parseo asi como se creo la tabla de varibles y funciones neuralgicas para ello.

### Avance 5
Se termino la tabla de variables locales y globales y puntos neuralgicos para guarda cada una de esta asi como las funciones.

