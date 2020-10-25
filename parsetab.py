
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAID COLON SEMICOLON LBRACKET RBRACKET EQUAL GREATERT LESST DIFF LPAREN RPAREN DOT COMA PLUS MINUS MULTIPLY DIVIDE CTESTRING CTEINT CTEF PROGRAM VAR INT FLOAT IF ELSE PRINTempty :PROGRAMA : PROGRAM ID SEMICOLON PROGRAMA_AUX BLOQUEPROGRAMA_AUX : VARS\n    | emptyVARS : VAR VARS_AUX COLON TIPO SEMICOLON VARS_AUX2VARS_AUX : ID COMA VARS_AUX\n    | IDVARS_AUX2 : VARS_AUX COLON TIPO SEMICOLON VARS_AUX2\n    | emptyTIPO : INT\n    | FLOATBLOQUE : LBRACKET ESTATUTO_AUX RBRACKETESTATUTO_AUX : ESTATUTO ESTATUTO_AUX\n    | emptyESTATUTO : ASIGNACION\n    | CONDICION\n    | ESCRITURAASIGNACION : ID EQUAL EXPRESION COLONEXPRESION : EXP EXPRESION_AUXEXPRESION_AUX : GREATERT EXP\n    | LESST EXP\n    | DIFF EXPRESION\n    | emptyCONDICION : IF LPAREN EXPRESION RPAREN BLOQUE CONDICION_AUX COLONCONDICION_AUX : ELSE BLOQUE\n    | emptyESCRITURA : PRINT LPAREN ESCRITURA_AUX RPAREN SEMICOLONESCRITURA_AUX : EXPRESION ESCRITURA_AUX2\n    | CTESTRING ESCRITURA_AUX2ESCRITURA_AUX2 : DOT ESCRITURA_AUX\n    | emptyEXP : TERMINO EXP_AUXEXP_AUX : PLUS EXP\n    | MINUS EXP\n    | emptyTERMINO : FACTOR TERMINO_AUXTERMINO_AUX : MULTIPLY TERMINO\n    | DIVIDE TERMINO\n    | emptyFACTOR : LPAREN EXPRESION RPAREN\n    | FACTOR_AUXFACTOR_AUX : PLUS VARCTE\n    | MINUS VARCTE\n    | VARCTEVARCTE : ID\n    | CTEINT\n    | CTEF'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,24,],[0,-2,-12,]),'ID':([2,8,10,14,16,17,18,23,26,27,28,38,40,42,49,50,52,53,54,57,58,61,62,70,85,92,94,],[3,12,19,19,-15,-16,-17,12,33,33,33,33,33,33,12,-18,33,33,33,33,33,33,33,33,-27,-24,12,]),'SEMICOLON':([3,29,30,31,68,91,],[4,49,-10,-11,85,94,]),'VAR':([4,],[8,]),'LBRACKET':([4,5,6,7,49,67,74,75,89,94,95,],[-1,10,-3,-4,-1,10,-5,-9,10,-1,-8,]),'RBRACKET':([10,13,14,15,16,17,18,25,50,85,92,],[-1,24,-1,-14,-15,-16,-17,-13,-18,-27,-24,]),'IF':([10,14,16,17,18,50,85,92,],[20,20,-15,-16,-17,-18,-27,-24,]),'PRINT':([10,14,16,17,18,50,85,92,],[21,21,-15,-16,-17,-18,-27,-24,]),'COLON':([11,12,24,32,33,34,35,36,37,39,41,43,44,51,55,56,59,60,63,65,66,73,76,77,78,79,80,81,82,83,84,88,90,93,],[22,-7,-12,-6,-45,50,-1,-1,-1,-41,-44,-46,-47,-19,-23,-32,-35,-36,-39,-42,-43,87,-20,-21,-22,-33,-34,-37,-38,-40,-1,92,-26,-25,]),'COMA':([12,],[23,]),'EQUAL':([19,],[26,]),'LPAREN':([20,21,26,27,28,38,52,53,54,57,58,61,62,70,],[27,28,38,38,38,38,38,38,38,38,38,38,38,38,]),'INT':([22,87,],[30,30,]),'FLOAT':([22,87,],[31,31,]),'ELSE':([24,84,],[-12,89,]),'PLUS':([26,27,28,33,36,37,38,39,41,43,44,52,53,54,57,58,60,61,62,63,65,66,70,81,82,83,],[40,40,40,-45,57,-1,40,-41,-44,-46,-47,40,40,40,40,40,-36,40,40,-39,-42,-43,40,-37,-38,-40,]),'MINUS':([26,27,28,33,36,37,38,39,41,43,44,52,53,54,57,58,60,61,62,63,65,66,70,81,82,83,],[42,42,42,-45,58,-1,42,-41,-44,-46,-47,42,42,42,42,42,-36,42,42,-39,-42,-43,42,-37,-38,-40,]),'CTEINT':([26,27,28,38,40,42,52,53,54,57,58,61,62,70,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'CTEF':([26,27,28,38,40,42,52,53,54,57,58,61,62,70,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'CTESTRING':([28,70,],[48,48,]),'MULTIPLY':([33,37,39,41,43,44,65,66,83,],[-45,61,-41,-44,-46,-47,-42,-43,-40,]),'DIVIDE':([33,37,39,41,43,44,65,66,83,],[-45,62,-41,-44,-46,-47,-42,-43,-40,]),'GREATERT':([33,35,36,37,39,41,43,44,56,59,60,63,65,66,79,80,81,82,83,],[-45,52,-1,-1,-41,-44,-46,-47,-32,-35,-36,-39,-42,-43,-33,-34,-37,-38,-40,]),'LESST':([33,35,36,37,39,41,43,44,56,59,60,63,65,66,79,80,81,82,83,],[-45,53,-1,-1,-41,-44,-46,-47,-32,-35,-36,-39,-42,-43,-33,-34,-37,-38,-40,]),'DIFF':([33,35,36,37,39,41,43,44,56,59,60,63,65,66,79,80,81,82,83,],[-45,54,-1,-1,-41,-44,-46,-47,-32,-35,-36,-39,-42,-43,-33,-34,-37,-38,-40,]),'RPAREN':([33,35,36,37,39,41,43,44,45,46,47,48,51,55,56,59,60,63,64,65,66,69,71,72,76,77,78,79,80,81,82,83,86,],[-45,-1,-1,-1,-41,-44,-46,-47,67,68,-1,-1,-19,-23,-32,-35,-36,-39,83,-42,-43,-28,-31,-29,-20,-21,-22,-33,-34,-37,-38,-40,-30,]),'DOT':([33,35,36,37,39,41,43,44,47,48,51,55,56,59,60,63,65,66,76,77,78,79,80,81,82,83,],[-45,-1,-1,-1,-41,-44,-46,-47,70,70,-19,-23,-32,-35,-36,-39,-42,-43,-20,-21,-22,-33,-34,-37,-38,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'PROGRAMA_AUX':([4,],[5,]),'VARS':([4,],[6,]),'empty':([4,10,14,35,36,37,47,48,49,84,94,],[7,15,15,55,59,63,71,71,75,90,75,]),'BLOQUE':([5,67,89,],[9,84,93,]),'VARS_AUX':([8,23,49,94,],[11,32,73,73,]),'ESTATUTO_AUX':([10,14,],[13,25,]),'ESTATUTO':([10,14,],[14,14,]),'ASIGNACION':([10,14,],[16,16,]),'CONDICION':([10,14,],[17,17,]),'ESCRITURA':([10,14,],[18,18,]),'TIPO':([22,87,],[29,91,]),'EXPRESION':([26,27,28,38,54,70,],[34,45,47,64,78,47,]),'EXP':([26,27,28,38,52,53,54,57,58,70,],[35,35,35,35,76,77,35,79,80,35,]),'TERMINO':([26,27,28,38,52,53,54,57,58,61,62,70,],[36,36,36,36,36,36,36,36,36,81,82,36,]),'FACTOR':([26,27,28,38,52,53,54,57,58,61,62,70,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'FACTOR_AUX':([26,27,28,38,52,53,54,57,58,61,62,70,],[39,39,39,39,39,39,39,39,39,39,39,39,]),'VARCTE':([26,27,28,38,40,42,52,53,54,57,58,61,62,70,],[41,41,41,41,65,66,41,41,41,41,41,41,41,41,]),'ESCRITURA_AUX':([28,70,],[46,86,]),'EXPRESION_AUX':([35,],[51,]),'EXP_AUX':([36,],[56,]),'TERMINO_AUX':([37,],[60,]),'ESCRITURA_AUX2':([47,48,],[69,72,]),'VARS_AUX2':([49,94,],[74,95,]),'CONDICION_AUX':([84,],[88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',72),
  ('PROGRAMA -> PROGRAM ID SEMICOLON PROGRAMA_AUX BLOQUE','PROGRAMA',5,'p_PROGRAMA','lexer.py',77),
  ('PROGRAMA_AUX -> VARS','PROGRAMA_AUX',1,'p_PROGRAMA_AUX','lexer.py',82),
  ('PROGRAMA_AUX -> empty','PROGRAMA_AUX',1,'p_PROGRAMA_AUX','lexer.py',83),
  ('VARS -> VAR VARS_AUX COLON TIPO SEMICOLON VARS_AUX2','VARS',6,'p_VARS','lexer.py',88),
  ('VARS_AUX -> ID COMA VARS_AUX','VARS_AUX',3,'p_VARS_AUX','lexer.py',93),
  ('VARS_AUX -> ID','VARS_AUX',1,'p_VARS_AUX','lexer.py',94),
  ('VARS_AUX2 -> VARS_AUX COLON TIPO SEMICOLON VARS_AUX2','VARS_AUX2',5,'p_VARS_AUX2','lexer.py',99),
  ('VARS_AUX2 -> empty','VARS_AUX2',1,'p_VARS_AUX2','lexer.py',100),
  ('TIPO -> INT','TIPO',1,'p_TIPO','lexer.py',105),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','lexer.py',106),
  ('BLOQUE -> LBRACKET ESTATUTO_AUX RBRACKET','BLOQUE',3,'p_BLOQUE','lexer.py',111),
  ('ESTATUTO_AUX -> ESTATUTO ESTATUTO_AUX','ESTATUTO_AUX',2,'p_ESTATUTO_AUX','lexer.py',116),
  ('ESTATUTO_AUX -> empty','ESTATUTO_AUX',1,'p_ESTATUTO_AUX','lexer.py',117),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','lexer.py',122),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','lexer.py',123),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','lexer.py',124),
  ('ASIGNACION -> ID EQUAL EXPRESION COLON','ASIGNACION',4,'p_ASIGNACION','lexer.py',129),
  ('EXPRESION -> EXP EXPRESION_AUX','EXPRESION',2,'p_EXPRESION','lexer.py',134),
  ('EXPRESION_AUX -> GREATERT EXP','EXPRESION_AUX',2,'p_EXPRESION_AUX','lexer.py',139),
  ('EXPRESION_AUX -> LESST EXP','EXPRESION_AUX',2,'p_EXPRESION_AUX','lexer.py',140),
  ('EXPRESION_AUX -> DIFF EXPRESION','EXPRESION_AUX',2,'p_EXPRESION_AUX','lexer.py',141),
  ('EXPRESION_AUX -> empty','EXPRESION_AUX',1,'p_EXPRESION_AUX','lexer.py',142),
  ('CONDICION -> IF LPAREN EXPRESION RPAREN BLOQUE CONDICION_AUX COLON','CONDICION',7,'p_CONDICION','lexer.py',147),
  ('CONDICION_AUX -> ELSE BLOQUE','CONDICION_AUX',2,'p_CONDICION_AUX','lexer.py',152),
  ('CONDICION_AUX -> empty','CONDICION_AUX',1,'p_CONDICION_AUX','lexer.py',153),
  ('ESCRITURA -> PRINT LPAREN ESCRITURA_AUX RPAREN SEMICOLON','ESCRITURA',5,'p_ESCRITURA','lexer.py',158),
  ('ESCRITURA_AUX -> EXPRESION ESCRITURA_AUX2','ESCRITURA_AUX',2,'p_ESCRITURA_AUX','lexer.py',163),
  ('ESCRITURA_AUX -> CTESTRING ESCRITURA_AUX2','ESCRITURA_AUX',2,'p_ESCRITURA_AUX','lexer.py',164),
  ('ESCRITURA_AUX2 -> DOT ESCRITURA_AUX','ESCRITURA_AUX2',2,'p_ESCRITURA_AUX2','lexer.py',169),
  ('ESCRITURA_AUX2 -> empty','ESCRITURA_AUX2',1,'p_ESCRITURA_AUX2','lexer.py',170),
  ('EXP -> TERMINO EXP_AUX','EXP',2,'p_EXP','lexer.py',175),
  ('EXP_AUX -> PLUS EXP','EXP_AUX',2,'p_EXP_AUX','lexer.py',180),
  ('EXP_AUX -> MINUS EXP','EXP_AUX',2,'p_EXP_AUX','lexer.py',181),
  ('EXP_AUX -> empty','EXP_AUX',1,'p_EXP_AUX','lexer.py',182),
  ('TERMINO -> FACTOR TERMINO_AUX','TERMINO',2,'p_TERMINO','lexer.py',187),
  ('TERMINO_AUX -> MULTIPLY TERMINO','TERMINO_AUX',2,'p_TERMINO_AUX','lexer.py',192),
  ('TERMINO_AUX -> DIVIDE TERMINO','TERMINO_AUX',2,'p_TERMINO_AUX','lexer.py',193),
  ('TERMINO_AUX -> empty','TERMINO_AUX',1,'p_TERMINO_AUX','lexer.py',194),
  ('FACTOR -> LPAREN EXPRESION RPAREN','FACTOR',3,'p_FACTOR','lexer.py',199),
  ('FACTOR -> FACTOR_AUX','FACTOR',1,'p_FACTOR','lexer.py',200),
  ('FACTOR_AUX -> PLUS VARCTE','FACTOR_AUX',2,'p_FACTOR_AUX','lexer.py',205),
  ('FACTOR_AUX -> MINUS VARCTE','FACTOR_AUX',2,'p_FACTOR_AUX','lexer.py',206),
  ('FACTOR_AUX -> VARCTE','FACTOR_AUX',1,'p_FACTOR_AUX','lexer.py',207),
  ('VARCTE -> ID','VARCTE',1,'p_VARCTE','lexer.py',212),
  ('VARCTE -> CTEINT','VARCTE',1,'p_VARCTE','lexer.py',213),
  ('VARCTE -> CTEF','VARCTE',1,'p_VARCTE','lexer.py',214),
]
