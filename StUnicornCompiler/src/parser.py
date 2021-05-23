import ply.yacc as yacc
from lexer import lexer, tokens
import symTab
from code_gen import *

def p_sign_1(p):
	'''sign :  '+' '''
	p[0] = {'name': p[1]}

def p_sign_2(p):
	'''sign :  '-' '''
	p[0] = {'name' : p[1]}

def p_non_string_1(p):
	'non_string :  DIGITSEQ'
	p[0] = {'value':p[1],'type':'integer'}

def p_identifier_list_1(p):
	'identifier_list :  identifier_list comma identifier'
	p[0] = {}
	p[0]['list_id'] = p[1]['list_id'] + [p[3]['name']]

def p_identifier_list_2(p):
	'identifier_list :  identifier'
	p[0] = {}
	p[0]['list_id'] = [p[1]['name']]

def p_constant_1(p):
	'constant :  non_string'
	p[0] = p[1]

def p_constant_2(p):
	'constant :  sign non_string'
	p[0] = p[1]
	if p[1]['name'] == '-' :
		p[0]['value'] = -1*p[0]['value']

def p_type_definition_list_1(p):
	'type_definition_list :  type_definition_list type_definition'

def p_type_definition_list_2(p):
	'type_definition_list :  type_definition'

def p_type_definition_1(p):
	'''type_definition :  identifier '=' type_denoter semicolon'''

def p_type_denoter_1(p):
	'type_denoter :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = p[1]['name']
		p[0]['width'] = st_entry['width']

def p_component_type_1(p):
	'component_type :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
	else:
		p[0]['type'] = p[1]['name']
		p[0]['width'] = st_entry['width']

def p_domain_type_1(p):
	'domain_type :  identifier'

def p_variable_declaration_part_1(p):
	'variable_declaration_part :  RESERVED_VAR variable_declaration_list semicolon'
	p[0] = {}
	p[0]['type'] = p[2]['type']

def p_variable_declaration_1(p):
	'variable_declaration :  identifier_list COLON type_denoter'
	p[0] = {}
	for iden in p[1]['list_id']:
		st_entry = S_TABLE.currentScope.search_up(name=iden)
		if st_entry is not None:
			throw_error("Variable redeclaration")
			p[0]['type'] = 'ERROR'
		else:
			st_entry = S_TABLE.currentScope.get_identificator(name=iden)
			S_TABLE.currentScope.re_get_identificator(name=iden,id_dict={'type':p[3]['type'],'t_name':S_TABLE.create_temporarly(name=iden,typ=p[3]['type'],width=p[3]['width'],id_path=st_entry)})
			p[0]['type'] = 'VOID'

def p_variable_declaration_list_1(p):
	'variable_declaration_list :    variable_declaration_list semicolon variable_declaration'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_variable_declaration_list_2(p):
	'variable_declaration_list :  variable_declaration'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_procedure_and_function_declaration_part_2(p):
	'procedure_and_function_declaration_part :  function_declaration semicolon'
	p[0] = p[1]

def p_formal_parameter_section_list_1(p):
	'formal_parameter_section_list :  formal_parameter_section_list semicolon formal_parameter_section'
	p[0] = {}
	p[0]['type_list'] = p[1]['type_list'] + p[3]['type_list']
	p[0]['arg_type_list'] = p[1]['arg_type_list'] + p[3]['arg_type_list']
	p[0]['width'] = p[1]['width'] + p[3]['width']
	p[0]['arg_temp_list'] = p[1]['arg_temp_list'] + p[3]['arg_temp_list']

	if p[1]['type'] ==  'ERROR' or p[3]['type'] ==  'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_formal_parameter_section_list_2(p):
	'formal_parameter_section_list :  formal_parameter_section'
	p[0] = p[1]

def p_formal_parameter_list_1(p):
	'formal_parameter_list :  LPAREN formal_parameter_section_list RPAREN'
	p[0] = p[2]

def p_formal_parameter_section_1(p):
	'formal_parameter_section :  value_parameter_specification'
	p[0] = p[1]

def p_formal_parameter_section_2(p):
	'formal_parameter_section :  variable_parameter_specification'
	p[0] = p[1]

