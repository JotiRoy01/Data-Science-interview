In python the variable is called the identifier
```
name = "joti"
```
here the identifier is name.
all identifier allow the 
* . A-Z, a-z
* . digit 0-9 //Don't start the identifier with digit
*  _

### Style Guide
- total_price = 100 -> snake_case <br> 
- totalPrice = 100 -> camelCase  
- TotalPrice = 100 -> PascalCase

### Operator
print(a**b) -> Calculate the power

>> And operator

| Result 1 | v1 | v2  |
|----------|----------|----------|
| T   | T   | T  |
| F   | T   | F  |
|F|F|T|
|F|F|F|

### Function
block of code that perform a specific task 
it has two part 
* defination -> where written the logic what is actually do 
* call -> when it is invoked 
>> Two types of parameters 
1. non default parameter
2. defualt parameter
always first write the no default parameter then default parameter

### Tuples
1. tuples are immutable
2. we cannot create single value tuple. in python, compiler read single value tuple as a expresion.
```
tuple = (1)
```
3. here the tuple act like a integer
4. if we want to create a single value tuple, we have to write two element or extra comma.
```
tuple = (1,)
```
### Method
* instance, class, static  

|instance|class|static|  
|----------|----------|----------| 
|1st parameter->self|1st parameter cls|no compolsary parameter|  
|access the class & instance atrtibute|access class attribute|no access|  
||decorator|decorator|  
||@classmethod|@staticmethod||

### File Operations
* r -> reading [default]
* w -> writing, truncate file first
* x -> creates new & open for writing
* a -> writing & appends at end
* b -> binary mode
* t -> text mode [default]
* plus -> opens disk file for update(r & w)

### JSON Module
>> javasript object notation

|json|python|  
|--------|--------|  
|arrays|list|
|object|dict|
|string|str|
|null|None|