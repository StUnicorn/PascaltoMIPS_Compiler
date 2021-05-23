
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programASSIGNMENT COLON COMMA COMMENT DIGITSEQ DOT IDENTIFIER LESSOREQ LPAREN MOREOREQ NOTEQ REALNUMBER RESERVED_AND RESERVED_BEGIN RESERVED_CONST RESERVED_DIV RESERVED_DO RESERVED_END RESERVED_FALSE RESERVED_FOR RESERVED_FUNCTION RESERVED_IF RESERVED_MOD RESERVED_NOT RESERVED_OR RESERVED_PROGRAM RESERVED_REPEAT RESERVED_STRING RESERVED_THEN RESERVED_TO RESERVED_TRUE RESERVED_UNTIL RESERVED_VAR RESERVED_WHILE RPAREN SEMI_COLON STRINGsign :  '+' sign :  '-' non_string :  DIGITSEQidentifier_list :  identifier_list comma identifieridentifier_list :  identifierconstant :  non_stringconstant :  sign non_stringtype_definition_list :  type_definition_list type_definitiontype_definition_list :  type_definitiontype_definition :  identifier '=' type_denoter semicolontype_denoter :  identifiercomponent_type :  identifierdomain_type :  identifiervariable_declaration_part :  RESERVED_VAR variable_declaration_list semicolonvariable_declaration :  identifier_list COLON type_denotervariable_declaration_list :    variable_declaration_list semicolon variable_declarationvariable_declaration_list :  variable_declarationprocedure_and_function_declaration_part :  function_declaration semicolonformal_parameter_section_list :  formal_parameter_section_list semicolon formal_parameter_sectionformal_parameter_section_list :  formal_parameter_sectionformal_parameter_list :  LPAREN formal_parameter_section_list RPARENformal_parameter_section :  value_parameter_specificationformal_parameter_section :  variable_parameter_specificationvalue_parameter_specification :  identifier_list COLON identifierprocedure_block :  blocksimple_expression :  termsimple_expression :  simple_expression addop termfunction_declaration :  function_identification semicolon function_blockfunction_declaration :  function_heading semicolon function_blockfunction_heading :  RESERVED_FUNCTION identifier COLON result_typefunction_heading :  RESERVED_FUNCTION identifier marker_fh formal_parameter_list COLON result_typedeclaration_part_list :  declaration_part_list declaration_entitydeclaration_part_list :  declaration_entitymarker_fh :primary :  variable_accessprimary :  unsigned_constantprimary :  function_designatorresult_type :  identifierfunction_identification :  RESERVED_FUNCTION identifierfunction_block :  blockstatement_part :  compound_statementcompound_statement :  RESERVED_BEGIN statement_sequence RESERVED_ENDvariable_parameter_specification :  RESERVED_VAR identifier_list COLON identifierstatement_sequence :  statement_sequence semicolon statementstatement_sequence :  statementstatement :  open_statementstatement :  closed_statementopen_statement :  non_labeled_open_statementclosed_statement :  non_labeled_closed_statementnon_labeled_closed_statement :  assignment_statementnon_labeled_closed_statement :  procedure_statementnon_labeled_closed_statement :  compound_statementnon_labeled_closed_statement :  repeat_statementnon_labeled_closed_statement :  closed_while_statementnon_labeled_closed_statement :  closed_for_statementnon_labeled_closed_statement : non_labeled_open_statement :  open_if_statementnon_labeled_open_statement :  open_while_statementnon_labeled_open_statement :  open_for_statementrepeat_statement :  RESERVED_REPEAT repeat_begin_marker statement_sequence RESERVED_UNTIL boolean_expressionrepeat_begin_marker : open_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO open_statementclosed_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO closed_statementmarker_while :open_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO open_statementclosed_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO closed_statementmarker_for_for_branching : open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching statementmarker_if_false :marker_for_branching :assignment_statement :  variable_access ASSIGNMENT expressionvariable_access :  identifierindex_expression_list :  index_expression_list comma index_expressionindex_expression_list :  index_expressionindex_expression :  expressionprocedure_statement :  identifier paramsprocedure_statement :  identifierdeclaration_entity :  procedure_and_function_declaration_partparams :  LPAREN actual_parameter_list RPARENactual_parameter_list :  actual_parameter_list comma actual_parameteractual_parameter_list :  actual_parameteractual_parameter :  expressionactual_parameter :  expression COLON expressionactual_parameter :  expression COLON expression COLON expressioncontrol_variable :  identifierinitial_value :  expressiondirection :  RESERVED_TOfinal_value :  expressionrecord_variable_list :  record_variable_list comma variable_accessrecord_variable_list :  variable_accessboolean_expression :  expressionunsigned_constant :  unsigned_numberunsigned_constant :  STRINGblock :  declaration_part_list statement_partblock :  statement_partdeclaration_entity :  variable_declaration_partexpression :  simple_expressionexpression :  simple_expression relop simple_expressionterm :  factorterm :  term mulop factorfactor :  sign factorfactor :  exponentiationexponentiation :  primaryprimary :  LPAREN expression RPARENprimary :  RESERVED_NOT primaryunsigned_number :  unsigned_integerunsigned_number :  unsigned_realunsigned_integer :  DIGITSEQunsigned_real :  REALNUMBERfunction_designator :  identifier paramsaddop :  '+' addop :  '-' addop :  RESERVED_ORmulop :  '*' mulop :  '/' mulop :  RESERVED_DIVmulop :  RESERVED_MODmulop :  RESERVED_ANDrelop :  '=' relop :  NOTEQrelop :  '<' relop :  '>' relop :  LESSOREQrelop :  MOREOREQidentifier :  IDENTIFIERidentifier :  RESERVED_STRINGsemicolon :  SEMI_COLONcomma :  COMMAprogram :  program_heading semicolon block DOTprogram_heading :  RESERVED_PROGRAM identifierprogram_heading :  RESERVED_PROGRAM identifier LPAREN identifier_list RPAREN"
    
