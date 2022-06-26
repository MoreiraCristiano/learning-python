
# Special methods:
	1. __init__(self)		--> Class constructor
	2. __repr__(self)		--> Used to get an string representation of an object

# Encapsulation	
	1. "Hide" an attribute from the client code; The access to the attribute is only to the class scope.
	2. Underscore naming convention: Attributes that start with "_" is for a class internal use.
	3. @property decorator: a get method that receive the same name of the getted variable to allow you access the variable calling: <obj>.<encapsulated_variable>
	4. @<property_name>.setter decorator : a set method that receive the same name of the setted that change the variable value calling: <obj>.<attribute> = <value>					
	5. Method with name set usually change the value of more than one attribute
					

					
