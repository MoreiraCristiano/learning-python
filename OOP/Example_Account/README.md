
# Special methods
	1. __init__(self)		--> Class constructor
	2. __repr__(self)		--> Used to get an string representation of an object like its constructor:
								'Time(hour=6, minute=30, second=0)'
	3. __str__(self)		--> Optional method, usually used to pretty print an object (for reports)
	4. 

# Module __main__	
	1. When load any module, python assigns a string with the modules names to a global attribute called __name__

# Encapsulation	
	1. "Hide" an attribute from the client code; The access to the attribute is only to the class scope.
	2. Underscore naming convention: Attributes that start with "_" is for a class internal use.
	3. @property decorator: a get method that receive the same name of the getted variable to allow you access the variable calling: <obj>.<encapsulated_variable>
	4. @<property_name>.setter decorator : a set method that receive the same name of the setted that change the variable value calling: <obj>.<attribute> = <value>					
	5. Method with name set usually change the value of more than one attribute
					
# Inheritance
	1. A base class may have a subclass(specialization) 
	2. All python class directly or indirectly inherit from an existing Class object
	3. Base classes can have the following declaration: class BaseClass(object)
	4. super(). calls method of base class
	5. Python provides 2 builtin functions issubclass and isinstance for testing "is a" relationships

# Polymorphism
	1. Override original methods of base class
	2. Do not have a special syntax
	3. Operator overloading