def p_value_parameter_specification_1(p):
	'value_parameter_specification :  identifier_list COLON identifier'
	p[0] = {}
	p[0]['type_list'] = []
	p[0]['arg_type_list'] = []
	p[0]['arg_temp_list'] = []
	p[0]['width'] = 0
	st_entry = S_TABLE.currentScope.search_up(name=p[3]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined - in value_parameter_specification")
		P[0]['type'] = 'ERROR'
		return
	else:
		p[0]['type'] = 'VOID'
		type_width = st_entry['width']
		for iden in p[1]['list_id']:
			st_entry = S_TABLE.currentScope.search_up(name=iden)
			if st_entry is not None:
				throw_error("Variable redeclaration")
				p[0]['type'] = 'ERROR'
			else:
				st_entry = S_TABLE.currentScope.get_identificator(name=iden)
				nt = S_TABLE.create_temporarly(name=iden,typ=p[3]['name'],width=type_width,id_path=st_entry)
				S_TABLE.currentScope.re_get_identificator(name=iden,id_dict={'type':p[3]['name'],'t_name':nt})
				p[0]['type_list'] = p[0]['type_list'] + [p[3]['name']]
				p[0]['arg_type_list'] = p[0]['arg_type_list'] + ['val']
				p[0]['arg_temp_list'] = p[0]['arg_temp_list'] + [nt]
				p[0]['type'] = 'VOID'
				p[0]['width'] += type_width

def p_procedure_block_1(p):
	'procedure_block :  block'
	p[0] = p[1]

def p_simple_expression_1(p):
	'simple_expression :  term'
	p[0] = p[1]

def p_simple_expression_2(p):
	'simple_expression :  simple_expression addop term'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.create_temporarly()
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" addop-operator"
		throw_error(error_st)
		return
	elif p[2]['name'] == 'or':
		p[0]['type'] = 'integer'
		TAC.create_tac_record(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'int'+p[2]['name'])
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		p[0]['type'] = 'real'
		TAC.create_tac_record(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]), 'real'+p[2]['name'])
	elif p[1]['type'] == 'integer' or p[3]['type'] == 'integer' :
		p[0]['type'] = 'integer'
		TAC.create_tac_record(p[0]['t_name'], temp_integer(p[1]), temp_integer(p[3]), 'int'+p[2]['name'])

def p_function_declaration_2(p):
	'function_declaration :  function_identification semicolon function_block'
	TAC.create_tac_record('','','','FUNC_RETURN')
	S_TABLE.finish_view_range()
	if p[1]['type'] == p[1]['type'] == 'VOID' :
		p[0] = {'type' : 'VOID'}
	else :
		p[0] = {'type' : 'ERROR'}

def p_function_declaration_3(p):
	'function_declaration :  function_heading semicolon function_block'
	TAC.create_tac_record('','','','FUNC_RETURN')
	S_TABLE.finish_view_range()
	if p[1]['type'] == p[1]['type'] == 'VOID' :
		p[0] = {'type' : 'VOID'}
	else :
		p[0] = {'type' : 'ERROR'}

