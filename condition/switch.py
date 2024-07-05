"""Make the calculator in the switch statment in the python"""
n1=int(input("Enter the your first number "))
n2=int(input("Enter the your second number"))
match n1,n2:
    case 1:
        print("the addition is the ",n1+n2)
    case 2:
        print("the Subtract",n1-n2)
        