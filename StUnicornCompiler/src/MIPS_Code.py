class MIPS_Code(object):
	def __init__(self, TAC, symTab):
		self.TAC = TAC
		self.symTab = symTab
		self.code = {}
		self.data = []
		self.currFunc = ''
		self.register_descriptor = {
		'$t0' : None, '$t1' : None, '$t2' : None, '$t3' : None, '$t4' : None, '$t5' : None, '$t6' : None, '$t7' : None,
		'$t8' : None, '$t9' : None,
		'$s0' : None, '$s1' : None, '$s2' : None, '$s3' : None, '$s4' : None,'$s5' : None, '$s6' : None, '$s7' : None
		}
		self.free_regs = [register  for register in self.register_descriptor]
		self.busy_regs = []

	def return_register(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def return_register_address(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		self.create_new_line(['addi',reg,'$sp',curr_temp_details['offset']])
		return reg

	def create_new_data_record(self,temp,data):
		self.data += [temp + data]

	def create_new_line(self,line):
		self.code[self.currFunc] += [line]

	def return_register_for_function_temporarly(self,temp,arg_num,func_name):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[func_name].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def return_register_argument(self,temp,arg_num):
		reg = '$t'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['lw',reg, str(curr_temp_details['offset'])+'($fp)' ,''])
		return reg

	def return_value_address(self,func_name,ret_temp):
		curr_func_details = self.symTab.scope_list[func_name]
		ret_temp_details = curr_func_details.tempList[ret_temp]
		self.clear_register('$t0')
		self.create_new_line(['addi','$t0','$fp',ret_temp_details['offset']])
		self.create_new_line(['sw','$t0','-12($fp)',''])

	def assing_temporarly_into_register(self, temp, reg):
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['lw',reg, str(curr_temp_details['offset'])+'($sp)' ,''])

	def create_new_function(self,f_n):
		self.code[f_n] = []
		self.currFunc = f_n

	def return_function_register(self,temp,arg_num):
		reg = '$f'+str(arg_num)
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['l.s',reg, str(curr_temp_details['offset'])+'($sp)' ,''])
		return reg

	def assing_temporarly_into_func_register(self, temp, reg):
		self.register_descriptor[reg] = temp
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[temp]
		curr_temp_details['reg'] = reg
		self.create_new_line(['l.s',reg, str(curr_temp_details['offset'])+'($sp)' ,''])

	def get_assign(self):
		curr_func_details = self.symTab.scope_list[self.currFunc]
		self.create_new_line(['move','$fp','$sp',''])

	def clear_func_register(self,reg):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		self.create_new_line(['s.s',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def clear_register_func_name(self,reg,func_name):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[func_name].tempList[self.register_descriptor[reg]]
		self.create_new_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def return_function_handler(self,func_name):
		curr_func_details = self.symTab.scope_list[func_name]
		curr_func_entry_list = self.symTab.show_me_func_entrypoint(curr_func_details)
		self.clear_register('$t1')
		r1 = self.return_register(curr_func_entry_list['t_name'],1)
		self.clear_register('$t0')
		self.create_new_line(['lw','$t0','-12($fp)',''])
		self.create_new_line(['sw',r1,'0($t0)',''])
		self.create_new_line(['lw','$ra','-8($fp)',''])
		self.create_new_line(['move','$sp','$fp',''])
		self.create_new_line(['lw','$fp','-4($sp)',''])
		self.create_new_line(['jr','$ra','',''])

	def function_handler_caller(self,callee_name,counter,tac_params,tac_param_type,width,label,ret_temp):
		curr_func_details = self.symTab.scope_list[callee_name]
		self.create_new_line(['sw','$fp','-4($sp)',''])
		self.create_new_line(['move','$fp','$sp',''])
		self.create_new_line(['sub','$sp','$sp',curr_func_details.width+32])
		curr_func_st_entry = self.symTab.show_me_func_entrypoint(curr_func_details)
		self.return_value_address(self.currFunc,ret_temp)
		for i in range(counter):
			r1 = self.return_register_for_function_temporarly(curr_func_st_entry['arg_temp_list'][i],1,callee_name)
			r2 = self.return_register_argument(tac_params[i],2)
			self.create_new_line(['move',r1,r2,''])
			self.clear_register_func_name(r1,callee_name)
		self.create_new_line(['jal',label,'',''])

	def clear_register(self,reg):
		if self.register_descriptor[reg] is None:
			return
		curr_temp_details = self.symTab.scope_list[self.currFunc].tempList[self.register_descriptor[reg]]
		self.create_new_line(['sw',reg,  str(curr_temp_details['offset'])+'($sp)' ,''])
		self.register_descriptor[reg] = None

	def comms(self, str) :
		annotate = True
		if annotate :
			self.create_new_line(['#', str, '', ''])

	def write_mips_code(self):
		print_str =  '.text'+'\n'
		for func in self.symTab.scope_list:
			if func == 'root':
				print_str += 'main:'+'\n'
			for code in self.code[func]:
				print_str += str(code[0]) + ' ' + str(code[1]) + ' ' + str(code[2]) + ' ' + str(code[3])+'\n'
				# print code
			if func == 'root':
				print_str += 'li $v0, 10'+'\n'
				print_str += 'syscall'+'\n'
		if len(self.data) > 0:
			print_str += '.data'+'\n'
			for dat in self.data:
				print_str += dat + '\n'
		print (print_str)
		with open('temp.asm', 'w') as f:
			f.write(print_str)
		return	