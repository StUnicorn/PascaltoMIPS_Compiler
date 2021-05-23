from MIPS_Code import *

def addops(tac, TAC, symTab, M_Code):
	if tac[3] == 'int:=' or tac[3] == 'integer:=':
		r1 = M_Code.return_register(tac[0], 1)
		if type(tac[1]) is str and tac[1][0] == 't':
			r2 = M_Code.return_register(tac[1], 2)
			M_Code.create_new_line(['move', r1, r2, ''])
		else:
			M_Code.create_new_line(['li', r1, tac[1], ''])
		M_Code.clear_register(r1)
	elif tac[3] == 'string:=' and tac[1][0] == '\'':
		M_Code.create_new_data_record(tac[0], ': .asciiz "' + tac[1][1:-1] + '"')
		r1 = M_Code.return_register(tac[0], 1)
		M_Code.create_new_line(['la', r1, tac[0], ''])
		M_Code.clear_register(r1)
	elif tac[3] == 'string:=' and tac[1][0] == 't':
		r1 = M_Code.return_register(tac[0], 1)
		r2 = M_Code.return_register(tac[1], 2)
		M_Code.create_new_line(['move', r1, r2, ''])
		M_Code.clear_register(r1)
	elif tac[3] == 'label':
		M_Code.create_new_line([tac[0], ':', '', ''])
	elif tac[3] == 'int+':
		r1 = M_Code.return_register(tac[0], 1)
		r2 = M_Code.return_register(tac[1], 2)
		if type(tac[2]) is int:
			M_Code.create_new_line(['addi', r1, r2, tac[2]])
		else:
			r3 = M_Code.return_register(tac[2], 3)
			M_Code.create_new_line(['add', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'int-':
		r1 = M_Code.return_register(tac[0], 1)
		r2 = M_Code.return_register(tac[1], 2)
		if type(tac[2]) is int:
			M_Code.create_new_line(['sub', r1, r2, tac[2]])
		else:
			r3 = M_Code.return_register(tac[2], 3)
			M_Code.create_new_line(['sub', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'real+':
		r1 = M_Code.return_function_register(tac[0], 1)
		r2 = M_Code.return_function_register(tac[1], 2)
		if type(tac[2]) is float:
			M_Code.create_new_line(['li.s', '$f30', tac[2]])
			M_Code.create_new_line(['add.s', r1, r2, '$f30'])
		else:
			r3 = M_Code.return_function_register(tac[2], 3)
			M_Code.create_new_line(['add.s', r1, r2, r3])
		M_Code.clear_func_register(r1)
	elif tac[3] == 'real-':
		r1 = M_Code.return_function_register(tac[0], 1)
		r2 = M_Code.return_function_register(tac[1], 2)
		if type(tac[2]) is float:
			M_Code.create_new_line(['li.s', '$f30', tac[2]])
			M_Code.create_new_line(['sub.s', r1, r2, '$f30'])
		else:
			r3 = M_Code.return_function_register(tac[2], 3)
			M_Code.create_new_line(['sub.s', r1, r2, r3])
		M_Code.clear_func_register(r1)
	elif tac[3] == 'intand':
		r1 = M_Code.return_register(tac[0], 1)
		r2 = M_Code.return_register(tac[1], 2)
		r3 = M_Code.return_register(tac[2], 3)
		M_Code.create_new_line(['and', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'intor':
		r1 = M_Code.return_register(tac[0], 1)
		r2 = M_Code.return_register(tac[1], 2)
		r3 = M_Code.return_register(tac[2], 3)
		M_Code.create_new_line(['or', r1, r2, r3])
		M_Code.clear_register(r1)

def mulops(tac,TAC, symTab, M_Code):
	if tac[3] == 'real*':
		r1 = M_Code.return_function_register(tac[0],1)
		r2 = M_Code.return_function_register(tac[1],2)
		if type(tac[2]) is int or type(tac[2]) is float :
			r3 = tac[2]
		else :
			r3 = M_Code.return_function_register(tac[2],3)
		M_Code.create_new_line(['mul.s', r1, r2, r3])
		M_Code.clear_func_register(r1)
	elif tac[3] == 'int*':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		if type(tac[2]) is int :
			r3 = tac[2]
		else :
			r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['mul', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'intdiv' :
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		if type(tac[2]) is int :
			r3 = tac[2]
		else :
			r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['div', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'intmod' :
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		if type(tac[2]) is int :
			r3 = tac[2]
		else :
			r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['rem', r1, r2, r3])
		M_Code.clear_register(r1)
	elif tac[3] == '/' :
		r1 = M_Code.return_function_register(tac[0],1)
		r2 = M_Code.return_function_register(tac[1],2)
		if (type(tac[2]) is float) or (type(tac[2]) is int) :
			r3 = tac[2]
		else :
			r3 = M_Code.return_function_register(tac[2],3)
		M_Code.create_new_line(['div.s', r1, r2, r3])
		M_Code.clear_func_register(r1)

def relops(tac, TAC, symTab, M_Code):
	if tac[3] == 'int<':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['slt',r1,r2,r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'int>':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['slt',r1,r3,r2])
		M_Code.clear_register(r1)
	elif tac[3] == 'int<=':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['sle',r1,r2,r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'real:=' :
		r1 = M_Code.return_function_register(tac[0],1)
		if type(tac[1]) is str:
			r2 = M_Code.return_function_register(tac[1],2)
			M_Code.create_new_line(['mov.s',r1,r2,''])
		else:
			M_Code.create_new_line(['li.s',r1,tac[1],''])
		M_Code.clear_func_register(r1)
	elif tac[3] == 'int>=':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['sle',r1,r3,r2])
		M_Code.clear_register(r1)
	elif tac[3] == 'int=':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['seq',r1,r2,r3])
		M_Code.clear_register(r1)
	elif tac[3] == 'int<>':
		r1 = M_Code.return_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		r3 = M_Code.return_register(tac[2],3)
		M_Code.create_new_line(['sneq',r1,r2,r3])
		M_Code.clear_register(r1)

def change_type(tac, TAC, symTab, M_Code):
	if tac[3] == 'INT_TO_REAL' :
		r1 = M_Code.return_function_register(tac[0],1)
		r2 = M_Code.return_register(tac[1],2)
		M_Code.create_new_line(['mtc1', r2, r1, ''])
		M_Code.create_new_line(['cvt.s.w', r1, r1, ''])
		M_Code.clear_func_register(r1)

def jumps(tac, TAC, symTab, M_Code):
	if tac[3] == 'IF_FALSE_GOTO':
		r1 = M_Code.return_register(tac[1],1)
		M_Code.create_new_line(['beqz',r1,tac[0],''])
	elif tac[3] == 'IF_TRUE_GOTO':
		r1 = M_Code.return_register(tac[1],1)
		M_Code.create_new_line(['bne',r1, '$zero', tac[0]])
	elif tac[3] == 'GOTO':
		M_Code.create_new_line(['j', tac[0],'',''])

def output(tac, TAC, symTab, M_Code):
	if tac[3] == 'WRITE_NL' :
		M_Code.create_new_line(['li', '$v0', '11', ''])
		M_Code.create_new_line(['li', '$a0', '10', ''])
		M_Code.create_new_line(['syscall', '', '', ''])
	elif tac[3] == 'WRITE_INT' :
		M_Code.create_new_line(['li', '$v0', '1', ''])
		M_Code.assing_temporarly_into_register(tac[1], '$a0')
		M_Code.create_new_line(['syscall', '', '', ''])
	elif tac[3] == 'WRITE_REAL' :
		M_Code.create_new_line(['li', '$v0', '2', ''])
		M_Code.assing_temporarly_into_func_register(tac[1], '$f12')
		M_Code.create_new_line(['syscall', '', '', ''])
	elif tac[3] == 'WRITE_STRING' :
		M_Code.create_new_line(['li', '$v0', '4', ''])
		M_Code.assing_temporarly_into_register(tac[1], '$a0')
		M_Code.create_new_line(['syscall', '', '', ''])

def mips_instr_generator(TAC,symTab):
	M_Code = MIPS_Code(TAC,symTab)
	for f_name in TAC.code:
		M_Code.create_new_function(f_name)
		if f_name == 'root':
			M_Code.create_new_line(['sub', '$sp','$sp',120])
			M_Code.get_assign()
		for tac in TAC.code[f_name]:
			M_Code.comms('This is a code func : '+tac[3])
			if tac[3] == 'SET_PARAM_OFFSET_WIDTH':
				calee_name = tac[0]
				counter = 0
				tac_params = []
				tac_param_type = []
				width = tac[1]
				ret_temp = tac[2]
			elif tac[3] == 'PUSH_VAR_PARAMS':
				counter += 1
				tac_param_type += ['var']
				tac_params += [tac[0]]
			elif tac[3] == 'PUSH_VAL_PARAMS':
				tac_param_type += ['val']
				tac_params += [tac[0]]
				counter += 1
			elif tac[3] == 'CALL_FUNCTION':
				M_Code.function_handler_caller(calee_name, counter, tac_params, tac_param_type, width, tac[0], ret_temp)
			elif tac[3] == 'FUNC_RETURN':
				M_Code.return_function_handler(f_name)
			elif tac[3] == 'FUNC_BEGIN':
				M_Code.create_new_line(['sw', '$ra', '-8($fp)', ''])
			else:
				print(tac[3] + " not implemented")
			addops(tac,TAC, symTab, M_Code)
			mulops(tac, TAC, symTab, M_Code)
			relops(tac, TAC, symTab, M_Code)
			jumps(tac, TAC, symTab, M_Code)
			change_type(tac, TAC, symTab, M_Code)
			output(tac, TAC, symTab, M_Code)
			M_Code.comms('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
	M_Code.write_mips_code()