def p_function_heading_1(p):
	'function_heading :  RESERVED_FUNCTION identifier COLON result_type'
	p[0] = {}

	st_entry = S_TABLE.currentScope.search_up(name=p[2]['name'])
	if st_entry is not None:
		throw_error("Variable redeclaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.get_identificator(name=p[2]['name'])
		p[0]['label'] = S_TABLE.create_label()
		S_TABLE.currentScope.re_get_identificator(name=p[2]['name'],id_dict={'type':'function','result_type':p[4]['type'],'label':p[0]['label'],'type_list':[],'arg_type_list':[],'arg_temp_list':[],'t_name':S_TABLE.create_temporarly(name=p[2]['name'],width=0,id_path=st_entry),'param_width':0})
		p[0]['type'] = 'VOID'
		S_TABLE.start_view_range(name=p[2]['name'])
		TAC.create_func_record(p[2]['name'])
		TAC.create_tac_record(p[0]['label'],'','','label')
		TAC.create_tac_record('','','','FUNC_BEGIN')

def p_function_heading_2(p):
	'function_heading :  RESERVED_FUNCTION identifier marker_fh formal_parameter_list COLON result_type'
	p[0] = {}
	p[3]['f_st_entry']['result_type'] = p[6]['type']
	p[3]['f_st_entry']['type'] = 'function'
	p[0]['label'] = S_TABLE.create_label()
	p[3]['f_st_entry']['label'] = p[0]['label']
	p[3]['f_st_entry']['type_list'] = p[4]['type_list']
	p[3]['f_st_entry']['arg_temp_list'] = p[4]['arg_temp_list']
	p[3]['f_st_entry']['arg_type_list'] = p[4]['arg_type_list']
	p[3]['f_st_entry']['t_name'] = S_TABLE.create_temporarly(name=p[2]['name'],typ='function',id_path=p[3]['f_st_entry'],width=4)
	p[3]['f_st_entry']['param_width'] = p[4]['width']
	TAC.create_tac_record(p[0]['label'],'','','label')
	TAC.create_tac_record('','','','FUNC_BEGIN')
	if p[6]['type'] == 'ERROR' :
		p[0]['type'] = 'ERROR'
		return
	if p[3]['type'] == p[4]['type'] == 'VOID' :
		p[0]['type'] = 'VOID'
	else:
		p[0]['type'] = 'ERROR'

def p_declaration_part_list_1(p):
	'declaration_part_list :  declaration_part_list declaration_entity'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[2]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_declaration_part_list_2(p):
	'declaration_part_list :  declaration_entity'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_marker_fh_1(p):
	'marker_fh :'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[-1]['name'])
	if st_entry is not None:
		throw_error("Variable redeclaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.get_identificator(name=p[-1]['name'])
		p[0]['type'] = 'VOID'
		p[0]['f_st_entry'] = st_entry
		S_TABLE.start_view_range(name=p[-1]['name'])
		TAC.create_func_record(p[-1]['name'])
		TAC.create_tac_record('','','','FUNC_BEGIN')

def p_primary_1(p):
	'primary :  variable_access'
	p[0] = p[1]

def p_primary_2(p):
	'primary :  unsigned_constant'
	p[0] = p[1]

def p_primary_3(p):
	'primary :  function_designator'
	p[0] = p[1]

def p_result_type_1(p):
	'result_type :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[1]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined")
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = p[1]['name']

def p_function_identification_1(p):
	'function_identification :  RESERVED_FUNCTION identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[2]['name'])
	if st_entry is not None:
		throw_error("Variable redeclaration")
		p[0]['type'] = 'ERROR'
	else:
		st_entry = S_TABLE.currentScope.get_identificator(name=p[2]['name'])
		S_TABLE.currentScope.re_get_identificator(name=p[2]['name'],id_dict={'type':'function','result_type': 'VOID','type_list':[],'t_name':S_TABLE.create_temporarly(name=p[2]['name'],typ='function',id_path=st_entry,width=0),'param_width':0})
		p[0]['type'] = 'VOID'
		S_TABLE.start_view_range(name=p[2]['name'])
		TAC.create_func_record(paramsp[2]['name'])

def p_function_block_1(p):
	'function_block :  block'
	p[0] = p[1]

def p_statement_part_1(p):
	'statement_part :  compound_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_compound_statement_1(p):
	'compound_statement :  RESERVED_BEGIN statement_sequence RESERVED_END'
	p[0] = {}
	p[0]['type'] = p[2]['type']

def p_variable_parameter_specification_1(p):
	'variable_parameter_specification :  RESERVED_VAR identifier_list COLON identifier'
	p[0] = {}
	p[0]['type_list'] = []
	p[0]['arg_type_list'] = []
	p[0]['arg_temp_list'] = []
	p[0]['width'] = 0
	st_entry = S_TABLE.currentScope.search_up(name=p[4]['name'])
	if st_entry['type'] != 'typedef':
		throw_error("Type not defined - in variable_parameter_specification")
	else:
		p[0]['type'] = 'VOID'
		type_width = st_entry['width']
		for iden in p[2]['list_id']:
			st_entry = S_TABLE.currentScope.search_up(name=iden)
			if st_entry is not None:
				throw_error("Variable redeclaration")
				p[0]['type'] = 'ERROR'
			else:
				st_entry = S_TABLE.currentScope.get_identificator(name=iden)
				nt = S_TABLE.create_temporarly(name=iden,typ=p[3]['name'],width=type_width,id_path=st_entry)
				S_TABLE.currentScope.re_get_identificator(name=iden,id_dict={'type':p[4]['name'],'t_name':nt})
				p[0]['type_list'] = p[0]['type_list'] + [p[4]['name']]
				p[0]['arg_type_list'] = p[0]['arg_type_list'] + ['var']
				p[0]['arg_temp_list'] = p[0]['arg_temp_list'] + [nt]
				p[0]['type'] = 'VOID'
				p[0]['width'] += type_width

def p_statement_sequence_1(p):
	'statement_sequence :  statement_sequence semicolon statement'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_statement_sequence_2(p):
	'statement_sequence :  statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_statement_1(p):
	'statement :  open_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_statement_2(p):
	'statement :  closed_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_open_statement_2(p):
	'open_statement :  non_labeled_open_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_closed_statement_2(p):
	'closed_statement :  non_labeled_closed_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_1(p):
	'non_labeled_closed_statement :  assignment_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_2(p):
	'non_labeled_closed_statement :  procedure_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_4(p):
	'non_labeled_closed_statement :  compound_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_6(p):
	'non_labeled_closed_statement :  repeat_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_9(p):
	'non_labeled_closed_statement :  closed_while_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_10(p):
	'non_labeled_closed_statement :  closed_for_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_closed_statement_11(p):
	'non_labeled_closed_statement : '
	p[0] = {}
	p[0]['type'] = 'VOID'

def p_non_labeled_open_statement_2(p):
	'non_labeled_open_statement :  open_if_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_open_statement_3(p):
	'non_labeled_open_statement :  open_while_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_non_labeled_open_statement_4(p):
	'non_labeled_open_statement :  open_for_statement'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_repeat_statement_1(p):
	'repeat_statement :  RESERVED_REPEAT repeat_begin_marker statement_sequence RESERVED_UNTIL boolean_expression'
	TAC.create_tac_record(p[2]['repeat_begin'],p[5]['t_name'], '','IF_TRUE_GOTO')
	p[0] = {}
	if p[3]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'

def p_repeat_begin_marker_1(p):
	'repeat_begin_marker : '
	p[0] = {}
	p[0]['repeat_begin'] = S_TABLE.create_label()
	TAC.create_tac_record(p[0]['repeat_begin'],'','','label')

def p_open_while_statement_1(p):
	'open_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO open_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
	TAC.create_tac_record(p[2]['false'],'','','label')

def p_closed_while_statement_1(p):
	'closed_while_statement :  RESERVED_WHILE boolean_expression marker_while RESERVED_DO closed_statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
	TAC.create_tac_record(p[2]['false'],'','','label')

def p_marker_while_1(p):
	'marker_while :'
	p[0] = {}
	TAC.create_tac_record(p[-1]['false'],p[-1]['t_name'],'','IF_FALSE_GOTO')

def p_open_for_statement_1(p):
	'open_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO open_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' :
			if p[8]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				TAC.create_tac_record(p[2]['t_name'], p[2]['t_name'], 1,'int'+p[5]['control_op'])
				TAC.create_tac_record(p[7]['cond_chek_label'],'','','GOTO')
				TAC.create_tac_record(p[7]['for_end'],'','','label')
				return
		else :
			throw_error('count variables in for loop should be integer type')
	else:
		throw_error('type mismatch')
	p[0]['type'] = 'ERROR'

def p_closed_for_statement_1(p):
	'closed_for_statement :  RESERVED_FOR control_variable ASSIGNMENT initial_value direction final_value marker_for_for_branching RESERVED_DO closed_statement'
	p[0] = {}
	if p[2]['type'] == p[4]['type'] == p[6]['type'] :
		if p[2]['type'].lower() == 'integer' :
			if p[9]['type'] == 'VOID' :
				p[0]['type'] = 'VOID'
				TAC.create_tac_record(p[2]['t_name'], p[2]['t_name'], 1,'int'+p[5]['control_op'])
				TAC.create_tac_record(p[7]['cond_chek_label'],'','','GOTO')
				TAC.create_tac_record(p[7]['for_end'],'','','label')
				return
		else :
			throw_error('count variables in for loop should be integer type')
	else:
		throw_error('type mismatch')
	p[0]['type'] = 'ERROR'

def p_marker_for_for_branching_1(p):
	'marker_for_for_branching : '
	p[0] = {}
	TAC.create_tac_record(p[-5]['t_name'],p[-3]['t_name'],'','int' +p[-4])
	p[0]['cond_chek_label'] = S_TABLE.create_label()
	TAC.create_tac_record(p[0]['cond_chek_label'],'','','label')
	p[0]['bool_temp'] = S_TABLE.create_temporarly(typ='integer')
	TAC.create_tac_record(p[0]['bool_temp'],p[-5]['t_name'],p[-1]['t_name'],p[-2]['relop'])
	p[0]['for_end'] = S_TABLE.create_label()
	TAC.create_tac_record(p[0]['for_end'],p[0]['bool_temp'],'','IF_FALSE_GOTO')

def p_open_if_statement_1(p):
	'open_if_statement :  RESERVED_IF boolean_expression RESERVED_THEN marker_for_branching statement'
	p[0] = {}
	if p[2]['type'] == 'ERROR' or p[5]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'
		TAC.create_tac_record(p[2]['false'],'','','label')

def p_marker_if_false_1(p):
	'marker_if_false :'
	p[0] = {}
	p[0]['t_name'] = p[-5]['false']
	p[0]['if_end'] = S_TABLE.create_label()
	TAC.create_tac_record(p[0]['if_end'],'','','GOTO')
	TAC.create_tac_record(p[0]['t_name'],'','','label')

def p_marker_for_branching_1(p):
	'marker_for_branching :'
	p[0] = {}
	TAC.create_tac_record(p[-2]['false'],p[-2]['t_name'],'','IF_FALSE_GOTO')

def p_assignment_statement_1(p):
	'assignment_statement :  variable_access ASSIGNMENT expression'
	p[0] = {}
	if p[1]['type'] == 'function':
		p[1]['type'] = p[1]['result_type']
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
		return
	if (p[1]['type'] != p[3]['type']) :
		if p[1]['type'] == 'real' and p[3]['type'] == 'integer' :
			p[0]['type'] = 'VOID'
			TAC.create_tac_record(p[1]['t_name'],temp_real(p[3]),'','real' +p[2])
		else :
			p[0]['type'] = 'ERROR'
			throw_error("type mis-match during assignment. conversion not possible")
	else:
		p[0]['type'] = 'VOID'
		TAC.create_tac_record(p[1]['t_name'],p[3]['t_name'],'',p[3]['type']+p[2])

def p_variable_access_1(p):
	'variable_access :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[1]['name'])
	if st_entry is None:
		p[0]['type'] = 'ERROR'
		throw_error("Variable not declared")
	elif st_entry['type'] == 'function':
		p[0]['result_type'] = st_entry['result_type']
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']
	else:
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']


def p_index_expression_list_1(p):
	'index_expression_list :  index_expression_list comma index_expression'
	p[0] = {}
	p[0]['list'] = p[1]['list'] + [p[3]]

def p_index_expression_list_2(p):
	'index_expression_list :  index_expression'
	p[0] = {}
	p[0]['list'] = [p[1]]

def p_index_expression_1(p):
	'index_expression :  expression'
	p[0] = p[1]

def p_procedure_statement_1(p):
	'procedure_statement :  identifier params'
	st_entry = S_TABLE.currentScope.search_up(name = p[1]['name'])
	if(st_entry == None) :
		if p[1]['name'].lower() == 'writeln':
			for param_type, param in zip(p[2]['type_list'], p[2]['list']):
				if(param_type == 'integer'):
					TAC.create_tac_record('', param['t_name'],'','WRITE_INT')
				elif(param_type == 'real'):
					TAC.create_tac_record('', param['t_name'],'','WRITE_REAL')
				elif(param_type == 'string'):
					TAC.create_tac_record('', param['t_name'],'','WRITE_STRING')
				else :
					throw_error("Wrong type.")
					p[0] = {'type' : 'ERROR'}
					break
			TAC.create_tac_record('', '', '', 'WRITE_NL')
		else:
			throw_error("procedure is not defined")
			p[0] = {'type' : 'ERROR'}
		if p[0] != {'type' : 'ERROR'} :
			p[0] = {'type' : 'VOID'}
	elif st_entry['type'] != 'procedure' :
		throw_error('this identifier cannot be used as a procedure ')
		p[0] = {'type' : 'ERROR'}
	else :
		p[0] = {'type' : 'VOID','t_name':S_TABLE.create_temporarly(name = p[1]['name'],width=0)}
		if match_list(p[2]['type_list'],st_entry['type_list']) :
			TAC.create_tac_record(p[1]['name'],st_entry['param_width'],'','SET_PARAM_OFFSET_WIDTH')
			for i,param in enumerate(p[2]['list']):
				if(st_entry['arg_type_list'][i] == 'var'):
					TAC.create_tac_record(param['t_name'],'','','PUSH_VAR_PARAMS')
				else:
					TAC.create_tac_record(param['t_name'],'','','PUSH_VAL_PARAMS')
			TAC.create_tac_record(st_entry['label'],'','','CALL_PROCEDURE')

def p_procedure_statement_2(p):
	'procedure_statement :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name=p[1]['name'])
	st_entry = S_TABLE.currentScope.search_up(name = p[1]['name'])
	if(st_entry == None) :
		throw_error("procedure is not defined")
		p[0] = {'type' : 'ERROR'}
	elif st_entry['type'] != 'procedure' :
		throw_error('this identifier cannot be used as a procedure ')
		p[0] = {'type' : 'ERROR'}
	else :
		p[0] = {'type' : 'VOID','t_name':S_TABLE.create_temporarly(name = p[1]['name'],width=0)}
		TAC.create_tac_record(st_entry['label'],'','','CALL_PROCEDURE')

def p_declaration_entity_2(p):
	'declaration_entity :  procedure_and_function_declaration_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_params_1(p):
	'params :  LPAREN actual_parameter_list RPAREN'
	p[0] = p[2]

def p_actual_parameter_list_1(p):
	'actual_parameter_list :  actual_parameter_list comma actual_parameter'
	p[0] = {}
	p[0]['list'] = p[1]['list'] + [p[3]]
	p[0]['type_list'] = p[1]['type_list'] + [p[3]['type']]
	if p[1]['type'] == 'ERROR' or p[3]['type'] == 'ERROR' :
		p[0]['type'] = 'ERROR'
	else :
		p[0]['type'] = 'VOID'

def p_actual_parameter_list_2(p):
	'actual_parameter_list :  actual_parameter'
	p[0] = {}
	p[0]['list'] = [p[1]]
	p[0]['type_list'] = [p[1]['type']]
	p[0]['type'] = p[1]['type']

def p_actual_parameter_1(p):
	'actual_parameter :  expression'
	p[0] = p[1]

def p_actual_parameter_2(p):
	'actual_parameter :  expression COLON expression'

def p_actual_parameter_3(p):
	'actual_parameter :  expression COLON expression COLON expression'

def p_control_variable_1(p):
	'control_variable :  identifier'
	p[0] = {}
	st_entry = S_TABLE.currentScope.search_up(name = p[1]['name'])
	if st_entry == None:
		throw_error('control variable not declared')
		p[0]['type'] = 'ERROR'
		return
	else :
		p[0]['type'] = st_entry['type']
		p[0]['t_name'] = st_entry['t_name']

def p_initial_value_1(p):
	'initial_value :  expression'
	p[0] = p[1]

def p_direction_1(p):
	'direction :  RESERVED_TO'
	p[0] = {}
	p[0]['relop'] = 'int<='
	p[0]['control_op'] = '+'

def p_final_value_1(p):
	'final_value :  expression'
	p[0] = p[1]

def p_record_variable_list_1(p):
	'record_variable_list :  record_variable_list comma variable_access'

def p_record_variable_list_2(p):
	'record_variable_list :  variable_access'

def p_boolean_expression_1(p):
	'boolean_expression :  expression'
	p[0] = {}
	if p[1]['type'] == 'ERROR':
		p[0]['type'] == 'ERROR'
	else :
		p[0] = p[1]
		p[0]['true'] = S_TABLE.create_label()
		p[0]['false'] = S_TABLE.create_label()

def p_unsigned_constant_1(p):
	'unsigned_constant :  unsigned_number'
	p[0] = p[1]
	p[0]['t_name'] = S_TABLE.create_temporarly()
	TAC.create_tac_record(p[0]['t_name'],p[1]['value'],'',p[0]['type']+':=')

def p_unsigned_constant_2(p):
	'unsigned_constant :  STRING'
	p[0] = {'value':p[1],'type':'string'}
	p[0]['t_name'] = S_TABLE.create_temporarly()
	TAC.create_tac_record(p[0]['t_name'],p[1],'','string:=')

def p_block_1(p):
	'block :  declaration_part_list statement_part'
	p[0] = {}
	if p[1]['type'] == 'ERROR' or p[2]['type'] == 'ERROR':
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = 'VOID'

def p_block_2(p):
	'block :  statement_part'
	p[0] = p[1]

def p_declaration_entity_1(p):
	'declaration_entity :  variable_declaration_part'
	p[0] = {}
	p[0]['type'] = p[1]['type']

def p_expression_1(p):
	'expression :  simple_expression'
	p[0] = p[1]

def p_expression_2(p):
	'expression :  simple_expression relop simple_expression'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.create_temporarly()
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" relational-operator"
		throw_error(error_st)
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		TAC.create_tac_record(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]),'real'+p[2]['name'])
	else :
		TAC.create_tac_record(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'int'+p[2]['name'])
	p[0]['type'] = 'integer'

