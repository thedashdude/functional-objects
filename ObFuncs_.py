import copy

DefiningObject_ = True
DefiningClass_ = True
Get_ = 'get'
Set_ = 'set'
Call_ = 'call'
Dump_ = 'dump'
Kind_ = 'kind'

def CreateObject_(varis,funcs,kind="Generic" ):
	varis = copy.deepcopy(varis)
	funcs = copy.deepcopy(funcs)
	def Object_(me,cmd,name=None,*args):
		if cmd == Get_:
			return varis[name]
		elif cmd == Set_:
			varis[name] = args[0]
			return args[0]
		elif cmd == Call_:
			return funcs[name](me,args)
		elif cmd == Dump_:
			return copy.deepcopy(varis), copy.deepcopy(funcs)
		elif cmd == Kind_:
			return kind
		else:
			return None

	return Object_

def CreateClass_(Varis,Funcs,Kind="Generic" ):
	Varis = copy.deepcopy(Varis)
	Funcs = copy.deepcopy(Funcs)
	def CreateInstance_():
		varis = copy.deepcopy(Varis)
		funcs = copy.deepcopy(Funcs)
		kind = Kind
		def Instance_(me,cmd,name=None,*args):
			if cmd == Get_:
				return varis[name]
			elif cmd == Set_:
				varis[name] = args[0]
				return args[0]
			elif cmd == Call_:
				return funcs[name](me,args)
			elif cmd == Dump_:
				return copy.deepcopy(varis), copy.deepcopy(funcs)
			elif cmd == Kind_:
				return kind
			else:
				return None

		return Instance_

	return CreateInstance_

def CreateSubClass_(Class,Varis,Funcs,Kind = None):
	Temp = Class()
	ClassVaris, ClassFuncs = Temp(Temp,Dump_)
	Varis = copy.deepcopy(Varis)
	Funcs = copy.deepcopy(Funcs)

	if not Kind:
		Kind = Temp(Temp,Kind_)

	for k in ClassVaris:
		if k not in Varis:
			Varis.update({k:ClassVaris[k]})

	for k in ClassFuncs:
		if k not in Funcs:
			Funcs.update({k:ClassFuncs[k]})
	def CreateInstance_():
		varis = copy.deepcopy(Varis)
		funcs = copy.deepcopy(Funcs)
		kind = Kind
		def Instance_(me,cmd,name=None,*args):
			if cmd == Get_:
				return varis[name]
			elif cmd == Set_:
				varis[name] = args[0]
				return args[0]
			elif cmd == Call_:
				return funcs[name](me,args)
			elif cmd == Dump_:
				return copy.deepcopy(varis), copy.deepcopy(funcs)
			elif cmd == Kind_:
				return kind
			else:
				return None

		return Instance_

	return CreateInstance_