_lr_action_items = {'RESERVED_PROGRAM':([0,],[3,]),'$end':([1,23,],[0,-129,]),'SEMI_COLON':([2,5,6,7,8,11,13,16,17,19,20,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,48,49,54,56,57,59,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,84,86,91,92,93,96,97,98,116,118,119,122,126,127,128,129,131,132,135,136,137,138,139,140,143,148,149,150,151,154,155,156,161,162,170,171,175,176,177,178,],[5,-127,-130,-125,-126,-95,-41,-56,5,5,5,-94,5,-45,-46,-47,-48,-49,-57,-58,-59,-50,-51,-52,-53,-54,-55,-77,-61,5,-17,-39,-42,-56,-91,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-76,-56,-28,-40,-29,-131,-44,-70,-101,-105,-110,-71,5,-16,-15,-11,-38,-30,-56,-98,-27,-100,-104,-56,-79,5,-20,-22,-23,-68,-62,-63,-60,-31,-19,-24,-43,-56,-65,-66,]),'IDENTIFIER':([3,5,16,18,21,22,41,42,43,46,57,63,65,66,71,72,83,85,86,87,88,89,90,94,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,134,135,140,144,145,146,147,153,157,158,164,165,169,172,176,],[7,-127,7,7,7,7,7,7,7,-61,7,7,-1,-2,7,7,7,7,7,7,7,7,-128,7,-70,7,7,-119,-120,-121,-122,-123,-124,-111,-112,-113,7,-114,-115,-116,-117,-118,7,7,7,7,7,7,7,7,7,7,-87,7,7,7,7,7,]),'RESERVED_STRING':([3,5,16,18,21,22,41,42,43,46,57,63,65,66,71,72,83,85,86,87,88,89,90,94,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,134,135,140,144,145,146,147,153,157,158,164,165,169,172,176,],[8,-127,8,8,8,8,8,8,8,-61,8,8,-1,-2,8,8,8,8,8,8,8,8,-128,8,-70,8,8,-119,-120,-121,-122,-123,-124,-111,-112,-113,8,-114,-115,-116,-117,-118,8,8,8,8,8,8,8,8,8,8,-87,8,8,8,8,8,]),'RESERVED_BEGIN':([4,5,10,12,14,15,16,25,46,47,52,53,57,86,87,98,135,140,176,],[16,-127,16,-33,-78,-96,16,-32,-61,-18,16,16,16,16,-14,-70,16,16,16,]),'RESERVED_VAR':([4,5,10,12,14,15,25,47,52,53,87,134,164,],[18,-127,18,-33,-78,-96,-32,-18,18,18,-14,153,153,]),'RESERVED_FUNCTION':([4,5,10,12,14,15,25,47,52,53,87,],[21,-127,21,-33,-78,-96,-32,-18,21,21,-14,]),'RESERVED_IF':([5,16,46,57,86,98,135,140,176,],[-127,41,-61,41,41,-70,41,41,41,]),'RESERVED_WHILE':([5,16,46,57,86,98,135,140,176,],[-127,42,-61,42,42,-70,42,42,42,]),'RESERVED_FOR':([5,16,46,57,86,98,135,140,176,],[-127,43,-61,43,43,-70,43,43,43,]),'RESERVED_REPEAT':([5,16,46,57,86,98,135,140,176,],[-127,46,-61,46,46,-70,46,46,46,]),'RESERVED_END':([5,7,8,16,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,56,57,59,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,84,97,98,116,118,119,122,135,136,137,138,139,140,143,154,155,156,161,176,177,178,],[-127,-125,-126,-56,56,-45,-46,-47,-48,-49,-57,-58,-59,-50,-51,-52,-53,-54,-55,-77,-42,-56,-91,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-76,-44,-70,-101,-105,-110,-71,-56,-98,-27,-100,-104,-56,-79,-68,-62,-63,-60,-56,-65,-66,]),'RESERVED_UNTIL':([5,7,8,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,56,57,59,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,84,86,97,98,116,118,119,122,126,135,136,137,138,139,140,143,154,155,156,161,176,177,178,],[-127,-125,-126,-45,-46,-47,-48,-49,-57,-58,-59,-50,-51,-52,-53,-54,-55,-77,-61,-42,-56,-91,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-76,-56,-44,-70,-101,-105,-110,-71,146,-56,-98,-27,-100,-104,-56,-79,-68,-62,-63,-60,-56,-65,-66,]),'LPAREN':([6,7,8,41,42,45,54,63,65,66,71,72,73,83,85,90,95,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,144,145,146,157,158,169,],[22,-125,-126,71,71,85,-34,71,-1,-2,71,71,85,71,71,-128,134,71,71,-119,-120,-121,-122,-123,-124,-111,-112,-113,71,-114,-115,-116,-117,-118,71,71,71,71,71,-87,71,]),'ASSIGNMENT':([7,8,44,45,81,82,],[-125,-126,83,-72,121,-85,]),'COLON':([7,8,50,51,54,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,125,130,133,136,137,138,139,143,152,160,163,166,],[-125,-126,88,-5,94,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,145,-4,147,-98,-27,-100,-104,-79,165,169,-21,172,]),'COMMA':([7,8,50,51,55,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,123,124,125,130,136,137,138,139,143,152,159,160,166,174,],[-125,-126,90,-5,90,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,90,-81,-82,-4,-98,-27,-100,-104,-79,90,-80,-83,90,-84,]),'RPAREN':([7,8,51,55,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,117,118,119,123,124,125,130,136,137,138,139,143,148,149,150,151,159,160,170,171,174,175,],[-125,-126,-5,96,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,139,-105,-110,143,-81,-82,-4,-98,-27,-100,-104,-79,163,-20,-22,-23,-80,-83,-19,-24,-84,-43,]),'*':([7,8,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,111,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,111,-100,-104,-79,]),'/':([7,8,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,112,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,112,-100,-104,-79,]),'RESERVED_DIV':([7,8,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,113,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,113,-100,-104,-79,]),'RESERVED_MOD':([7,8,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,114,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,114,-100,-104,-79,]),'RESERVED_AND':([7,8,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,115,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,115,-100,-104,-79,]),'=':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,101,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'NOTEQ':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,102,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'<':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,103,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'>':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,104,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'LESSOREQ':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,105,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'MOREOREQ':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,137,138,139,143,],[-125,-126,106,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-27,-100,-104,-79,]),'+':([7,8,41,42,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,78,79,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,121,136,137,138,139,143,144,145,146,157,158,169,],[-125,-126,65,65,107,-26,-99,65,-102,-1,-2,-103,-35,-36,-37,65,-72,-92,-93,-106,-107,-108,-109,65,65,-128,65,65,-119,-120,-121,-122,-123,-124,-111,-112,-113,65,-114,-115,-116,-117,-118,-101,-105,-110,65,107,-27,-100,-104,-79,65,65,65,65,-87,65,]),'-':([7,8,41,42,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,78,79,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,121,136,137,138,139,143,144,145,146,157,158,169,],[-125,-126,66,66,108,-26,-99,66,-102,-1,-2,-103,-35,-36,-37,66,-72,-92,-93,-106,-107,-108,-109,66,66,-128,66,66,-119,-120,-121,-122,-123,-124,-111,-112,-113,66,-114,-115,-116,-117,-118,-101,-105,-110,66,108,-27,-100,-104,-79,66,66,66,66,-87,66,]),'RESERVED_OR':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,136,137,138,139,143,],[-125,-126,109,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,109,-27,-100,-104,-79,]),'RESERVED_THEN':([7,8,58,59,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,136,137,138,139,143,],[-125,-126,98,-91,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-98,-27,-100,-104,-79,]),'RESERVED_DO':([7,8,59,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,80,116,118,119,120,136,137,138,139,143,167,168,173,],[-125,-126,-91,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-64,-101,-105,-110,140,-98,-27,-100,-104,-79,-67,-88,176,]),'RESERVED_TO':([7,8,60,61,62,64,67,68,69,70,73,74,75,76,77,78,79,116,118,119,136,137,138,139,141,142,143,],[-125,-126,-97,-26,-99,-102,-103,-35,-36,-37,-72,-92,-93,-106,-107,-108,-109,-101,-105,-110,-98,-27,-100,-104,158,-86,-79,]),'DOT':([9,11,13,24,56,],[23,-95,-41,-94,-42,]),'RESERVED_NOT':([41,42,63,65,66,71,72,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,144,145,146,157,158,169,],[72,72,72,-1,-2,72,72,72,72,-128,72,72,-119,-120,-121,-122,-123,-124,-111,-112,-113,72,-114,-115,-116,-117,-118,72,72,72,72,72,-87,72,]),'STRING':([41,42,63,65,66,71,72,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,144,145,146,157,158,169,],[75,75,75,-1,-2,75,75,75,75,-128,75,75,-119,-120,-121,-122,-123,-124,-111,-112,-113,75,-114,-115,-116,-117,-118,75,75,75,75,75,-87,75,]),'DIGITSEQ':([41,42,63,65,66,71,72,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,144,145,146,157,158,169,],[78,78,78,-1,-2,78,78,78,78,-128,78,78,-119,-120,-121,-122,-123,-124,-111,-112,-113,78,-114,-115,-116,-117,-118,78,78,78,78,78,-87,78,]),'REALNUMBER':([41,42,63,65,66,71,72,83,85,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,121,144,145,146,157,158,169,],[79,79,79,-1,-2,79,79,79,79,-128,79,79,-119,-120,-121,-122,-123,-124,-111,-112,-113,79,-114,-115,-116,-117,-118,79,79,79,79,79,-87,79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_heading':([0,],[2,]),'semicolon':([2,17,19,20,26,48,126,148,],[4,47,52,53,57,87,57,164,]),'identifier':([3,16,18,21,22,41,42,43,57,63,71,72,83,85,86,87,88,89,94,99,100,110,121,134,135,140,144,145,146,147,153,157,164,165,169,172,176,],[6,45,51,54,51,73,73,82,45,73,73,73,73,73,45,51,129,130,131,73,73,73,73,51,45,45,73,73,73,131,51,73,51,171,73,175,45,]),'block':([4,52,53,],[9,92,92,]),'declaration_part_list':([4,52,53,],[10,10,10,]),'statement_part':([4,10,52,53,],[11,24,11,11,]),'declaration_entity':([4,10,52,53,],[12,25,12,12,]),'compound_statement':([4,10,16,52,53,57,86,135,140,176,],[13,13,37,13,13,37,37,37,37,37,]),'procedure_and_function_declaration_part':([4,10,52,53,],[14,14,14,14,]),'variable_declaration_part':([4,10,52,53,],[15,15,15,15,]),'function_declaration':([4,10,52,53,],[17,17,17,17,]),'function_identification':([4,10,52,53,],[19,19,19,19,]),'function_heading':([4,10,52,53,],[20,20,20,20,]),'statement_sequence':([16,86,],[26,126,]),'statement':([16,57,86,135,],[27,97,27,154,]),'open_statement':([16,57,86,135,140,176,],[28,28,28,28,155,177,]),'closed_statement':([16,57,86,135,140,176,],[29,29,29,29,156,178,]),'non_labeled_open_statement':([16,57,86,135,140,176,],[30,30,30,30,30,30,]),'non_labeled_closed_statement':([16,57,86,135,140,176,],[31,31,31,31,31,31,]),'open_if_statement':([16,57,86,135,140,176,],[32,32,32,32,32,32,]),'open_while_statement':([16,57,86,135,140,176,],[33,33,33,33,33,33,]),'open_for_statement':([16,57,86,135,140,176,],[34,34,34,34,34,34,]),'assignment_statement':([16,57,86,135,140,176,],[35,35,35,35,35,35,]),'procedure_statement':([16,57,86,135,140,176,],[36,36,36,36,36,36,]),'repeat_statement':([16,57,86,135,140,176,],[38,38,38,38,38,38,]),'closed_while_statement':([16,57,86,135,140,176,],[39,39,39,39,39,39,]),'closed_for_statement':([16,57,86,135,140,176,],[40,40,40,40,40,40,]),'variable_access':([16,41,42,57,63,71,72,83,85,86,99,100,110,121,135,140,144,145,146,157,169,176,],[44,68,68,44,68,68,68,68,68,44,68,68,68,68,44,44,68,68,68,68,68,44,]),'variable_declaration_list':([18,],[48,]),'variable_declaration':([18,87,],[49,127,]),'identifier_list':([18,22,87,134,153,164,],[50,55,50,152,166,152,]),'boolean_expression':([41,42,146,],[58,80,161,]),'expression':([41,42,71,83,85,121,144,145,146,157,169,],[59,59,117,122,125,142,125,160,59,168,174,]),'simple_expression':([41,42,71,83,85,99,121,144,145,146,157,169,],[60,60,60,60,60,136,60,60,60,60,60,60,]),'term':([41,42,71,83,85,99,100,121,144,145,146,157,169,],[61,61,61,61,61,61,137,61,61,61,61,61,61,]),'factor':([41,42,63,71,83,85,99,100,110,121,144,145,146,157,169,],[62,62,116,62,62,62,62,62,138,62,62,62,62,62,62,]),'sign':([41,42,63,71,83,85,99,100,110,121,144,145,146,157,169,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'exponentiation':([41,42,63,71,83,85,99,100,110,121,144,145,146,157,169,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'primary':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[67,67,67,67,118,67,67,67,67,67,67,67,67,67,67,67,]),'unsigned_constant':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'function_designator':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'unsigned_number':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'unsigned_integer':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'unsigned_real':([41,42,63,71,72,83,85,99,100,110,121,144,145,146,157,169,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'control_variable':([43,],[81,]),'params':([45,73,],[84,119,]),'repeat_begin_marker':([46,],[86,]),'comma':([50,55,123,152,166,],[89,89,144,89,89,]),'function_block':([52,53,],[91,93,]),'marker_fh':([54,],[95,]),'relop':([60,],[99,]),'addop':([60,136,],[100,100,]),'mulop':([61,137,],[110,110,]),'marker_while':([80,],[120,]),'actual_parameter_list':([85,],[123,]),'actual_parameter':([85,144,],[124,159,]),'type_denoter':([88,],[128,]),'result_type':([94,147,],[132,162,]),'formal_parameter_list':([95,],[133,]),'marker_for_branching':([98,],[135,]),'initial_value':([121,],[141,]),'formal_parameter_section_list':([134,],[148,]),'formal_parameter_section':([134,164,],[149,170,]),'value_parameter_specification':([134,164,],[150,150,]),'variable_parameter_specification':([134,164,],[151,151,]),'direction':([141,],[157,]),'final_value':([157,],[167,]),'marker_for_for_branching':([167,],[173,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('sign -> +','sign',1,'p_sign_1','parser.py',7),
  ('sign -> -','sign',1,'p_sign_2','parser.py',11),
  ('non_string -> DIGITSEQ','non_string',1,'p_non_string_1','parser.py',15),
  ('identifier_list -> identifier_list comma identifier','identifier_list',3,'p_identifier_list_1','parser.py',19),
  ('identifier_list -> identifier','identifier_list',1,'p_identifier_list_2','parser.py',24),
  ('constant -> non_string','constant',1,'p_constant_1','parser.py',29),
  ('constant -> sign non_string','constant',2,'p_constant_2','parser.py',33),
  ('type_definition_list -> type_definition_list type_definition','type_definition_list',2,'p_type_definition_list_1','parser.py',39),
  ('type_definition_list -> type_definition','type_definition_list',1,'p_type_definition_list_2','parser.py',42),
  ('type_definition -> identifier = type_denoter semicolon','type_definition',4,'p_type_definition_1','parser.py',45),
  ('type_denoter -> identifier','type_denoter',1,'p_type_denoter_1','parser.py',48),
  ('component_type -> identifier','component_type',1,'p_component_type_1','parser.py',58),
  ('domain_type -> identifier','domain_type',1,'p_domain_type_1','parser.py',68),
  ('variable_declaration_part -> RESERVED_VAR variable_declaration_list semicolon','variable_declaration_part',3,'p_variable_declaration_part_1','parser.py',71),
  ('variable_declaration -> identifier_list COLON type_denoter','variable_declaration',3,'p_variable_declaration_1','parser.py',76),
  ('variable_declaration_list -> variable_declaration_list semicolon variable_declaration','variable_declaration_list',3,'p_variable_declaration_list_1','parser.py',89),
  ('variable_declaration_list -> variable_declaration','variable_declaration_list',1,'p_variable_declaration_list_2','parser.py',97),
  ('procedure_and_function_declaration_part -> function_declaration semicolon','procedure_and_function_declaration_part',2,'p_procedure_and_function_declaration_part_2','parser.py',102),
  ('formal_parameter_section_list -> formal_parameter_section_list semicolon formal_parameter_section','formal_parameter_section_list',3,'p_formal_parameter_section_list_1','parser.py',106),
  ('formal_parameter_section_list -> formal_parameter_section','formal_parameter_section_list',1,'p_formal_parameter_section_list_2','parser.py',119),
  ('formal_parameter_list -> LPAREN formal_parameter_section_list RPAREN','formal_parameter_list',3,'p_formal_parameter_list_1','parser.py',123),
  ('formal_parameter_section -> value_parameter_specification','formal_parameter_section',1,'p_formal_parameter_section_1','parser.py',127),
  ('formal_parameter_section -> variable_parameter_specification','formal_parameter_section',1,'p_formal_parameter_section_2','parser.py',131),
  ('value_parameter_specification -> identifier_list COLON identifier','value_parameter_specification',3,'p_value_parameter_specification_1','parser.py',135),
  ('procedure_block -> block','procedure_block',1,'p_procedure_block_1','parser.py',165),
  ('simple_expression -> term','simple_expression',1,'p_simple_expression_1','parser.py',169),
  ('simple_expression -> simple_expression addop term','simple_expression',3,'p_simple_expression_2','parser.py',173),
  ('function_declaration -> function_identification semicolon function_block','function_declaration',3,'p_function_declaration_2','parser.py',191),
  ('function_declaration -> function_heading semicolon function_block','function_declaration',3,'p_function_declaration_3','parser.py',200),
  ('function_heading -> RESERVED_FUNCTION identifier COLON result_type','function_heading',4,'p_function_heading_1','parser.py',209),
  ('function_heading -> RESERVED_FUNCTION identifier marker_fh formal_parameter_list COLON result_type','function_heading',6,'p_function_heading_2','parser.py',227),
  ('declaration_part_list -> declaration_part_list declaration_entity','declaration_part_list',2,'p_declaration_part_list_1','parser.py',249),
  ('declaration_part_list -> declaration_entity','declaration_part_list',1,'p_declaration_part_list_2','parser.py',257),
  ('marker_fh -> <empty>','marker_fh',0,'p_marker_fh_1','parser.py',262),
  ('primary -> variable_access','primary',1,'p_primary_1','parser.py',277),
  ('primary -> unsigned_constant','primary',1,'p_primary_2','parser.py',281),
  ('primary -> function_designator','primary',1,'p_primary_3','parser.py',285),
  ('result_type -> identifier','result_type',1,'p_result_type_1','parser.py',289),
  ('function_identification -> RESERVED_FUNCTION identifier','function_identification',2,'p_function_identification_1','parser.py',299),
  ('function_block -> block','function_block',1,'p_function_block_1','parser.py',313),
  ('statement_part -> compound_statement','statement_part',1,'p_statement_part_1','parser.py',317),
  ('compound_statement -> RESERVED_BEGIN statement_sequence RESERVED_END','compound_statement',3,'p_compound_statement_1','parser.py',322),
  ('variable_parameter_specification -> RESERVED_VAR identifier_list COLON identifier','variable_parameter_specification',4,'p_variable_parameter_specification_1','parser.py',327),
  ('statement_sequence -> statement_sequence semicolon statement','statement_sequence',3,'p_statement_sequence_1','parser.py',355),
  ('statement_sequence -> statement','statement_sequence',1,'p_statement_sequence_2','parser.py',363),
  ('statement -> open_statement','statement',1,'p_statement_1','parser.py',368),
  ('statement -> closed_statement','statement',1,'p_statement_2','parser.py',373),
  ('open_statement -> non_labeled_open_statement','open_statement',1,'p_open_statement_2','parser.py',378),
  ('closed_statement -> non_labeled_closed_statement','closed_statement',1,'p_closed_statement_2','parser.py',383),
  ('non_labeled_closed_statement -> assignment_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_1','parser.py',388),
  ('non_labeled_closed_statement -> procedure_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_2','parser.py',393),
  ('non_labeled_closed_statement -> compound_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_4','parser.py',398),
  ('non_labeled_closed_statement -> repeat_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_6','parser.py',403),
  ('non_labeled_closed_statement -> closed_while_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_9','parser.py',408),
  ('non_labeled_closed_statement -> closed_for_statement','non_labeled_closed_statement',1,'p_non_labeled_closed_statement_10','parser.py',413),
  ('non_labeled_closed_statement -> <empty>','non_labeled_closed_statement',0,'p_non_labeled_closed_statement_11','parser.py',418),
  ('non_labeled_open_statement -> open_if_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_2','parser.py',423),
  ('non_labeled_open_statement -> open_while_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_3','parser.py',428),
  ('non_labeled_open_statement -> open_for_statement','non_labeled_open_statement',1,'p_non_labeled_open_statement_4','parser.py',433),
  ('repeat_statement -> RESERVED_REPEAT repeat_begin_marker statement_sequence RESERVED_UNTIL boolean_expression','repeat_statement',5,'p_repeat_statement_1','parser.py',438),
  ('repeat_begin_marker -> <empty>','repeat_begin_marker',0,'p_repeat_begin_marker_1','parser.py',447),
  ('open_while_statement -> RESERVED_WHILE boolean_expression marker_while RESERVED_DO open_statement','open_while_statement',5,'p_open_while_statement_1','parser.py',453),
  ('closed_while_statement -> RESERVED_WHILE boolean_expression marker_while RESERVED_DO closed_statement','closed_while_statement',5,'p_closed_while_statement_1','parser.py',462),
  ('marker_while -> <empty>','marker_while',0,'p_marker_while_1','parser.py',471),
  ('open_for_statement -> RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO open_statement','open_for_statement',9,'p_open_for_statement_1','parser.py',476),
  ('closed_for_statement -> RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO closed_statement','closed_for_statement',9,'p_closed_for_statement_1','parser.py',493),
  ('marker_for_for_branching -> <empty>','marker_for_for_branching',0,'p_marker_for_for_branching_1','parser.py',510),
  ('open_if_statement -> RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching statement','open_if_statement',5,'p_open_if_statement_1','parser.py',521),
  ('marker_if_false -> <empty>','marker_if_false',0,'p_marker_if_false_1','parser.py',530),
  ('marker_for_branching -> <empty>','marker_for_branching',0,'p_marker_for_branching_1','parser.py',538),
  ('assignment_statement -> variable_access ASSIGNMENT expression','assignment_statement',3,'p_assignment_statement_1','parser.py',543),
  ('variable_access -> identifier','variable_access',1,'p_variable_access_1','parser.py',562),
  ('index_expression_list -> index_expression_list comma index_expression','index_expression_list',3,'p_index_expression_list_1','parser.py',578),
  ('index_expression_list -> index_expression','index_expression_list',1,'p_index_expression_list_2','parser.py',583),
  ('index_expression -> expression','index_expression',1,'p_index_expression_1','parser.py',588),
  ('procedure_statement -> identifier params','procedure_statement',2,'p_procedure_statement_1','parser.py',592),
  ('procedure_statement -> identifier','procedure_statement',1,'p_procedure_statement_2','parser.py',628),
  ('declaration_entity -> procedure_and_function_declaration_part','declaration_entity',1,'p_declaration_entity_2','parser.py',643),
  ('params -> LPAREN actual_parameter_list RPAREN','params',3,'p_params_1','parser.py',648),
  ('actual_parameter_list -> actual_parameter_list comma actual_parameter','actual_parameter_list',3,'p_actual_parameter_list_1','parser.py',652),
  ('actual_parameter_list -> actual_parameter','actual_parameter_list',1,'p_actual_parameter_list_2','parser.py',662),
  ('actual_parameter -> expression','actual_parameter',1,'p_actual_parameter_1','parser.py',669),
  ('actual_parameter -> expression COLON expression','actual_parameter',3,'p_actual_parameter_2','parser.py',673),
  ('actual_parameter -> expression COLON expression COLON expression','actual_parameter',5,'p_actual_parameter_3','parser.py',676),
  ('control_variable -> identifier','control_variable',1,'p_control_variable_1','parser.py',679),
  ('initial_value -> expression','initial_value',1,'p_initial_value_1','parser.py',691),
  ('direction -> RESERVED_TO','direction',1,'p_direction_1','parser.py',695),
  ('final_value -> expression','final_value',1,'p_final_value_1','parser.py',701),
  ('record_variable_list -> record_variable_list comma variable_access','record_variable_list',3,'p_record_variable_list_1','parser.py',705),
  ('record_variable_list -> variable_access','record_variable_list',1,'p_record_variable_list_2','parser.py',708),
  ('boolean_expression -> expression','boolean_expression',1,'p_boolean_expression_1','parser.py',711),
  ('unsigned_constant -> unsigned_number','unsigned_constant',1,'p_unsigned_constant_1','parser.py',721),
  ('unsigned_constant -> STRING','unsigned_constant',1,'p_unsigned_constant_2','parser.py',727),
  ('block -> declaration_part_list statement_part','block',2,'p_block_1','parser.py',733),
  ('block -> statement_part','block',1,'p_block_2','parser.py',741),
  ('declaration_entity -> variable_declaration_part','declaration_entity',1,'p_declaration_entity_1','parser.py',745),
  ('expression -> simple_expression','expression',1,'p_expression_1','parser.py',750),
  ('expression -> simple_expression relop simple_expression','expression',3,'p_expression_2','parser.py',754),
  ('term -> factor','term',1,'p_term_1','parser.py',767),
  ('term -> term mulop factor','term',3,'p_term_2','parser.py',771),
  ('factor -> sign factor','factor',2,'p_factor_1','parser.py',792),
  ('factor -> exponentiation','factor',1,'p_factor_2','parser.py',803),
  ('exponentiation -> primary','exponentiation',1,'p_exponentiation_1','parser.py',807),
  ('primary -> LPAREN expression RPAREN','primary',3,'p_primary_4','parser.py',811),
  ('primary -> RESERVED_NOT primary','primary',2,'p_primary_5','parser.py',815),
  ('unsigned_number -> unsigned_integer','unsigned_number',1,'p_unsigned_number_1','parser.py',822),
  ('unsigned_number -> unsigned_real','unsigned_number',1,'p_unsigned_number_2','parser.py',826),
  ('unsigned_integer -> DIGITSEQ','unsigned_integer',1,'p_unsigned_integer_1','parser.py',830),
  ('unsigned_real -> REALNUMBER','unsigned_real',1,'p_unsigned_real_1','parser.py',834),
  ('function_designator -> identifier params','function_designator',2,'p_function_designator_1','parser.py',838),
  ('addop -> +','addop',1,'p_addop_1','parser.py',859),
  ('addop -> -','addop',1,'p_addop_2','parser.py',863),
  ('addop -> RESERVED_OR','addop',1,'p_addop_3','parser.py',867),
  ('mulop -> *','mulop',1,'p_mulop_1','parser.py',871),
  ('mulop -> /','mulop',1,'p_mulop_2','parser.py',875),
  ('mulop -> RESERVED_DIV','mulop',1,'p_mulop_3','parser.py',879),
  ('mulop -> RESERVED_MOD','mulop',1,'p_mulop_4','parser.py',883),
  ('mulop -> RESERVED_AND','mulop',1,'p_mulop_5','parser.py',887),
  ('relop -> =','relop',1,'p_relop_1','parser.py',891),
  ('relop -> NOTEQ','relop',1,'p_relop_2','parser.py',895),
  ('relop -> <','relop',1,'p_relop_3','parser.py',899),
  ('relop -> >','relop',1,'p_relop_4','parser.py',903),
  ('relop -> LESSOREQ','relop',1,'p_relop_5','parser.py',907),
  ('relop -> MOREOREQ','relop',1,'p_relop_6','parser.py',911),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier_1','parser.py',915),
  ('identifier -> RESERVED_STRING','identifier',1,'p_identifier_3','parser.py',920),
  ('semicolon -> SEMI_COLON','semicolon',1,'p_semicolon_1','parser.py',925),
  ('comma -> COMMA','comma',1,'p_comma_1','parser.py',928),
  ('program -> program_heading semicolon block DOT','program',4,'p_program_1','parser.py',931),
  ('program_heading -> RESERVED_PROGRAM identifier','program_heading',2,'p_program_heading_1','parser.py',934),
  ('program_heading -> RESERVED_PROGRAM identifier LPAREN identifier_list RPAREN','program_heading',5,'p_program_heading_2','parser.py',937),
]