def p_term_1(p):
	'term :  factor'
	p[0] = p[1]

def p_term_2(p):
	'term :  term mulop factor'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.create_temporarly()
	if p[1]['type'] == 'string' or p[3]['type'] == 'string' :
		error_st = "string type cannot be used with "+p[3]['name']+" mulop-operator"
		throw_error(error_st)
		return
	elif p[2]['name'] == 'and' :
		p[0]['type'] = 'integer'
		TAC.create_tac_record(p[0]['t_name'],p[1]['t_name'],p[3]['t_name'],'int'+p[2]['name'])
	elif p[2]['name'] == '/' :
		p[0]['type'] = 'real'
		TAC.create_tac_record(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]),p[2]['name'])
	elif p[1]['type'] == 'real' or p[3]['type'] == 'real' :
		p[0]['type'] = 'real'
		TAC.create_tac_record(p[0]['t_name'], temp_real(p[1]), temp_real(p[3]), 'real'+p[2]['name'])
	elif p[1]['type'] == 'integer' or p[3]['type'] == 'integer' :
		p[0]['type'] = 'integer'
		TAC.create_tac_record(p[0]['t_name'], temp_integer(p[1]), temp_integer(p[3]), 'int'+p[2]['name'])

def p_factor_1(p):
	'factor :  sign factor'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.create_temporarly()
	if p[2]['type'] == 'string' :
		throw_error('string type can\'t be used')
		p[0]['type'] = 'ERROR'
	else:
		p[0]['type'] = p[2]['type']
		TAC.create_tac_record(p[0]['t_name'],0,p[2]['t_name'],p[1]['name'])

