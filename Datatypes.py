# integer


a = 5
print("printing the integer", a);

b = 5.5
print("printing the float number", b);

# Integer, Float, Boolean, String, List, Tuple, Dictionary, Sets,

Int_Var = 5
Float_Var = 5.5
String_Var = "This is priya"
Boolean_Var = True
# There are number of points to know about the boolean data type, function and operators checkout in geeks
List_Var = [1, 2, 3, 4]
Tuple_Var = (1, 2, 2, 3)
Set_Var = {1, 2, 3, 4}
Dictionary_Var = {'1': 0, '2': 1, '3': 3}
# printing the above variables
print("Type integer", type(Int_Var), "Type float", type(Float_Var), "Type String", type(String_Var), "Type Boolean",
      type(Boolean_Var), )

# the above statement gives the class type of each variable
print("Type integer", Int_Var, '\n' "Type float", Float_Var, '\n' "Type String", String_Var, '\n' "Type Boolean",
      Boolean_Var)

# Operators using the functions
# Operators are of 7 types
# Arithemetic Operators
add = Int_Var + Float_Var
sub = Int_Var - Float_Var
Mul = Int_Var * Float_Var
Div = Int_Var / Float_Var
print( add, sub,Mul, Div)

# Comparison Operators and this gives the output values of 'true' or 'false'


print( "check if this is equal", Int_Var == add)
print("check if this is not equal" , Int_Var != add)
print("check if this greater number",  Int_Var > add)
print("check if this lesser number",  Int_Var < add)
print("check if this greater or equal number",  Int_Var >= add)
print("check if this lesser or equal number",  Int_Var <= add)

# Assignment Operators
Int_Var += 5
print("Adding the number", Int_Var )
Int_Var -= 6
print("Subtracted the number", Int_Var)
Int_Var /= 2
print("divded the number", Int_Var)
Int_Var *=3
print("Multiplied the number", Int_Var)
Int_Var %= 5
print("the divedend value", Int_Var)
Int_Var **= 2
print("printing the exponential value", Int_Var)

# Bit wise Operators, Logical Operators  https://www.scholarhat.com/tutorial/python/operators-of-python

# Membership Operators : this is used to determine if a give value is part or not part of the collection of values
# 2 types: in and not in
# in returns true id a sequence if the specified value is present in the object
# not in Returns True if a sequence with the specified value is not present in the object

print( " give the value is present in the list ", 1 in List_Var)  # this give the false value

print( " give the value is present in the list ", 10 in List_Var) # this gives the true value

# Membership Operators





