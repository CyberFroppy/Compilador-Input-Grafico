
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaCOLON SEMICOLON LBRACKET RBRACKET EQUAL DBEQUALS NOTEQUAL GREATERT LESST GREATEREQUAL LESSEQUAL AND OR LPAREN RPAREN DOT COMA PLUS MINUS MULTIPLY DIVIDE CTESTRING CTEINT CTEF CTEC TRANSPUESTA DETERMINANTE INVERSA ID COMMENT PROGRAM MAIN VAR INT FLOAT CHAR PRINT IF ELSE THEN TO WHILE DO FOR VOID MODULE RETURN WRITE READprograma : PROGRAM ID SEMICOLON vars module main\n                | PROGRAM ID SEMICOLON module main\n                | PROGRAM ID SEMICOLON vars main\n                | PROGRAM ID SEMICOLON mainmain : MAIN n_seen_func_name n_seen_main bloque_module n_end_programvars : VAR vars_auxvars_aux : ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux\n                | ID n_seen_var_name COLON tipo n_set_var_type DOTvars_func : ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func\n                 | ID n_seen_var_name COLON tipo n_set_var_typetipo : INT n_seen_type\n            | FLOAT n_seen_type\n            | CHAR n_seen_typebloque_module : LBRACKET vars estatuto_aux RBRACKET\n                     | LBRACKET vars RBRACKET\n                     | LBRACKET estatuto_aux RBRACKET\n                     | LBRACKET RBRACKET bloque : LBRACKET estatuto_aux RBRACKET\n              | LBRACKET RBRACKETestatuto_aux : estatuto estatuto_aux\n                    | estatutoestatuto : asignacion SEMICOLON\n                | condicion SEMICOLON\n                | escritura SEMICOLON\n                | lectura SEMICOLON\n                | return SEMICOLON\n                | for SEMICOLON\n                | while SEMICOLON\n                | call_module SEMICOLON\n                asignacion : ID n_seen_factor_id EQUAL n_add_operator expresion n_assignexpresion : exp n_gen_and AND n_add_operator expresion\n                 | exp n_gen_and exp : exp_aux n_gen_or OR n_add_operator exp\n           | exp_aux n_gen_or exp_aux : exp_aux2 n_gen_relational GREATERT n_add_operator exp_aux\n               | exp_aux2 n_gen_relational LESST n_add_operator exp_aux\n               | exp_aux2 n_gen_relational NOTEQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational DBEQUALS n_add_operator exp_aux\n               | exp_aux2 n_gen_relational GREATEREQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational LESSEQUAL n_add_operator exp_aux\n               | exp_aux2 n_gen_relational exp_aux2 : term n_gen_term PLUS n_add_operator exp_aux2 \n                | term n_gen_term MINUS n_add_operator exp_aux2\n                | term n_gen_termterm : factor n_gen_factor MULTIPLY n_add_operator term \n            | factor n_gen_factor DIVIDE n_add_operator term \n            | factor n_gen_factorfactor : LPAREN n_push_fake_bottom expresion RPAREN n_pop_fake_bottom\n              | CTEINT n_seen_factor_int\n              | CTEF n_seen_factor_float\n              | CTEC n_seen_factor_char\n              | ID n_seen_factor_idmodule : MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module\n              | MODULE tipo ID n_seen_func_name params bloque_module module\n              | MODULE VOID n_seen_type ID n_seen_func_name params bloque_module\n              | MODULE tipo ID n_seen_func_name params bloque_moduleparams : LPAREN vars_func RPAREN\n              | LPAREN RPARENcall_module : ID LPAREN expresion RPAREN \n                   | ID LPAREN RPARENreturn : RETURN expresionfor : FOR n_salto_for asignacion TO CTEINT bloquewhile : WHILE n_salto_while LPAREN expresion RPAREN n_cond_while bloque n_ret_while condicion : IF LPAREN expresion RPAREN n_check_exp bloque ELSE n_else bloque n_fill_end\n                 | IF LPAREN expresion RPAREN n_check_exp bloque n_fill_endlectura : READ LPAREN lect_aux RPARENlect_aux : ID n_read\n                | ID n_read COMA lect_auxescritura : PRINT LPAREN escritura_aux RPARENescritura_aux : expresion n_print COMA escritura_aux\n                     | CTESTRING n_seen_string n_print COMA escritura_aux\n                     | expresion n_print\n                     | CTESTRING n_seen_string n_printn_seen_type : n_seen_var_name : n_seen_func_name : n_set_var_type : n_seen_factor_id : n_seen_factor_int : n_seen_factor_float : n_seen_factor_char : n_seen_string : n_assign : n_add_operator : n_gen_term : n_gen_factor : n_gen_relational : n_gen_or : n_gen_and : n_push_fake_bottom : n_pop_fake_bottom : n_check_exp : n_fill_end : n_else : n_seen_main : n_salto_while :n_cond_while :n_ret_while :n_salto_for :n_read : n_print : n_end_program : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,12,13,22,33,39,42,66,67,101,],[0,-4,-3,-2,-1,-102,-5,-17,-15,-16,-14,]),'ID':([2,8,14,16,17,18,19,20,24,26,27,28,34,38,40,43,56,57,69,70,71,72,73,74,75,76,78,79,80,81,88,93,95,96,102,116,123,124,127,135,136,137,138,139,140,141,142,143,144,145,146,153,155,156,157,158,159,160,161,162,163,164,165,166,167,174,176,193,],[3,15,-6,-74,25,-74,-74,-74,31,-11,-12,-13,52,64,52,52,92,-99,-22,-23,-24,-25,-26,-27,-28,-29,92,92,92,110,-90,122,15,-8,-84,92,92,-7,92,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,92,110,92,92,92,92,92,92,92,92,92,92,92,92,52,92,64,]),'SEMICOLON':([3,18,19,20,26,27,28,35,44,45,46,47,48,49,50,51,59,82,83,84,85,86,87,89,90,91,92,104,111,112,113,114,115,117,118,119,120,128,130,133,151,168,172,173,178,179,180,181,182,183,184,185,186,187,188,189,190,191,195,197,199,202,203,204,205,],[4,-74,-74,-74,-11,-12,-13,-77,69,70,71,72,73,74,75,76,95,-61,-89,-88,-87,-85,-86,-79,-80,-81,-78,-60,-32,-34,-41,-44,-47,-49,-50,-51,-52,-59,-69,-66,-83,-91,-30,-93,-31,-33,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,-62,-65,-19,-98,-18,-63,-93,-64,]),'VAR':([4,34,],[8,8,]),'MODULE':([4,5,14,42,61,66,67,96,97,101,124,],[9,9,-6,-17,9,-15,-16,-8,9,-14,-7,]),'MAIN':([4,5,6,11,14,42,61,66,67,96,97,98,101,124,125,],[10,10,10,10,-6,-17,-56,-15,-16,-8,-55,-54,-14,-7,-53,]),'VOID':([9,],[16,]),'INT':([9,30,126,],[18,18,18,]),'FLOAT':([9,30,126,],[19,19,19,]),'CHAR':([9,30,126,],[20,20,20,]),'LBRACKET':([10,21,29,37,60,63,99,129,152,169,170,192,194,201,],[-76,-95,34,34,34,-58,-57,-92,174,174,-97,174,-94,174,]),'RBRACKET':([14,34,40,41,43,65,68,69,70,71,72,73,74,75,76,96,124,174,196,],[-6,42,66,67,-21,101,-20,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,197,202,]),'IF':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,53,53,53,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,53,]),'PRINT':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,54,54,54,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,54,]),'READ':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,55,55,55,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,55,]),'RETURN':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,56,56,56,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,56,]),'FOR':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,57,57,57,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,57,]),'WHILE':([14,34,40,43,69,70,71,72,73,74,75,76,96,124,174,],[-6,58,58,58,-22,-23,-24,-25,-26,-27,-28,-29,-8,-7,58,]),'COLON':([15,23,64,100,],[-75,30,-75,126,]),'DOT':([18,19,20,26,27,28,35,59,],[-74,-74,-74,-11,-12,-13,-77,96,]),'COMA':([18,19,20,26,27,28,83,84,85,86,87,89,90,91,92,107,108,110,111,112,113,114,115,117,118,119,120,131,132,134,150,154,168,171,178,179,180,181,182,183,184,185,186,187,188,189,190,],[-74,-74,-74,-11,-12,-13,-89,-88,-87,-85,-86,-79,-80,-81,-78,-101,-82,-100,-32,-34,-41,-44,-47,-49,-50,-51,-52,153,-101,155,-77,176,-91,193,-31,-33,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,]),'RPAREN':([18,19,20,26,27,28,38,62,78,83,84,85,86,87,89,90,91,92,103,105,106,107,108,109,110,111,112,113,114,115,117,118,119,120,131,132,134,147,149,150,154,168,171,175,177,178,179,180,181,182,183,184,185,186,187,188,189,190,198,200,],[-74,-74,-74,-11,-12,-13,63,99,104,-89,-88,-87,-85,-86,-79,-80,-81,-78,128,129,130,-101,-82,133,-100,-32,-34,-41,-44,-47,-49,-50,-51,-52,-72,-101,-67,168,170,-77,-73,-91,-10,-70,-68,-31,-33,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,-71,-9,]),'LPAREN':([25,31,32,36,52,53,54,55,56,58,78,79,80,88,94,102,116,123,127,135,136,137,138,139,140,141,142,143,144,145,146,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[-76,-76,38,38,78,79,80,81,88,-96,88,88,88,-90,123,-84,88,88,88,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'EQUAL':([52,77,122,],[-78,102,-78,]),'CTEINT':([56,78,79,80,88,102,116,123,127,135,136,137,138,139,140,141,142,143,144,145,146,148,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[89,89,89,89,-90,-84,89,89,89,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,169,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'CTEF':([56,78,79,80,88,102,116,123,127,135,136,137,138,139,140,141,142,143,144,145,146,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[90,90,90,90,-90,-84,90,90,90,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,90,90,90,90,90,90,90,90,90,90,90,90,90,90,]),'CTEC':([56,78,79,80,88,102,116,123,127,135,136,137,138,139,140,141,142,143,144,145,146,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[91,91,91,91,-90,-84,91,91,91,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,-84,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'CTESTRING':([80,153,176,],[108,108,108,]),'AND':([83,84,85,86,87,89,90,91,92,111,112,113,114,115,117,118,119,120,168,179,180,181,182,183,184,185,186,187,188,189,190,],[-89,-88,-87,-85,-86,-79,-80,-81,-78,135,-34,-41,-44,-47,-49,-50,-51,-52,-91,-33,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,]),'TO':([83,84,85,86,87,89,90,91,92,111,112,113,114,115,117,118,119,120,121,151,168,172,178,179,180,181,182,183,184,185,186,187,188,189,190,],[-89,-88,-87,-85,-86,-79,-80,-81,-78,-32,-34,-41,-44,-47,-49,-50,-51,-52,148,-83,-91,-30,-31,-33,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,]),'OR':([84,85,86,87,89,90,91,92,112,113,114,115,117,118,119,120,168,180,181,182,183,184,185,186,187,188,189,190,],[-88,-87,-85,-86,-79,-80,-81,-78,136,-41,-44,-47,-49,-50,-51,-52,-91,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-48,]),'GREATERT':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,137,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'LESST':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,138,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'NOTEQUAL':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,139,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'DBEQUALS':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,140,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'GREATEREQUAL':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,141,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'LESSEQUAL':([85,86,87,89,90,91,92,113,114,115,117,118,119,120,168,186,187,188,189,190,],[-87,-85,-86,-79,-80,-81,-78,142,-44,-47,-49,-50,-51,-52,-91,-42,-43,-45,-46,-48,]),'PLUS':([86,87,89,90,91,92,114,115,117,118,119,120,168,188,189,190,],[-85,-86,-79,-80,-81,-78,143,-47,-49,-50,-51,-52,-91,-45,-46,-48,]),'MINUS':([86,87,89,90,91,92,114,115,117,118,119,120,168,188,189,190,],[-85,-86,-79,-80,-81,-78,144,-47,-49,-50,-51,-52,-91,-45,-46,-48,]),'MULTIPLY':([87,89,90,91,92,115,117,118,119,120,168,190,],[-86,-79,-80,-81,-78,145,-49,-50,-51,-52,-91,-48,]),'DIVIDE':([87,89,90,91,92,115,117,118,119,120,168,190,],[-86,-79,-80,-81,-78,146,-49,-50,-51,-52,-91,-48,]),'ELSE':([173,197,202,],[194,-19,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'vars':([4,34,],[5,40,]),'module':([4,5,61,97,],[6,11,98,125,]),'main':([4,5,6,11,],[7,12,13,22,]),'vars_aux':([8,95,],[14,124,]),'tipo':([9,30,126,],[17,35,150,]),'n_seen_func_name':([10,25,31,],[21,32,36,]),'n_seen_var_name':([15,64,],[23,100,]),'n_seen_type':([16,18,19,20,],[24,26,27,28,]),'n_seen_main':([21,],[29,]),'bloque_module':([29,37,60,],[33,61,97,]),'params':([32,36,],[37,60,]),'n_end_program':([33,],[39,]),'estatuto_aux':([34,40,43,174,],[41,65,68,196,]),'estatuto':([34,40,43,174,],[43,43,43,43,]),'asignacion':([34,40,43,93,174,],[44,44,44,121,44,]),'condicion':([34,40,43,174,],[45,45,45,45,]),'escritura':([34,40,43,174,],[46,46,46,46,]),'lectura':([34,40,43,174,],[47,47,47,47,]),'return':([34,40,43,174,],[48,48,48,48,]),'for':([34,40,43,174,],[49,49,49,49,]),'while':([34,40,43,174,],[50,50,50,50,]),'call_module':([34,40,43,174,],[51,51,51,51,]),'n_set_var_type':([35,150,],[59,171,]),'vars_func':([38,193,],[62,200,]),'n_seen_factor_id':([52,92,122,],[77,120,77,]),'expresion':([56,78,79,80,116,123,127,153,156,176,],[82,103,105,107,147,149,151,107,178,107,]),'exp':([56,78,79,80,116,123,127,153,156,157,176,],[83,83,83,83,83,83,83,83,83,179,83,]),'exp_aux':([56,78,79,80,116,123,127,153,156,157,158,159,160,161,162,163,176,],[84,84,84,84,84,84,84,84,84,84,180,181,182,183,184,185,84,]),'exp_aux2':([56,78,79,80,116,123,127,153,156,157,158,159,160,161,162,163,164,165,176,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,186,187,85,]),'term':([56,78,79,80,116,123,127,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,188,189,86,]),'factor':([56,78,79,80,116,123,127,153,156,157,158,159,160,161,162,163,164,165,166,167,176,],[87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,]),'n_salto_for':([57,],[93,]),'n_salto_while':([58,],[94,]),'escritura_aux':([80,153,176,],[106,175,198,]),'lect_aux':([81,155,],[109,177,]),'n_gen_and':([83,],[111,]),'n_gen_or':([84,],[112,]),'n_gen_relational':([85,],[113,]),'n_gen_term':([86,],[114,]),'n_gen_factor':([87,],[115,]),'n_push_fake_bottom':([88,],[116,]),'n_seen_factor_int':([89,],[117,]),'n_seen_factor_float':([90,],[118,]),'n_seen_factor_char':([91,],[119,]),'n_add_operator':([102,135,136,137,138,139,140,141,142,143,144,145,146,],[127,156,157,158,159,160,161,162,163,164,165,166,167,]),'n_print':([107,132,],[131,154,]),'n_seen_string':([108,],[132,]),'n_read':([110,],[134,]),'n_check_exp':([129,],[152,]),'n_assign':([151,],[172,]),'bloque':([152,169,192,201,],[173,191,199,204,]),'n_pop_fake_bottom':([168,],[190,]),'n_cond_while':([170,],[192,]),'n_fill_end':([173,204,],[195,205,]),'n_else':([194,],[201,]),'n_ret_while':([199,],[203,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON vars module main','programa',6,'p_programa','lexerparser.py',440),
  ('programa -> PROGRAM ID SEMICOLON module main','programa',5,'p_programa','lexerparser.py',441),
  ('programa -> PROGRAM ID SEMICOLON vars main','programa',5,'p_programa','lexerparser.py',442),
  ('programa -> PROGRAM ID SEMICOLON main','programa',4,'p_programa','lexerparser.py',443),
  ('main -> MAIN n_seen_func_name n_seen_main bloque_module n_end_program','main',5,'p_main','lexerparser.py',448),
  ('vars -> VAR vars_aux','vars',2,'p_vars','lexerparser.py',452),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type SEMICOLON vars_aux','vars_aux',7,'p_vars_aux','lexerparser.py',456),
  ('vars_aux -> ID n_seen_var_name COLON tipo n_set_var_type DOT','vars_aux',6,'p_vars_aux','lexerparser.py',457),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type COMA vars_func','vars_func',7,'p_vars_func','lexerparser.py',460),
  ('vars_func -> ID n_seen_var_name COLON tipo n_set_var_type','vars_func',5,'p_vars_func','lexerparser.py',461),
  ('tipo -> INT n_seen_type','tipo',2,'p_tipo','lexerparser.py',464),
  ('tipo -> FLOAT n_seen_type','tipo',2,'p_tipo','lexerparser.py',465),
  ('tipo -> CHAR n_seen_type','tipo',2,'p_tipo','lexerparser.py',466),
  ('bloque_module -> LBRACKET vars estatuto_aux RBRACKET','bloque_module',4,'p_bloque_module','lexerparser.py',470),
  ('bloque_module -> LBRACKET vars RBRACKET','bloque_module',3,'p_bloque_module','lexerparser.py',471),
  ('bloque_module -> LBRACKET estatuto_aux RBRACKET','bloque_module',3,'p_bloque_module','lexerparser.py',472),
  ('bloque_module -> LBRACKET RBRACKET','bloque_module',2,'p_bloque_module','lexerparser.py',473),
  ('bloque -> LBRACKET estatuto_aux RBRACKET','bloque',3,'p_bloque','lexerparser.py',477),
  ('bloque -> LBRACKET RBRACKET','bloque',2,'p_bloque','lexerparser.py',478),
  ('estatuto_aux -> estatuto estatuto_aux','estatuto_aux',2,'p_estatuto_aux','lexerparser.py',482),
  ('estatuto_aux -> estatuto','estatuto_aux',1,'p_estatuto_aux','lexerparser.py',483),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',487),
  ('estatuto -> condicion SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',488),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',489),
  ('estatuto -> lectura SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',490),
  ('estatuto -> return SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',491),
  ('estatuto -> for SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',492),
  ('estatuto -> while SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',493),
  ('estatuto -> call_module SEMICOLON','estatuto',2,'p_estatuto','lexerparser.py',494),
  ('asignacion -> ID n_seen_factor_id EQUAL n_add_operator expresion n_assign','asignacion',6,'p_asignacion','lexerparser.py',499),
  ('expresion -> exp n_gen_and AND n_add_operator expresion','expresion',5,'p_expresion','lexerparser.py',503),
  ('expresion -> exp n_gen_and','expresion',2,'p_expresion','lexerparser.py',504),
  ('exp -> exp_aux n_gen_or OR n_add_operator exp','exp',5,'p_exp','lexerparser.py',508),
  ('exp -> exp_aux n_gen_or','exp',2,'p_exp','lexerparser.py',509),
  ('exp_aux -> exp_aux2 n_gen_relational GREATERT n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',513),
  ('exp_aux -> exp_aux2 n_gen_relational LESST n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',514),
  ('exp_aux -> exp_aux2 n_gen_relational NOTEQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',515),
  ('exp_aux -> exp_aux2 n_gen_relational DBEQUALS n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',516),
  ('exp_aux -> exp_aux2 n_gen_relational GREATEREQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',517),
  ('exp_aux -> exp_aux2 n_gen_relational LESSEQUAL n_add_operator exp_aux','exp_aux',5,'p_exp_aux','lexerparser.py',518),
  ('exp_aux -> exp_aux2 n_gen_relational','exp_aux',2,'p_exp_aux','lexerparser.py',519),
  ('exp_aux2 -> term n_gen_term PLUS n_add_operator exp_aux2','exp_aux2',5,'p_exp_aux2','lexerparser.py',523),
  ('exp_aux2 -> term n_gen_term MINUS n_add_operator exp_aux2','exp_aux2',5,'p_exp_aux2','lexerparser.py',524),
  ('exp_aux2 -> term n_gen_term','exp_aux2',2,'p_exp_aux2','lexerparser.py',525),
  ('term -> factor n_gen_factor MULTIPLY n_add_operator term','term',5,'p_term','lexerparser.py',529),
  ('term -> factor n_gen_factor DIVIDE n_add_operator term','term',5,'p_term','lexerparser.py',530),
  ('term -> factor n_gen_factor','term',2,'p_term','lexerparser.py',531),
  ('factor -> LPAREN n_push_fake_bottom expresion RPAREN n_pop_fake_bottom','factor',5,'p_factor','lexerparser.py',535),
  ('factor -> CTEINT n_seen_factor_int','factor',2,'p_factor','lexerparser.py',536),
  ('factor -> CTEF n_seen_factor_float','factor',2,'p_factor','lexerparser.py',537),
  ('factor -> CTEC n_seen_factor_char','factor',2,'p_factor','lexerparser.py',538),
  ('factor -> ID n_seen_factor_id','factor',2,'p_factor','lexerparser.py',539),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module module','module',8,'p_module','lexerparser.py',544),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module module','module',7,'p_module','lexerparser.py',545),
  ('module -> MODULE VOID n_seen_type ID n_seen_func_name params bloque_module','module',7,'p_module','lexerparser.py',546),
  ('module -> MODULE tipo ID n_seen_func_name params bloque_module','module',6,'p_module','lexerparser.py',547),
  ('params -> LPAREN vars_func RPAREN','params',3,'p_params','lexerparser.py',550),
  ('params -> LPAREN RPAREN','params',2,'p_params','lexerparser.py',551),
  ('call_module -> ID LPAREN expresion RPAREN','call_module',4,'p_call_module','lexerparser.py',554),
  ('call_module -> ID LPAREN RPAREN','call_module',3,'p_call_module','lexerparser.py',555),
  ('return -> RETURN expresion','return',2,'p_return','lexerparser.py',558),
  ('for -> FOR n_salto_for asignacion TO CTEINT bloque','for',6,'p_for','lexerparser.py',562),
  ('while -> WHILE n_salto_while LPAREN expresion RPAREN n_cond_while bloque n_ret_while','while',8,'p_while','lexerparser.py',566),
  ('condicion -> IF LPAREN expresion RPAREN n_check_exp bloque ELSE n_else bloque n_fill_end','condicion',10,'p_condicion','lexerparser.py',570),
  ('condicion -> IF LPAREN expresion RPAREN n_check_exp bloque n_fill_end','condicion',7,'p_condicion','lexerparser.py',571),
  ('lectura -> READ LPAREN lect_aux RPAREN','lectura',4,'p_lectura','lexerparser.py',574),
  ('lect_aux -> ID n_read','lect_aux',2,'p_lectura_aux','lexerparser.py',578),
  ('lect_aux -> ID n_read COMA lect_aux','lect_aux',4,'p_lectura_aux','lexerparser.py',579),
  ('escritura -> PRINT LPAREN escritura_aux RPAREN','escritura',4,'p_escritura','lexerparser.py',582),
  ('escritura_aux -> expresion n_print COMA escritura_aux','escritura_aux',4,'p_escritura_aux','lexerparser.py',586),
  ('escritura_aux -> CTESTRING n_seen_string n_print COMA escritura_aux','escritura_aux',5,'p_escritura_aux','lexerparser.py',587),
  ('escritura_aux -> expresion n_print','escritura_aux',2,'p_escritura_aux','lexerparser.py',588),
  ('escritura_aux -> CTESTRING n_seen_string n_print','escritura_aux',3,'p_escritura_aux','lexerparser.py',589),
  ('n_seen_type -> <empty>','n_seen_type',0,'p_n_seen_type','lexerparser.py',609),
  ('n_seen_var_name -> <empty>','n_seen_var_name',0,'p_n_seen_var_name','lexerparser.py',615),
  ('n_seen_func_name -> <empty>','n_seen_func_name',0,'p_n_seen_func_name','lexerparser.py',633),
  ('n_set_var_type -> <empty>','n_set_var_type',0,'p_n_set_var_type','lexerparser.py',711),
  ('n_seen_factor_id -> <empty>','n_seen_factor_id',0,'p_n_seen_factor_id','lexerparser.py',741),
  ('n_seen_factor_int -> <empty>','n_seen_factor_int',0,'p_n_seen_factor_int','lexerparser.py',748),
  ('n_seen_factor_float -> <empty>','n_seen_factor_float',0,'p_n_seen_factor_float','lexerparser.py',761),
  ('n_seen_factor_char -> <empty>','n_seen_factor_char',0,'p_n_seen_factor_char','lexerparser.py',774),
  ('n_seen_string -> <empty>','n_seen_string',0,'p_n_seen_string','lexerparser.py',788),
  ('n_assign -> <empty>','n_assign',0,'p_n_assign','lexerparser.py',802),
  ('n_add_operator -> <empty>','n_add_operator',0,'p_n_add_operator','lexerparser.py',817),
  ('n_gen_term -> <empty>','n_gen_term',0,'p_n_gen_term','lexerparser.py',823),
  ('n_gen_factor -> <empty>','n_gen_factor',0,'p_n_gen_factor','lexerparser.py',828),
  ('n_gen_relational -> <empty>','n_gen_relational',0,'p_n_gen_relational','lexerparser.py',833),
  ('n_gen_or -> <empty>','n_gen_or',0,'p_n_gen_or','lexerparser.py',839),
  ('n_gen_and -> <empty>','n_gen_and',0,'p_n_gen_and','lexerparser.py',844),
  ('n_push_fake_bottom -> <empty>','n_push_fake_bottom',0,'p_n_push_fake_bottom','lexerparser.py',850),
  ('n_pop_fake_bottom -> <empty>','n_pop_fake_bottom',0,'p_n_pop_fake_bottom','lexerparser.py',856),
  ('n_check_exp -> <empty>','n_check_exp',0,'p_n_check_exp','lexerparser.py',887),
  ('n_fill_end -> <empty>','n_fill_end',0,'p_n_fill_end','lexerparser.py',900),
  ('n_else -> <empty>','n_else',0,'p_n_else','lexerparser.py',907),
  ('n_seen_main -> <empty>','n_seen_main',0,'p_n_seen_main','lexerparser.py',917),
  ('n_salto_while -> <empty>','n_salto_while',0,'p_n_salto_while','lexerparser.py',926),
  ('n_cond_while -> <empty>','n_cond_while',0,'p_n_cond_while','lexerparser.py',932),
  ('n_ret_while -> <empty>','n_ret_while',0,'p_n_ret_while','lexerparser.py',945),
  ('n_salto_for -> <empty>','n_salto_for',0,'p_n_salto_for','lexerparser.py',957),
  ('n_read -> <empty>','n_read',0,'p_n_read','lexerparser.py',969),
  ('n_print -> <empty>','n_print',0,'p_n_print','lexerparser.py',977),
  ('n_end_program -> <empty>','n_end_program',0,'p_n_end_program','lexerparser.py',988),
]