def p_factor_2(p):
	'factor :  exponentiation'
	p[0] = p[1]

def p_exponentiation_1(p):
	'exponentiation :  primary'
	p[0] = p[1]

def p_primary_4(p):
	'primary :  LPAREN expression RPAREN'
	p[0] = p[2]

def p_primary_5(p):
	'primary :  RESERVED_NOT primary'
	p[0] = {}
	p[0]['t_name'] = S_TABLE.create_temporarly(typ='integer')
	p[0]['type'] = 'integer'
	TAC.create_tac_record(p[0]['t_name'], p[2]['t_name'], '', 'NOT')

def p_unsigned_number_1(p):
	'unsigned_number :  unsigned_integer'
	p[0] = p[1]

def p_unsigned_number_2(p):
	'unsigned_number :  unsigned_real'
	p[0] = p[1]

def p_unsigned_integer_1(p):
	'unsigned_integer :  DIGITSEQ'
	p[0] = {'value':p[1],'type':'integer'}

def p_unsigned_real_1(p):
	'unsigned_real :  REALNUMBER'
	p[0] = {'value':p[1],'type':'real'}

def p_function_designator_1(p):
	'function_designator :  identifier params'
	st_entry = S_TABLE.currentScope.search_up(name = p[1]['name'])
	if(st_entry == None) :
		throw_error("function is not defined")
		p[0] = {'type' : 'ERROR'}
	elif st_entry['type'] != 'function' :
		throw_error('this identifier cannot be used as a function ')
		p[0] = {'type' : 'ERROR'}
	else :
		rt = S_TABLE.create_temporarly(name = p[1]['name'],width=4,typ='function',id_path=st_entry)
		p[0] = {'type' : st_entry['result_type'],'t_name':rt}
		if match_list(p[2]['type_list'],st_entry['type_list']):
			TAC.create_tac_record(p[1]['name'],st_entry['param_width'],rt,'SET_PARAM_OFFSET_WIDTH')
			for i,param in enumerate(p[2]['list']):
				if(st_entry['arg_type_list'][i] == 'var'):
					TAC.create_tac_record(param['t_name'],'','','PUSH_VAR_PARAMS')
				else:
					TAC.create_tac_record(param['t_name'],'','','PUSH_VAL_PARAMS')
			TAC.create_tac_record(st_entry['label'],'','','CALL_FUNCTION')

