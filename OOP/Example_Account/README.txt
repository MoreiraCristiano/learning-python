__init__()		--> Class constructor

Encapsulation	--> "Hide" an attribute from the client code; The access to the attribute
					is only to the class scope.

					Underscore naming convention: Attributes that start with "_" is for a 
					class internal use.

					@property decorator: a get method that receive the same name of the getted variable
					to allow you access the variable calling: <obj>.<encapsulated_variable>

					@<property_name>.setter decorator : a set method that receive the same name of the setted variable that change the variable value calling: <obj>.<attribute> = <value>
