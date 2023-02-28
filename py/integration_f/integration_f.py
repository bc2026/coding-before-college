import math

general_form = "ax^n + bx^n-1 + cx^n-2 ... + z "
#n is the degree and d is the constant term at the end

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
coefficients = []
degree = int(input("What degree is the polynomial term (26 MAX) ?"))
func = ""

for i in range(degree):
    print("What is the coefficient for ", letters[i])
    coef = float(input())
    coefficients.append(coef)

    if(degree - i == degree):
        func += str(coef) + "x^"+str(degree-i)
    elif (degree - i == 1):
        func += " + " +str(coef)+ "x"
    else:
        func += " + " + str(coef) + "x^"+str(degree-i)
constant = float(input("What is the constant? "))

func += " + " + str(constant)

print(func)


def menu():
    print( "THIS IS AN INTEGRATION PROGRAM. PLEASE ENTER YOUR PREFERREED \nWAY OF APPROXIMATING THE AREA UNDER THE POLYNOMIAL CURVE")
    print("1) LRAM \n 2) RRAM \n 3) MRAM \n 4) TRAPE")

    choice = input()

    try: 
        choice = int(choice)

        if(choice == 1):        lram(x,y,z)
        elif (choice == 2):     rram(x,y,z)
        elif (choice == 3):     mram(x,y,z)
        elif(choice == 4):      trape(x,y,z)
    except TypeError:
        if (choice.lower() == "lram"):      lram(x,y,z)
        elif (choice.lower() == "rram"):    rram(x,y,z)
        elif(choice.lower() == "mram"):     mram(x,y,z)
        elif(choice.lower() == "trape"):    trape(x,y,z)
        
        
        
            # print("do stuff")

def lram() :
def rram() :
def mram() :
def trape():