def p_addop_1(p):
	'''addop :  '+' '''
	p[0] = {'name':p[1].lower()}

def p_addop_2(p):
	'''addop :  '-' '''
	p[0] = {'name':p[1].lower()}

def p_addop_3(p):
	'addop :  RESERVED_OR'
	p[0] = {'name':p[1].lower()}

def p_mulop_1(p):
	'''mulop :  '*' '''
	p[0] = {'name':p[1].lower()}

def p_mulop_2(p):
	'''mulop :  '/' '''
	p[0] = {'name':p[1].lower()}

def p_mulop_3(p):
	'mulop :  RESERVED_DIV'
	p[0] = {'name':p[1].lower()}

def p_mulop_4(p):
	'mulop :  RESERVED_MOD'
	p[0] = {'name':p[1].lower()}

def p_mulop_5(p):
	'mulop :  RESERVED_AND'
	p[0] = {'name':p[1].lower()}

def p_relop_1(p):
	'''relop :  '=' '''
	p[0] = {'name':p[1]}

def p_relop_2(p):
	'relop :  NOTEQ'
	p[0] = {'name':p[1]}

def p_relop_3(p):
	'''relop :  '<' '''
	p[0] = {'name':p[1]}

def p_relop_4(p):
	'''relop :  '>' '''
	p[0] = {'name':p[1]}

