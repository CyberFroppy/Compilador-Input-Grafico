
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaID COMMENT COLON SEMICOLON LBRACKET RBRACKET EQUAL DBEQUALS NOTEQUAL GREATERT LESST AND OR LPAREN RPAREN DOT COMA PLUS MINUS MULTIPLY DIVIDE CTESTRING CTEINT CTEF PROGRAM MAIN VAR INT FLOAT CHAR PRINT IF ELSE THEN TO WHILE DO FOR VOID MODULE RETURN WRITE READprograma : PROGRAM ID SEMICOLON vars module main\n                | PROGRAM ID SEMICOLON module main\n                | PROGRAM ID SEMICOLON vars main\n                | PROGRAM ID SEMICOLON mainmain : MAIN bloque_modulevars : VAR vars_auxvars_aux : ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux\n                | ID n_seen_var_name COLON tipo n_set_var_type SEMICOLONvars_func : ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func\n                 | ID n_seen_var_name COLON tipo n_set_var_typetipo : INT n_seen_type\n            | FLOAT n_seen_typebloque_module : LBRACKET estatuto_module_aux RBRACKET\n                     | LBRACKET RBRACKET estatuto_module_aux : estatuto_module estatuto_module_aux\n                           | estatuto_moduleestatuto_module : estatuto\n                       | varsbloque : LBRACKET estatuto_aux RBRACKET\n              | LBRACKET RBRACKETestatuto_aux : estatuto estatuto_aux\n                    | estatutoestatuto : asignacion SEMICOLON\n                | condicion SEMICOLON\n                | escritura SEMICOLON\n                | return SEMICOLON\n                | for SEMICOLON\n                | while SEMICOLON\n                | call_module SEMICOLONasignacion : ID EQUAL expresionexpresion : exp AND expresion\n                 | expexp : exp_aux OR exp\n           | exp_aux exp_aux : exp_aux2 GREATERT exp_aux2\n               | exp_aux2 LESST exp_aux2\n               | exp_aux2 NOTEQUAL exp_aux2\n               | exp_aux2 DBEQUALS exp_aux2\n               | exp_aux2exp_aux2 : term PLUS exp_aux2\n                | term MINUS exp_aux2\n                | termterm : factor MULTIPLY term\n            | factor DIVIDE term\n            | factorfactor : LPAREN expresion RPAREN\n              | CTEINT\n              | CTEF\n              | IDmodule : MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module\n              | MODULE tipo ID n_seen_func_name params bloque_module module\n              | MODULE VOID n_seen_type ID n_seen_func_name params bloque_module\n              | MODULE tipo ID n_seen_func_name params bloque_moduleparams : LPAREN vars_func RPAREN\n              | LPAREN RPARENcall_module : ID LPAREN expresion RPAREN \n                   | ID LPAREN RPARENreturn : RETURN expresionfor : FOR asignacion TO CTEINT LBRACKET estatuto RBRACKETwhile : WHILE LPAREN expresion RPAREN LBRACKET estatuto RBRACKETcondicion : IF LPAREN expresion RPAREN bloque ELSE bloque\n                 | IF LPAREN expresion RPAREN bloqueescritura : PRINT LPAREN escritura_aux RPARENescritura_aux : expresion COMA escritura_aux\n                     | CTESTRING COMA escritura_aux\n                     | expresion\n                     | CTESTRINGn_seen_type : n_seen_var_name : n_seen_func_name : n_set_var_type : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,12,13,20,22,29,49,],[0,-4,-3,-2,-5,-1,-14,-13,]),'ID':([2,8,14,16,17,18,19,21,24,26,27,30,31,32,43,44,51,52,53,54,55,56,57,58,59,60,61,68,74,78,86,87,88,89,90,91,92,93,94,95,108,109,123,129,132,133,134,140,150,],[3,15,-6,-68,25,-68,-68,40,47,-11,-12,40,-17,-18,71,73,-23,-24,-25,-26,-27,-28,-29,71,71,71,71,71,71,104,71,71,71,71,71,71,71,71,71,71,71,71,15,40,40,40,-7,40,104,]),'SEMICOLON':([3,18,19,26,27,33,34,35,36,37,38,39,62,63,64,65,66,67,69,70,71,75,79,81,99,105,107,110,111,112,113,114,115,116,117,118,119,120,128,139,144,145,147,148,],[4,-68,-68,-11,-12,51,52,53,54,55,56,57,-58,-32,-34,-39,-42,-45,-47,-48,-49,-71,-30,-57,123,-56,-63,-31,-33,-35,-36,-37,-38,-40,-41,-43,-44,-46,-62,-20,-61,-19,-59,-60,]),'VAR':([4,14,21,30,31,32,51,52,53,54,55,56,57,123,134,],[8,-6,8,8,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,-7,]),'MODULE':([4,5,14,29,49,101,123,124,134,],[9,9,-6,-14,-13,9,-8,9,-7,]),'MAIN':([4,5,6,11,14,29,49,101,123,124,125,134,135,],[10,10,10,10,-6,-14,-13,-53,-8,-52,-51,-7,-50,]),'VOID':([9,],[16,]),'INT':([9,46,136,],[18,18,18,]),'FLOAT':([9,46,136,],[19,19,19,]),'LBRACKET':([10,77,100,103,106,121,122,126,137,],[21,21,21,-55,129,132,133,-54,129,]),'IF':([14,21,30,31,32,51,52,53,54,55,56,57,123,129,132,133,134,140,],[-6,41,41,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,41,41,41,-7,41,]),'PRINT':([14,21,30,31,32,51,52,53,54,55,56,57,123,129,132,133,134,140,],[-6,42,42,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,42,42,42,-7,42,]),'RETURN':([14,21,30,31,32,51,52,53,54,55,56,57,123,129,132,133,134,140,],[-6,43,43,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,43,43,43,-7,43,]),'FOR':([14,21,30,31,32,51,52,53,54,55,56,57,123,129,132,133,134,140,],[-6,44,44,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,44,44,44,-7,44,]),'WHILE':([14,21,30,31,32,51,52,53,54,55,56,57,123,129,132,133,134,140,],[-6,45,45,-17,-18,-23,-24,-25,-26,-27,-28,-29,-8,45,45,45,-7,45,]),'RBRACKET':([14,21,28,30,31,32,50,51,52,53,54,55,56,57,123,129,134,138,140,141,142,146,],[-6,29,49,-16,-17,-18,-15,-23,-24,-25,-26,-27,-28,-29,-8,139,-7,145,-22,147,148,-21,]),'COLON':([15,23,104,127,],[-69,46,-69,136,]),'COMA':([18,19,26,27,63,64,65,66,67,69,70,71,84,85,110,111,112,113,114,115,116,117,118,119,120,143,149,],[-68,-68,-11,-12,-32,-34,-39,-42,-45,-47,-48,-49,108,109,-31,-33,-35,-36,-37,-38,-40,-41,-43,-44,-46,-71,150,]),'RPAREN':([18,19,26,27,59,63,64,65,66,67,69,70,71,78,80,82,83,84,85,96,98,102,110,111,112,113,114,115,116,117,118,119,120,130,131,143,149,151,],[-68,-68,-11,-12,81,-32,-34,-39,-42,-45,-47,-48,-49,103,105,106,107,-66,-67,120,122,126,-31,-33,-35,-36,-37,-38,-40,-41,-43,-44,-46,-64,-65,-71,-10,-9,]),'LPAREN':([25,40,41,42,43,45,47,48,58,59,60,61,68,74,76,86,87,88,89,90,91,92,93,94,95,108,109,],[-70,59,60,61,68,74,-70,78,68,68,68,68,68,68,78,68,68,68,68,68,68,68,68,68,68,68,68,]),'EQUAL':([40,73,],[58,58,]),'CTEINT':([43,58,59,60,61,68,74,86,87,88,89,90,91,92,93,94,95,97,108,109,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,121,69,69,]),'CTEF':([43,58,59,60,61,68,74,86,87,88,89,90,91,92,93,94,95,108,109,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'CTESTRING':([61,108,109,],[85,85,85,]),'AND':([63,64,65,66,67,69,70,71,111,112,113,114,115,116,117,118,119,120,],[86,-34,-39,-42,-45,-47,-48,-49,-33,-35,-36,-37,-38,-40,-41,-43,-44,-46,]),'TO':([63,64,65,66,67,69,70,71,72,79,110,111,112,113,114,115,116,117,118,119,120,],[-32,-34,-39,-42,-45,-47,-48,-49,97,-30,-31,-33,-35,-36,-37,-38,-40,-41,-43,-44,-46,]),'OR':([64,65,66,67,69,70,71,112,113,114,115,116,117,118,119,120,],[87,-39,-42,-45,-47,-48,-49,-35,-36,-37,-38,-40,-41,-43,-44,-46,]),'GREATERT':([65,66,67,69,70,71,116,117,118,119,120,],[88,-42,-45,-47,-48,-49,-40,-41,-43,-44,-46,]),'LESST':([65,66,67,69,70,71,116,117,118,119,120,],[89,-42,-45,-47,-48,-49,-40,-41,-43,-44,-46,]),'NOTEQUAL':([65,66,67,69,70,71,116,117,118,119,120,],[90,-42,-45,-47,-48,-49,-40,-41,-43,-44,-46,]),'DBEQUALS':([65,66,67,69,70,71,116,117,118,119,120,],[91,-42,-45,-47,-48,-49,-40,-41,-43,-44,-46,]),'PLUS':([66,67,69,70,71,118,119,120,],[92,-45,-47,-48,-49,-43,-44,-46,]),'MINUS':([66,67,69,70,71,118,119,120,],[93,-45,-47,-48,-49,-43,-44,-46,]),'MULTIPLY':([67,69,70,71,120,],[94,-47,-48,-49,-46,]),'DIVIDE':([67,69,70,71,120,],[95,-47,-48,-49,-46,]),'ELSE':([128,139,145,],[137,-20,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([4,21,30,],[5,32,32,]),'module':([4,5,101,124,],[6,11,125,135,]),'main':([4,5,6,11,],[7,12,13,22,]),'vars_aux':([8,123,],[14,134,]),'tipo':([9,46,136,],[17,75,143,]),'bloque_module':([10,77,100,],[20,101,124,]),'n_seen_var_name':([15,104,],[23,127,]),'n_seen_type':([16,18,19,],[24,26,27,]),'estatuto_module_aux':([21,30,],[28,50,]),'estatuto_module':([21,30,],[30,30,]),'estatuto':([21,30,129,132,133,140,],[31,31,140,141,142,140,]),'asignacion':([21,30,44,129,132,133,140,],[33,33,72,33,33,33,33,]),'condicion':([21,30,129,132,133,140,],[34,34,34,34,34,34,]),'escritura':([21,30,129,132,133,140,],[35,35,35,35,35,35,]),'return':([21,30,129,132,133,140,],[36,36,36,36,36,36,]),'for':([21,30,129,132,133,140,],[37,37,37,37,37,37,]),'while':([21,30,129,132,133,140,],[38,38,38,38,38,38,]),'call_module':([21,30,129,132,133,140,],[39,39,39,39,39,39,]),'n_seen_func_name':([25,47,],[48,76,]),'expresion':([43,58,59,60,61,68,74,86,108,109,],[62,79,80,82,84,96,98,110,84,84,]),'exp':([43,58,59,60,61,68,74,86,87,108,109,],[63,63,63,63,63,63,63,63,111,63,63,]),'exp_aux':([43,58,59,60,61,68,74,86,87,108,109,],[64,64,64,64,64,64,64,64,64,64,64,]),'exp_aux2':([43,58,59,60,61,68,74,86,87,88,89,90,91,92,93,108,109,],[65,65,65,65,65,65,65,65,65,112,113,114,115,116,117,65,65,]),'term':([43,58,59,60,61,68,74,86,87,88,89,90,91,92,93,94,95,108,109,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,118,119,66,66,]),'factor':([43,58,59,60,61,68,74,86,87,88,89,90,91,92,93,94,95,108,109,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'params':([48,76,],[77,100,]),'escritura_aux':([61,108,109,],[83,130,131,]),'n_set_var_type':([75,143,],[99,149,]),'vars_func':([78,150,],[102,151,]),'bloque':([106,137,],[128,144,]),'estatuto_aux':([129,140,],[138,146,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON vars module main','programa',6,'p_programa','lexerparser.py',130),
  ('programa -> PROGRAM ID SEMICOLON module main','programa',5,'p_programa','lexerparser.py',131),
  ('programa -> PROGRAM ID SEMICOLON vars main','programa',5,'p_programa','lexerparser.py',132),
  ('programa -> PROGRAM ID SEMICOLON main','programa',4,'p_programa','lexerparser.py',133),
  ('main -> MAIN bloque_module','main',2,'p_main','lexerparser.py',138),
  ('vars -> VAR vars_aux','vars',2,'p_vars','lexerparser.py',142),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux','vars_aux',7,'p_vars_aux','lexerparser.py',146),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON','vars_aux',6,'p_vars_aux','lexerparser.py',147),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func','vars_func',7,'p_vars_func','lexerparser.py',150),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type','vars_func',5,'p_vars_func','lexerparser.py',151),
  ('tipo -> INT n_seen_type','tipo',2,'p_tipo','lexerparser.py',154),
  ('tipo -> FLOAT n_seen_type','tipo',2,'p_tipo','lexerparser.py',155),
  ('bloque_module -> LBRACKET estatuto_module_aux RBRACKET','bloque_module',3,'p_bloque_module','lexerparser.py',159),
  ('bloque_module -> LBRACKET RBRACKET','bloque_module',2,'p_bloque_module','lexerparser.py',160),
  ('estatuto_module_aux -> estatuto_module estatuto_module_aux','estatuto_module_aux',2,'p_estatuto_module_aux','lexerparser.py',164),
  ('estatuto_module_aux -> estatuto_module','estatuto_module_aux',1,'p_estatuto_module_aux','lexerparser.py',165),
  ('estatuto_module -> estatuto','estatuto_module',1,'p_estatuto_module','lexerparser.py',169),
  ('estatuto_module -> vars','estatuto_module',1,'p_estatuto_module','lexerparser.py',170),
  ('bloque -> LBRACKET estatuto_aux RBRACKET','bloque',3,'p_bloque','lexerparser.py',174),
  ('bloque -> LBRACKET RBRACKET','bloque',2,'p_bloque','lexerparser.py',175),
  ('estatuto_aux -> estatuto estatuto_aux','estatuto_aux',2,'p_estatuto_aux','lexerparser.py',179),
  ('estatuto_aux -> estatuto','estatuto_aux',1,'p_estatuto_aux','lexerparser.py',180),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',184),
  ('estatuto -> condicion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',185),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',186),
  ('estatuto -> return SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',187),
  ('estatuto -> for SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',188),
  ('estatuto -> while SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',189),
  ('estatuto -> call_module SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',190),
  ('asignacion -> ID EQUAL expresion','asignacion',3,'p_asignacion','lexerparser.py',194),
  ('expresion -> exp AND expresion','expresion',3,'p_expresion','lexerparser.py',198),
  ('expresion -> exp','expresion',1,'p_expresion','lexerparser.py',199),
  ('exp -> exp_aux OR exp','exp',3,'p_exp','lexerparser.py',203),
  ('exp -> exp_aux','exp',1,'p_exp','lexerparser.py',204),
  ('exp_aux -> exp_aux2 GREATERT exp_aux2','exp_aux',3,'p_exp_aux','lexerparser.py',208),
  ('exp_aux -> exp_aux2 LESST exp_aux2','exp_aux',3,'p_exp_aux','lexerparser.py',209),
  ('exp_aux -> exp_aux2 NOTEQUAL exp_aux2','exp_aux',3,'p_exp_aux','lexerparser.py',210),
  ('exp_aux -> exp_aux2 DBEQUALS exp_aux2','exp_aux',3,'p_exp_aux','lexerparser.py',211),
  ('exp_aux -> exp_aux2','exp_aux',1,'p_exp_aux','lexerparser.py',212),
  ('exp_aux2 -> term PLUS exp_aux2','exp_aux2',3,'p_exp_aux2','lexerparser.py',216),
  ('exp_aux2 -> term MINUS exp_aux2','exp_aux2',3,'p_exp_aux2','lexerparser.py',217),
  ('exp_aux2 -> term','exp_aux2',1,'p_exp_aux2','lexerparser.py',218),
  ('term -> factor MULTIPLY term','term',3,'p_term','lexerparser.py',222),
  ('term -> factor DIVIDE term','term',3,'p_term','lexerparser.py',223),
  ('term -> factor','term',1,'p_term','lexerparser.py',224),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','lexerparser.py',228),
  ('factor -> CTEINT','factor',1,'p_factor','lexerparser.py',229),
  ('factor -> CTEF','factor',1,'p_factor','lexerparser.py',230),
  ('factor -> ID','factor',1,'p_factor','lexerparser.py',231),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module','module',8,'p_module','lexerparser.py',235),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module module','module',7,'p_module','lexerparser.py',236),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module','module',7,'p_module','lexerparser.py',237),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module','module',6,'p_module','lexerparser.py',238),
  ('params -> LPAREN vars_func RPAREN','params',3,'p_params','lexerparser.py',241),
  ('params -> LPAREN RPAREN','params',2,'p_params','lexerparser.py',242),
  ('call_module -> ID LPAREN expresion RPAREN','call_module',4,'p_call_module','lexerparser.py',245),
  ('call_module -> ID LPAREN RPAREN','call_module',3,'p_call_module','lexerparser.py',246),
  ('return -> RETURN expresion','return',2,'p_return','lexerparser.py',249),
  ('for -> FOR asignacion TO CTEINT LBRACKET estatuto RBRACKET','for',7,'p_for','lexerparser.py',253),
  ('while -> WHILE LPAREN expresion RPAREN LBRACKET estatuto RBRACKET','while',7,'p_while','lexerparser.py',257),
  ('condicion -> IF LPAREN expresion RPAREN bloque ELSE bloque','condicion',7,'p_condicion','lexerparser.py',261),
  ('condicion -> IF LPAREN expresion RPAREN bloque','condicion',5,'p_condicion','lexerparser.py',262),
  ('escritura -> PRINT LPAREN escritura_aux RPAREN','escritura',4,'p_escritura','lexerparser.py',266),
  ('escritura_aux -> expresion COMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexerparser.py',270),
  ('escritura_aux -> CTESTRING COMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexerparser.py',271),
  ('escritura_aux -> expresion','escritura_aux',1,'p_escritura_aux','lexerparser.py',272),
  ('escritura_aux -> CTESTRING','escritura_aux',1,'p_escritura_aux','lexerparser.py',273),
  ('n_seen_type -> <empty>','n_seen_type',0,'p_n_seen_type','lexerparser.py',292),
  ('n_seen_var_name -> <empty>','n_seen_var_name',0,'p_n_seen_var_name','lexerparser.py',301),
  ('n_seen_func_name -> <empty>','n_seen_func_name',0,'p_n_seen_func_name','lexerparser.py',317),
  ('n_set_var_type -> <empty>','n_set_var_type',0,'p_n_set_var_type','lexerparser.py',327),
]
