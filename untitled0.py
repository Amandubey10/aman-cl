def calc_factorial(num):
    if num==1:
        return 1
    else:
        return(num * calc_factorial(num-1))
num = int(input("Enter number: "))
print("The factorial of" , num, "is" , calc_factorial(num))        