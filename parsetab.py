
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaCOLON SEMICOLON LBRACKET RBRACKET EQUAL DBEQUALS NOTEQUAL GREATERT LESST GREATEREQUAL LESSEQUAL AND OR LPAREN RPAREN DOT COMA PLUS MINUS MULTIPLY DIVIDE CTESTRING CTEINT CTEF CTEC TRANSPUESTA DETERMINANTE INVERSA ID COMMENT PROGRAM MAIN VAR INT FLOAT CHAR PRINT IF ELSE THEN TO WHILE DO FOR VOID MODULE RETURN WRITE READprograma : PROGRAM ID SEMICOLON vars module main\n                | PROGRAM ID SEMICOLON module main\n                | PROGRAM ID SEMICOLON vars main\n                | PROGRAM ID SEMICOLON mainmain : MAIN n_seen_func_name bloque_modulevars : VAR vars_auxvars_aux : ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux\n                | ID n_seen_var_name COLON tipo n_set_var_type DOTvars_func : ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func\n                 | ID n_seen_var_name COLON tipo n_set_var_typetipo : INT n_seen_type\n            | FLOAT n_seen_type\n            | CHAR n_seen_typebloque_module : LBRACKET vars estatuto_aux RBRACKET\n                     | LBRACKET vars RBRACKET\n                     | LBRACKET estatuto_aux RBRACKET\n                     | LBRACKET RBRACKET bloque : LBRACKET estatuto_aux RBRACKET\n              | LBRACKET RBRACKETestatuto_aux : estatuto estatuto_aux\n                    | estatutoestatuto : asignacion SEMICOLON\n                | condicion SEMICOLON\n                | escritura SEMICOLON\n                | return SEMICOLON\n                | for SEMICOLON\n                | while SEMICOLON\n                | call_module SEMICOLONasignacion : ID n_seen_factor_id EQUAL n_add_operator expresion n_assignexpresion : exp n_gen_and AND n_add_operator expresion\n                 | exp n_gen_and exp : exp_aux n_gen_or OR n_add_operator exp\n           | exp_aux n_gen_or exp_aux : exp_aux2 n_gen_relational GREATERT n_add_operator exp_aux\n               | exp_aux2 n_gen_relational LESST n_add_operator exp_aux\n               | exp_aux2 n_gen_relational NOTEQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational DBEQUALS n_add_operator exp_aux\n               | exp_aux2 n_gen_relational GREATEREQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational LESSEQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational exp_aux2 : term n_gen_term PLUS n_add_operator exp_aux2 \n                | term n_gen_term MINUS n_add_operator exp_aux2\n                | term n_gen_termterm : factor n_gen_factor MULTIPLY n_add_operator term \n            | factor n_gen_factor DIVIDE n_add_operator term \n            | factor n_gen_factorfactor : LPAREN n_push_fake_bottom expresion RPAREN n_pop_fake_bottom\n              | CTEINT n_seen_factor_int\n              | CTEF n_seen_factor_float\n              | CTEC n_seen_factor_char\n              | ID n_seen_factor_idmodule : MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module\n              | MODULE tipo ID n_seen_func_name params bloque_module module\n              | MODULE VOID n_seen_type ID n_seen_func_name params bloque_module\n              | MODULE tipo ID n_seen_func_name params bloque_moduleparams : LPAREN vars_func RPAREN\n              | LPAREN RPARENcall_module : ID LPAREN expresion RPAREN \n                   | ID LPAREN RPARENreturn : RETURN expresionfor : FOR asignacion TO CTEINT bloquewhile : WHILE  LPAREN expresion RPAREN  bloque condicion : IF LPAREN expresion RPAREN n_check_exp bloque ELSE n_else bloque n_fill_end\n                 | IF LPAREN expresion RPAREN n_check_exp bloque n_fill_endescritura : PRINT LPAREN escritura_aux RPARENescritura_aux : expresion COMA escritura_aux\n                     | CTESTRING COMA escritura_aux\n                     | expresion\n                     | CTESTRINGn_seen_type : n_seen_var_name : n_seen_func_name : n_set_var_type : n_seen_factor_id : n_seen_factor_int : n_seen_factor_float : n_seen_factor_char : n_assign : n_add_operator : n_gen_term : n_gen_factor : n_gen_relational : n_gen_or : n_gen_and : n_push_fake_bottom : n_pop_fake_bottom : n_check_exp : n_fill_end : n_else : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,12,13,22,29,36,56,57,90,],[0,-4,-3,-2,-1,-5,-17,-15,-16,-14,]),'ID':([2,8,14,16,17,18,19,20,24,26,27,28,30,34,37,48,49,54,59,60,61,62,63,64,65,67,68,69,76,83,91,103,110,111,116,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,144,145,146,147,148,149,150,151,152,153,154,155,158,182,],[3,15,-6,-70,25,-70,-70,-70,32,-11,-12,-13,45,45,45,80,82,89,-22,-23,-24,-25,-26,-27,-28,80,80,80,-85,80,-79,80,15,-8,80,80,80,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-7,80,80,80,80,80,80,80,80,80,80,80,80,45,89,]),'SEMICOLON':([3,18,19,20,26,27,28,38,39,40,41,42,43,44,51,70,71,72,73,74,75,77,78,79,80,84,93,98,99,100,101,102,104,105,106,107,117,119,140,156,157,159,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,177,180,181,185,186,],[4,-70,-70,-70,-11,-12,-13,59,60,61,62,63,64,65,-73,-60,-84,-83,-82,-80,-81,-75,-76,-77,-74,110,-59,-31,-33,-40,-43,-46,-48,-49,-50,-51,-58,-65,-78,-86,-61,-62,-29,-88,-30,-32,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,-19,-64,-18,-88,-63,]),'VAR':([4,30,],[8,8,]),'MODULE':([4,5,14,36,56,57,86,90,111,112,137,],[9,9,-6,-17,-15,-16,9,-14,-8,9,-7,]),'MAIN':([4,5,6,11,14,36,56,57,86,90,111,112,113,137,138,],[10,10,10,10,-6,-17,-15,-16,-55,-14,-8,-54,-53,-7,-52,]),'VOID':([9,],[16,]),'INT':([9,31,139,],[18,18,18,]),'FLOAT':([9,31,139,],[19,19,19,]),'CHAR':([9,31,139,],[20,20,20,]),'LBRACKET':([10,21,53,85,88,114,118,135,136,141,179,183,],[-72,30,30,30,-57,-56,-87,158,158,158,-89,158,]),'RBRACKET':([14,30,34,35,37,55,58,59,60,61,62,63,64,65,111,137,158,176,],[-6,36,56,57,-21,90,-20,-22,-23,-24,-25,-26,-27,-28,-8,-7,177,181,]),'IF':([14,30,34,37,59,60,61,62,63,64,65,111,137,158,],[-6,46,46,46,-22,-23,-24,-25,-26,-27,-28,-8,-7,46,]),'PRINT':([14,30,34,37,59,60,61,62,63,64,65,111,137,158,],[-6,47,47,47,-22,-23,-24,-25,-26,-27,-28,-8,-7,47,]),'RETURN':([14,30,34,37,59,60,61,62,63,64,65,111,137,158,],[-6,48,48,48,-22,-23,-24,-25,-26,-27,-28,-8,-7,48,]),'FOR':([14,30,34,37,59,60,61,62,63,64,65,111,137,158,],[-6,49,49,49,-22,-23,-24,-25,-26,-27,-28,-8,-7,49,]),'WHILE':([14,30,34,37,59,60,61,62,63,64,65,111,137,158,],[-6,50,50,50,-22,-23,-24,-25,-26,-27,-28,-8,-7,50,]),'COLON':([15,23,89,115,],[-71,31,-71,139,]),'DOT':([18,19,20,26,27,28,51,84,],[-70,-70,-70,-11,-12,-13,-73,111,]),'COMA':([18,19,20,26,27,28,71,72,73,74,75,77,78,79,80,96,97,98,99,100,101,102,104,105,106,107,156,160,163,164,165,166,167,168,169,170,171,172,173,174,175,178,],[-70,-70,-70,-11,-12,-13,-84,-83,-82,-80,-81,-75,-76,-77,-74,120,121,-31,-33,-40,-43,-46,-48,-49,-50,-51,-86,-73,-30,-32,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,182,]),'RPAREN':([18,19,20,26,27,28,54,67,71,72,73,74,75,77,78,79,80,87,92,94,95,96,97,98,99,100,101,102,104,105,106,107,109,134,142,143,156,160,163,164,165,166,167,168,169,170,171,172,173,174,175,178,184,],[-70,-70,-70,-11,-12,-13,88,93,-84,-83,-82,-80,-81,-75,-76,-77,-74,114,117,118,119,-68,-69,-31,-33,-40,-43,-46,-48,-49,-50,-51,136,156,-66,-67,-86,-73,-30,-32,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,-10,-9,]),'LPAREN':([25,32,33,45,46,47,48,50,52,67,68,69,76,83,91,103,116,120,121,122,123,124,125,126,127,128,129,130,131,132,133,144,145,146,147,148,149,150,151,152,153,154,155,],[-72,-72,54,67,68,69,76,83,54,76,76,76,-85,76,-79,76,76,76,76,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,76,76,76,76,76,76,76,76,76,76,76,76,]),'EQUAL':([45,66,82,],[-74,91,-74,]),'CTEINT':([48,67,68,69,76,83,91,103,108,116,120,121,122,123,124,125,126,127,128,129,130,131,132,133,144,145,146,147,148,149,150,151,152,153,154,155,],[77,77,77,77,-85,77,-79,77,135,77,77,77,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,77,77,77,77,77,77,77,77,77,77,77,77,]),'CTEF':([48,67,68,69,76,83,91,103,116,120,121,122,123,124,125,126,127,128,129,130,131,132,133,144,145,146,147,148,149,150,151,152,153,154,155,],[78,78,78,78,-85,78,-79,78,78,78,78,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,78,78,78,78,78,78,78,78,78,78,78,78,]),'CTEC':([48,67,68,69,76,83,91,103,116,120,121,122,123,124,125,126,127,128,129,130,131,132,133,144,145,146,147,148,149,150,151,152,153,154,155,],[79,79,79,79,-85,79,-79,79,79,79,79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,-79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CTESTRING':([69,120,121,],[97,97,97,]),'AND':([71,72,73,74,75,77,78,79,80,98,99,100,101,102,104,105,106,107,156,164,165,166,167,168,169,170,171,172,173,174,175,],[-84,-83,-82,-80,-81,-75,-76,-77,-74,122,-33,-40,-43,-46,-48,-49,-50,-51,-86,-32,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,]),'TO':([71,72,73,74,75,77,78,79,80,81,98,99,100,101,102,104,105,106,107,140,156,161,163,164,165,166,167,168,169,170,171,172,173,174,175,],[-84,-83,-82,-80,-81,-75,-76,-77,-74,108,-31,-33,-40,-43,-46,-48,-49,-50,-51,-78,-86,-29,-30,-32,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,]),'OR':([72,73,74,75,77,78,79,80,99,100,101,102,104,105,106,107,156,165,166,167,168,169,170,171,172,173,174,175,],[-83,-82,-80,-81,-75,-76,-77,-74,123,-40,-43,-46,-48,-49,-50,-51,-86,-34,-35,-36,-37,-38,-39,-41,-42,-44,-45,-47,]),'GREATERT':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,124,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'LESST':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,125,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'NOTEQUAL':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,126,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'DBEQUALS':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,127,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'GREATEREQUAL':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,128,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'LESSEQUAL':([73,74,75,77,78,79,80,100,101,102,104,105,106,107,156,171,172,173,174,175,],[-82,-80,-81,-75,-76,-77,-74,129,-43,-46,-48,-49,-50,-51,-86,-41,-42,-44,-45,-47,]),'PLUS':([74,75,77,78,79,80,101,102,104,105,106,107,156,173,174,175,],[-80,-81,-75,-76,-77,-74,130,-46,-48,-49,-50,-51,-86,-44,-45,-47,]),'MINUS':([74,75,77,78,79,80,101,102,104,105,106,107,156,173,174,175,],[-80,-81,-75,-76,-77,-74,131,-46,-48,-49,-50,-51,-86,-44,-45,-47,]),'MULTIPLY':([75,77,78,79,80,102,104,105,106,107,156,175,],[-81,-75,-76,-77,-74,132,-48,-49,-50,-51,-86,-47,]),'DIVIDE':([75,77,78,79,80,102,104,105,106,107,156,175,],[-81,-75,-76,-77,-74,133,-48,-49,-50,-51,-86,-47,]),'ELSE':([162,177,181,],[179,-19,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([4,30,],[5,34,]),'module':([4,5,86,112,],[6,11,113,138,]),'main':([4,5,6,11,],[7,12,13,22,]),'vars_aux':([8,110,],[14,137,]),'tipo':([9,31,139,],[17,51,160,]),'n_seen_func_name':([10,25,32,],[21,33,52,]),'n_seen_var_name':([15,89,],[23,115,]),'n_seen_type':([16,18,19,20,],[24,26,27,28,]),'bloque_module':([21,53,85,],[29,86,112,]),'estatuto_aux':([30,34,37,158,],[35,55,58,176,]),'estatuto':([30,34,37,158,],[37,37,37,37,]),'asignacion':([30,34,37,49,158,],[38,38,38,81,38,]),'condicion':([30,34,37,158,],[39,39,39,39,]),'escritura':([30,34,37,158,],[40,40,40,40,]),'return':([30,34,37,158,],[41,41,41,41,]),'for':([30,34,37,158,],[42,42,42,42,]),'while':([30,34,37,158,],[43,43,43,43,]),'call_module':([30,34,37,158,],[44,44,44,44,]),'params':([33,52,],[53,85,]),'n_seen_factor_id':([45,80,82,],[66,107,66,]),'expresion':([48,67,68,69,83,103,116,120,121,144,],[70,92,94,96,109,134,140,96,96,163,]),'exp':([48,67,68,69,83,103,116,120,121,144,145,],[71,71,71,71,71,71,71,71,71,71,164,]),'exp_aux':([48,67,68,69,83,103,116,120,121,144,145,146,147,148,149,150,151,],[72,72,72,72,72,72,72,72,72,72,72,165,166,167,168,169,170,]),'exp_aux2':([48,67,68,69,83,103,116,120,121,144,145,146,147,148,149,150,151,152,153,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,171,172,]),'term':([48,67,68,69,83,103,116,120,121,144,145,146,147,148,149,150,151,152,153,154,155,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,173,174,]),'factor':([48,67,68,69,83,103,116,120,121,144,145,146,147,148,149,150,151,152,153,154,155,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'n_set_var_type':([51,160,],[84,178,]),'vars_func':([54,182,],[87,184,]),'escritura_aux':([69,120,121,],[95,142,143,]),'n_gen_and':([71,],[98,]),'n_gen_or':([72,],[99,]),'n_gen_relational':([73,],[100,]),'n_gen_term':([74,],[101,]),'n_gen_factor':([75,],[102,]),'n_push_fake_bottom':([76,],[103,]),'n_seen_factor_int':([77,],[104,]),'n_seen_factor_float':([78,],[105,]),'n_seen_factor_char':([79,],[106,]),'n_add_operator':([91,122,123,124,125,126,127,128,129,130,131,132,133,],[116,144,145,146,147,148,149,150,151,152,153,154,155,]),'n_check_exp':([118,],[141,]),'bloque':([135,136,141,183,],[157,159,162,185,]),'n_assign':([140,],[161,]),'n_pop_fake_bottom':([156,],[175,]),'n_fill_end':([162,185,],[180,186,]),'n_else':([179,],[183,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON vars module main','programa',6,'p_programa','lexerparser.py',431),
  ('programa -> PROGRAM ID SEMICOLON module main','programa',5,'p_programa','lexerparser.py',432),
  ('programa -> PROGRAM ID SEMICOLON vars main','programa',5,'p_programa','lexerparser.py',433),
  ('programa -> PROGRAM ID SEMICOLON main','programa',4,'p_programa','lexerparser.py',434),
  ('main -> MAIN n_seen_func_name bloque_module','main',3,'p_main','lexerparser.py',439),
  ('vars -> VAR vars_aux','vars',2,'p_vars','lexerparser.py',443),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux','vars_aux',7,'p_vars_aux','lexerparser.py',447),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type DOT','vars_aux',6,'p_vars_aux','lexerparser.py',448),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func','vars_func',7,'p_vars_func','lexerparser.py',451),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type','vars_func',5,'p_vars_func','lexerparser.py',452),
  ('tipo -> INT n_seen_type','tipo',2,'p_tipo','lexerparser.py',455),
  ('tipo -> FLOAT n_seen_type','tipo',2,'p_tipo','lexerparser.py',456),
  ('tipo -> CHAR n_seen_type','tipo',2,'p_tipo','lexerparser.py',457),
  ('bloque_module -> LBRACKET vars estatuto_aux RBRACKET','bloque_module',4,'p_bloque_module','lexerparser.py',461),
  ('bloque_module -> LBRACKET vars RBRACKET','bloque_module',3,'p_bloque_module','lexerparser.py',462),
  ('bloque_module -> LBRACKET estatuto_aux RBRACKET','bloque_module',3,'p_bloque_module','lexerparser.py',463),
  ('bloque_module -> LBRACKET RBRACKET','bloque_module',2,'p_bloque_module','lexerparser.py',464),
  ('bloque -> LBRACKET estatuto_aux RBRACKET','bloque',3,'p_bloque','lexerparser.py',468),
  ('bloque -> LBRACKET RBRACKET','bloque',2,'p_bloque','lexerparser.py',469),
  ('estatuto_aux -> estatuto estatuto_aux','estatuto_aux',2,'p_estatuto_aux','lexerparser.py',473),
  ('estatuto_aux -> estatuto','estatuto_aux',1,'p_estatuto_aux','lexerparser.py',474),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',478),
  ('estatuto -> condicion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',479),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',480),
  ('estatuto -> return SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',481),
  ('estatuto -> for SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',482),
  ('estatuto -> while SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',483),
  ('estatuto -> call_module SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',484),
  ('asignacion -> ID n_seen_factor_id EQUAL n_add_operator expresion n_assign','asignacion',6,'p_asignacion','lexerparser.py',488),
  ('expresion -> exp n_gen_and AND n_add_operator expresion','expresion',5,'p_expresion','lexerparser.py',492),
  ('expresion -> exp n_gen_and','expresion',2,'p_expresion','lexerparser.py',493),
  ('exp -> exp_aux n_gen_or OR n_add_operator exp','exp',5,'p_exp','lexerparser.py',497),
  ('exp -> exp_aux n_gen_or','exp',2,'p_exp','lexerparser.py',498),
  ('exp_aux -> exp_aux2 n_gen_relational GREATERT n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',502),
  ('exp_aux -> exp_aux2 n_gen_relational LESST n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',503),
  ('exp_aux -> exp_aux2 n_gen_relational NOTEQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',504),
  ('exp_aux -> exp_aux2 n_gen_relational DBEQUALS n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',505),
  ('exp_aux -> exp_aux2 n_gen_relational GREATEREQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',506),
  ('exp_aux -> exp_aux2 n_gen_relational LESSEQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',507),
  ('exp_aux -> exp_aux2 n_gen_relational','exp_aux',2,'p_exp_aux','lexerparser.py',508),
  ('exp_aux2 -> term n_gen_term PLUS n_add_operator exp_aux2','exp_aux2',5,'p_exp_aux2','lexerparser.py',512),
  ('exp_aux2 -> term n_gen_term MINUS n_add_operator exp_aux2','exp_aux2',5,'p_exp_aux2','lexerparser.py',513),
  ('exp_aux2 -> term n_gen_term','exp_aux2',2,'p_exp_aux2','lexerparser.py',514),
  ('term -> factor n_gen_factor MULTIPLY n_add_operator term','term',5,'p_term','lexerparser.py',518),
  ('term -> factor n_gen_factor DIVIDE n_add_operator term','term',5,'p_term','lexerparser.py',519),
  ('term -> factor n_gen_factor','term',2,'p_term','lexerparser.py',520),
  ('factor -> LPAREN n_push_fake_bottom expresion RPAREN n_pop_fake_bottom','factor',5,'p_factor','lexerparser.py',524),
  ('factor -> CTEINT n_seen_factor_int','factor',2,'p_factor','lexerparser.py',525),
  ('factor -> CTEF n_seen_factor_float','factor',2,'p_factor','lexerparser.py',526),
  ('factor -> CTEC n_seen_factor_char','factor',2,'p_factor','lexerparser.py',527),
  ('factor -> ID n_seen_factor_id','factor',2,'p_factor','lexerparser.py',528),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module','module',8,'p_module','lexerparser.py',533),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module module','module',7,'p_module','lexerparser.py',534),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module','module',7,'p_module','lexerparser.py',535),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module','module',6,'p_module','lexerparser.py',536),
  ('params -> LPAREN vars_func RPAREN','params',3,'p_params','lexerparser.py',539),
  ('params -> LPAREN RPAREN','params',2,'p_params','lexerparser.py',540),
  ('call_module -> ID LPAREN expresion RPAREN','call_module',4,'p_call_module','lexerparser.py',543),
  ('call_module -> ID LPAREN RPAREN','call_module',3,'p_call_module','lexerparser.py',544),
  ('return -> RETURN expresion','return',2,'p_return','lexerparser.py',547),
  ('for -> FOR asignacion TO CTEINT bloque','for',5,'p_for','lexerparser.py',551),
  ('while -> WHILE LPAREN expresion RPAREN bloque','while',5,'p_while','lexerparser.py',555),
  ('condicion -> IF LPAREN expresion RPAREN n_check_exp bloque ELSE n_else bloque n_fill_end','condicion',10,'p_condicion','lexerparser.py',559),
  ('condicion -> IF LPAREN expresion RPAREN n_check_exp bloque n_fill_end','condicion',7,'p_condicion','lexerparser.py',560),
  ('escritura -> PRINT LPAREN escritura_aux RPAREN','escritura',4,'p_escritura','lexerparser.py',564),
  ('escritura_aux -> expresion COMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexerparser.py',568),
  ('escritura_aux -> CTESTRING COMA escritura_aux','escritura_aux',3,'p_escritura_aux','lexerparser.py',569),
  ('escritura_aux -> expresion','escritura_aux',1,'p_escritura_aux','lexerparser.py',570),
  ('escritura_aux -> CTESTRING','escritura_aux',1,'p_escritura_aux','lexerparser.py',571),
  ('n_seen_type -> <empty>','n_seen_type',0,'p_n_seen_type','lexerparser.py',591),
  ('n_seen_var_name -> <empty>','n_seen_var_name',0,'p_n_seen_var_name','lexerparser.py',597),
  ('n_seen_func_name -> <empty>','n_seen_func_name',0,'p_n_seen_func_name','lexerparser.py',615),
  ('n_set_var_type -> <empty>','n_set_var_type',0,'p_n_set_var_type','lexerparser.py',687),
  ('n_seen_factor_id -> <empty>','n_seen_factor_id',0,'p_n_seen_factor_id','lexerparser.py',717),
  ('n_seen_factor_int -> <empty>','n_seen_factor_int',0,'p_n_seen_factor_int','lexerparser.py',724),
  ('n_seen_factor_float -> <empty>','n_seen_factor_float',0,'p_n_seen_factor_float','lexerparser.py',738),
  ('n_seen_factor_char -> <empty>','n_seen_factor_char',0,'p_n_seen_factor_char','lexerparser.py',751),
  ('n_assign -> <empty>','n_assign',0,'p_n_assign','lexerparser.py',763),
  ('n_add_operator -> <empty>','n_add_operator',0,'p_n_add_operator','lexerparser.py',783),
  ('n_gen_term -> <empty>','n_gen_term',0,'p_n_gen_term','lexerparser.py',789),
  ('n_gen_factor -> <empty>','n_gen_factor',0,'p_n_gen_factor','lexerparser.py',794),
  ('n_gen_relational -> <empty>','n_gen_relational',0,'p_n_gen_relational','lexerparser.py',798),
  ('n_gen_or -> <empty>','n_gen_or',0,'p_n_gen_or','lexerparser.py',802),
  ('n_gen_and -> <empty>','n_gen_and',0,'p_n_gen_and','lexerparser.py',806),
  ('n_push_fake_bottom -> <empty>','n_push_fake_bottom',0,'p_n_push_fake_bottom','lexerparser.py',810),
  ('n_pop_fake_bottom -> <empty>','n_pop_fake_bottom',0,'p_n_pop_fake_bottom','lexerparser.py',815),
  ('n_check_exp -> <empty>','n_check_exp',0,'p_n_check_exp','lexerparser.py',846),
  ('n_fill_end -> <empty>','n_fill_end',0,'p_n_fill_end','lexerparser.py',860),
  ('n_else -> <empty>','n_else',0,'p_n_else','lexerparser.py',867),
]
