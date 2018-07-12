from ObFuncs_ import *

## Uncomment the tests below to see functionality of Objects, Classes, and SubClasses


def MyClass(): pass;
if DefiningClass_:
	def prod(me,args):
		return me(me,Get_,'x')*me(me,Get_,'y')
	def hello(me,args):
		return "Hello, my name is " + me(me,Get_,'name')
	def scale(me,args):
		me(me,Set_,'x', me(me,Get_,'x')*args[0] )
		me(me,Set_,'y', me(me,Get_,'y')*args[0] )
		return 'Scaled!'

	v = {"x":5,"y":3,"name":"Obfunc"}
	f = {"prod":prod,"hello":hello,"scale":scale}

	MyClass = CreateClass_(v,f,"MyClass")

def MySub(MyClass): pass;
if DefiningClass_:
	def poppy(me,args):
		return me(me,Get_,'pop')*args[0]
	newf = {"poppy":poppy}
	newv = {"pop":9}

	MySub = CreateSubClass_(MyClass,newv,newf,"MySub")


"""#TEST SUBCLASSES


Obfunc = MyClass()
Obfunc2 = MySub()


print("Get 'x': [5]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [3]")
print(Obfunc(Obfunc,Get_,'y'))
print("Set 'y' to 8: [8]")
print(Obfunc(Obfunc,Set_,'y',8))
print("Get 'y': [8]")
print(Obfunc(Obfunc,Get_,'y'))
print("Call 'prod': [40]")
print(Obfunc(Obfunc,Call_,'prod'))
print("Call 'hello':")
print(Obfunc(Obfunc,Call_,'hello'))
print("Call 'scale':")
print(Obfunc(Obfunc,Call_,'scale',3))
print("Get 'x': [15]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [24]")
print(Obfunc(Obfunc,Get_,'y'))
print("Kind: MyClass")
print(Obfunc(Obfunc,Kind_))
#print("Get 'pop': err")
#print(Obfunc(Obfunc,Get_,'pop'))
#print("Call 'poppy': err")
#print(Obfunc(Obfunc,Call_,'poppy',3))

print("In SubClass:")
print("Get 'x': [5]")
print(Obfunc2(Obfunc2,Get_,'x'))
print("Get 'y': [3]")
print(Obfunc2(Obfunc2,Get_,'y'))
print("Set 'y' to 8: [8]")
print(Obfunc2(Obfunc2,Set_,'y',8))
print("Get 'y': [8]")
print(Obfunc2(Obfunc2,Get_,'y'))
print("Call 'prod': [40]")
print(Obfunc2(Obfunc2,Call_,'prod'))
print("Call 'hello':")
print(Obfunc2(Obfunc2,Call_,'hello'))
print("Call 'scale':")
print(Obfunc2(Obfunc2,Call_,'scale',3))
print("Get 'x': [15]")
print(Obfunc2(Obfunc2,Get_,'x'))
print("Get 'y': [24]")
print(Obfunc2(Obfunc2,Get_,'y'))
print("Get 'pop': [9]")
print(Obfunc2(Obfunc2,Get_,'pop'))
print("Call 'poppy': [18]")
print(Obfunc2(Obfunc2,Call_,'poppy',2))
print("Kind: MySub")
print(Obfunc2(Obfunc2,Kind_))

"""


"""#TEST CLASSES
MyClass = CreateClass_(v,f)
Obfunc = MyClass()
Obfunc2 = MyClass()


print("Get 'x': [5]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [3]")
print(Obfunc(Obfunc,Get_,'y'))
print("Set 'y' to 8: [8]")
print(Obfunc(Obfunc,Set_,'y',8))
print("Get 'y': [8]")
print(Obfunc(Obfunc,Get_,'y'))
print("Call 'prod': [40]")
print(Obfunc(Obfunc,Call_,'prod'))
print("Call 'hello':")
print(Obfunc(Obfunc,Call_,'hello'))
print("Call 'scale':")
print(Obfunc(Obfunc,Call_,'scale',3))
print("Get 'x': [15]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [24]")
print(Obfunc(Obfunc,Get_,'y'))


print("Get 'x' in another object: [5]")
print(Obfunc2(Obfunc2,Get_,'x'))
print("Get 'y' in another object: [3]")
print(Obfunc2(Obfunc2,Get_,'y'))

"""

"""#TEST OBJECTS
Obfunc = CreateObject_(v,f)
Obfunc2 = CreateObject_(v,f)


print("Get 'x': [5]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [3]")
print(Obfunc(Obfunc,Get_,'y'))
print("Set 'y' to 8: [8]")
print(Obfunc(Obfunc,Set_,'y',8))
print("Get 'y': [8]")
print(Obfunc(Obfunc,Get_,'y'))
print("Call 'prod': [40]")
print(Obfunc(Obfunc,Call_,'prod'))
print("Call 'hello':")
print(Obfunc(Obfunc,Call_,'hello'))
print("Call 'scale':")
print(Obfunc(Obfunc,Call_,'scale',3))
print("Get 'x': [15]")
print(Obfunc(Obfunc,Get_,'x'))
print("Get 'y': [24]")
print(Obfunc(Obfunc,Get_,'y'))


print("Get 'x' in another object: [5]")
print(Obfunc2(Obfunc2,Get_,'x'))
print("Get 'y' in another object: [3]")
print(Obfunc2(Obfunc2,Get_,'y'))

"""