def p_relop_5(p):
	'relop :  LESSOREQ'
	p[0] = {'name':p[1]}

def p_relop_6(p):
	'relop :  MOREOREQ'
	p[0] = {'name':p[1]}

def p_identifier_1(p):
	'identifier :  IDENTIFIER'
	p[0] = {}
	p[0]['name'] = p[1].lower()

def p_identifier_3(p):
	'identifier :  RESERVED_STRING'
	p[0] = {}
	p[0]['name'] = p[1].lower()

def p_semicolon_1(p):
	'semicolon :  SEMI_COLON'

def p_comma_1(p):
	'comma :  COMMA'

def p_program_1(p):
	'program :  program_heading semicolon block DOT'

def p_program_heading_1(p):
	'program_heading :  RESERVED_PROGRAM identifier'

def p_program_heading_2(p):
	'program_heading :  RESERVED_PROGRAM identifier LPAREN identifier_list RPAREN'

def p_error(p):
	if p == None:
		print ("ERROR: Token missing at the end of code")
		return
	else:
		print ("ERROR: Unexpected token \""+str(p.value)+"\" at line no. " + str(p.lineno))
	while True:
		tok = yacc.token()
		if not tok or tok.type == 'SEMI_COLON': break
	yacc.errok()
	return tok

def throw_error(err):
	print ("ERROR: "+err)

