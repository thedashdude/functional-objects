### SET UP
# To import all required methods and constants, it is suggested that you use

from ObFuncs_ import *

# so that creation of objects is as clear as possible

### PROVIDED METHODS
# Objects can be created with the CreateObject_ function.
# It take two arguments, and an optional third one.
# Arguments:
# 	varis: A dictionary that lists the name of all variables the object should have,
#			and their initial values
# 	funcs: A dictionary that lists the name of all methods the object should have,
#			and a reference to the functions
#	kind: A string that represents the type of object created. Defaults to "Generic"
# 	
# The functions in funcs should take two arguments.
# 	me: The object itself is passed when a method is called. The name "me" is of course
#			just a convention, any name will work
# 	args: A list of arguments. Naming is again just a convention
#
#
# CreateObject_ returns a functional object.


# Classes can be created with the CreateClass_ function.
# It take two arguments, and an optional third one.
# Arguments:
# 	Varis: A dictionary that lists the name of all variables the objects in the 
#			class should have, and their initial values
# 	Funcs: A dictionary that lists the name of all methods the object in the class
#			should have, and a reference to the functions
#	Kind: A string that represents the type of objects created. Defaults to "Generic"
# 	
# Unlike CreateObject_, CreateClass_ doesn't create a functional object.
# Instead, it returns a constructor function, that when called (with no arguments)
# will return an object with the default variables and functions of the class.

# SubClasses can be created with the CreateSubClass_ function.
# It take three arguments, and an optional fourth one.
# Arguments:
#	Class: A class function (created by CreateClass_ or CreateSubClass_) that serves
#			as the parent of the new class
# 	Varis: A dictionary that lists the name of all the new variables the objects in the 
#			class should have, and their initial values. Any variables that share names
#			with variables of the parent class are kept, and used as the new initial
#			value of that variable.
# 	Funcs: A dictionary that lists the name of all new methods the object in the class
#			should have, and a reference to the functions. Same behavior with regard to 
#			conflicts as Varis
#	Kind: A string that represents the type of objects created. Defaults to the Kind of 
#			the parent class.
# 	
# Unlike CreateObject_, CreateSubClass_ doesn't create a functional object.
# Instead, it returns a constructor function, that when called (with no arguments)
# will return an object with the default variables and functions of the class.









### STYLING
# When defining an object, use the constant _DefiningObject in an if statement, so as to
# indent everything used to define the object.
# Before the if, define an empty function with the name of the object, so that the block
# is clearly titled
# An Example:


def MyObject(): pass;
if DefiningObject_:
	def prod(me,args):
		return me(me,'get','x')*me(me,'get','y')
	def hello(me,args):
		return "Hello, " + args[0] + ", my name is " + me(me,'get','name')

	v = {"x":5,"y":3,"name":"MyName"}
	f = {"prod":prod,"hello":hello}

	MyObject = CreateObject_(v,f)


# When defining a class, use the constant _DefiningClass in an if statement.
# Everything is the same otherwise, except all instances of the class should be created
# outside the defining block.
# An Example:

def MyClass(): pass;
if DefiningClass_:
	def prod(me,args):
		return me(me,'get','x')*me(me,'get','y')
	def hello(me,args):
		return "Hello, my name is " + me(me,'get','name')
	def scale(me,args):
		me(me,'set','x', me(me,'get','x')*args[0] )
		me(me,'set','y', me(me,'get','y')*args[0] )
		return 'Scaled!'

	v = {"x":5,"y":3,"name":"MyDefaultName"}
	f = {"prod":prod,"hello":hello,"scale":scale}

	MyClass = CreateClass_(v,f,"MyClass")

MyInstance = MyClass()
MyOtherInstance = MyClass()

# Subclasses are much like classes, except an argument should be placed in the empty 
# function to indicate the parent.
# An Example:

def MySub(MyClass): pass;
if DefiningClass_:
	def poppy(me,args):
		return me(me,'get','pop')*args[0]
	newf = {"poppy":poppy}
	newv = {"pop":9}

	MySubClass = CreateSubClass_(MyClass,newv,newf,"MySub")

MySub = MySubClass()
MyOtherSub = MySubClass()




### USING OBJECTS
# All functionality of a functional object is achieved through calling it.
# Calling a functional object takes a different number arguments depending on what 
# you are doing, but the first argument is always the object itself.

MyObject(MyObject, '...')

# The next argument is a string, either 'get', 'set', 'call', 'dump', or 'kind'
# These can also be written cleaner as constants Get_, Set_, Call_, Dump_, and Kind_. 

## GET
# Requires just one extra argument, a string. This is the name of the variable to return.
print("\n\nGET")


k = MyObject(MyObject, 'get', 'x')
#> 5
print(k)

## SET
# Requires two extra arguments, a name to access, and a value to to asign it.
# Returns the value that it assigned.
print("\n\nSET")


MyObject(MyObject, 'set', 'x', 6)
k = MyObject(MyObject, 'get', 'x')
#> 6
print(k)


## CALL
# Requires one argument, the function to call, and any number of other arguments,
# depending on the requirements of the function being called.
# returns whatever the called function returns.
print("\n\nCALL")

s = MyObject(MyObject, 'call', 'hello', 'My Dude')
#> Hello, My Dude, my name is MyName
print(s)

## DUMP
# No arguments required, returns varis, funcs.
# That is, all the data contained by the object. 
# Little practical uses, good for testing
print("\n\nDUMP")


print(MyObject(MyObject, 'dump'))
#>Lots of stuff.

##KIND
# No other arguments. Returns the type assigned to the object at creation or by its class.
print("\n\nKIND")


print(MyObject(MyObject, 'kind'))
#>Generic
print(MyInstance(MyInstance, 'kind'))
#>MyClass