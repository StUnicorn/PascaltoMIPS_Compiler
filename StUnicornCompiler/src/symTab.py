class SymTable:
	def __init__(self):
		self.currentScope = Scope(parent=None,name='root')
		self.temp_var_count = 0;
		self.label_count = 0;
		self.scope_list = {'root':self.currentScope}

	def show_me_func_entrypoint(self,scope):
		if scope.name != 'root':
			parent = scope.parentScope
			return parent.EntryList[scope.name]
		else :
			return None

	def create_temporarly(self,id_path={},typ='',width=4,name=''):
		self.temp_var_count += 1
		name2 = "t" + str(self.temp_var_count)
		self.currentScope.get_temporarly(name2,typ,width,name,id_path)
		return name2

	def create_label(self):
		self.label_count += 1
		return "label_" + str(self.label_count)

	def start_view_range(self,name):
		self.currentScope = Scope(parent=self.currentScope,name=name)
		self.scope_list[name] = self.currentScope

	def finish_view_range(self):
		self.currentScope = self.currentScope.parentScope

	def print_temp(self):
		for sc_name in self.scope_list:
			print(sc_name)
			print(self.scope_list[sc_name].tempList)

class Scope:
	def __init__(self,parent,name):
		self.EntryList = {'integer':{'type':'typedef', 'width': 4},
							'real':{'type':'typedef', 'width': 4},
							'string':{'type':'typedef', 'width': 4}
						}
		self.tempList = {}
		self.width = 0
		self.num_entries = 0
		self.parentScope = parent
		self.name = name

	def search_up(self,name):
		scope = self
		while(scope is not None):
			if name in scope.EntryList:
				return scope.EntryList[name]
			else:
				scope = scope.parentScope
		return None

	def get_identificator(self,name):
		self.EntryList[name] = {}
		self.num_entries += 1
		self.EntryList[name]['name'] = name
		return self.EntryList[name]

	def re_get_identificator(self,name,id_dict):
		req_id_dict = self.search_up(name=name)
		if req_id_dict is None:
			print( "Can't update, identifier didn't exist")
		else:
			for id_key in id_dict:
				req_id_dict[id_key] = id_dict[id_key]

	def get_temporarly(self,name,typ,width,variable_name,id_path):
		self.tempList[name] = {'offset':self.width,'width':width,'type':typ,'variable_name':variable_name,'id_path':id_path}
		self.width += width
		self.tempList[name]['name'] = name
		return self.tempList[name]