def parseProgram(program):
	parser.parse(program, lexer=lexer)

def testYacc(inputFile):
	program = open(inputFile).read()
	parser.parse(program, lexer=lexer, debug=1)

def temp_real(a):
	if a['type'] == 'real':
		return a['t_name']
	elif a['type'] == 'integer':
		temp_t = S_TABLE.create_temporarly(typ='real', width=4)
		TAC.create_tac_record(temp_t, a['t_name'], '', 'INT_TO_REAL')
		return temp_t

	else:
		error_str = "type-conversion from " + a['type'] + "-type to real-type not possible"
		throw_error(error_st)

def temp_integer(a):
	if a['type'] == 'integer':
		return a['t_name']
	else:
		error_str = "type-conversion from " + a['type'] + "-type to real-type not possible"
		throw_error(error_st)


def match_list(list1, list2):
	if (len(list1) != len(list2)):
		return False
	else:
		for i in range(len(list1)):
			if list1[i] != list2[i]:
				return False
	return True

parser = yacc.yacc(start='program')

class ThreeAddrCode:
	def __init__(self,symbol_table):
		self.code = {'root' : []}
		self.quad = {'root' : -1}
		self.n_quad = {'root' : 0}
		self.ST = symbol_table

	def create_tac_record(self,dest,src1,src2,op):
		curr_func = self.ST.currentScope.name
		self.quad[curr_func] = self.n_quad[curr_func]
		self.n_quad[curr_func] += 1
		self.code[curr_func].append([dest,src1,src2,op])

	def create_func_record(self,func_name):
		self.code[func_name] = []
		self.quad[func_name] = -1
		self.n_quad[func_name] = 0

	def print_three_adr_code(self):
		for t in self.code:
			print(t)
			for c in self.code[t]:
				print(c)

if __name__ == "__main__":
	from sys import argv
	filename, inputFile = argv
	debugger = True
	S_TABLE = symTab.SymTable()
	TAC = ThreeAddrCode(S_TABLE)
	testYacc(inputFile)
	print("--------------------")
	print(S_TABLE.print_temp())
	print("--------------------")
	print ("\n#*-*-*-*-*-* generating mips code : *-*-*-*-*-*\n")
	mips_instr_generator(TAC,S_TABLE)
