''' Hello guys this a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
perform the calculation and display the result.
'''

Value_1= input("INPUT YOUR FIRST NUMBER:-")
Value_2= input("INPUT YOUR SECOND NUMBER:-")



print(''' 
        Press 1 For Addition.
        Press 2 For Subtraction.
        Press 3 For Multiplication.
        Press 4 For Division
         ''')

# you can select any choice from here.....
choice = int(input("Enter your choice (1/2/3/4):-"))

# This choice for Addition of Two Numbers....
if choice==1:
    print("Result:-",int(Value_1)+int(Value_2))

# This choice for Subtraction of two numbers...


elif choice ==2:
    print("Result:-",int(Value_1)-int(Value_2))


# This choice for multiplication of two numbers....
elif choice ==3:
    print("Result:-",int(Value_1)*int(Value_2))

# This choice for divide of Two Numbers.....
elif choice ==4:
    print("Result:-",int(Value_1)/int(Value_2))

# if client select any roungh choice...
else:
    print("!! invailid Input !!:")

