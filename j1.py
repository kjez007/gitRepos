def addition (a,b):
        return a+b
def soustraction (a,b):
        return a-b
def multiplication (a,b):
        return a*b
def division (a,b):
        return a/b
def calculatrice(a,b):
        print("calculatrice")
        print("1-addition")
        print("2-soustraction")
        print("3-multiplication")
        print("4-division")

a = int(input ("saisissez la valeur de a:"))
b = int(input ("saisissez la valeur de b:"))

choix = int(input("saisissez votre choix"))

if choix == 1:
        print("résultat:", addition(a,b))
elif choix == 2:
        print("résultat:", soustraction(a,b))
elif choix == 3:
        print("résultat:", multiplication(a,b))
elif choix == 4:
        print("résultat:", division(a,b))
else:
        print ("non disponible")

calculatrice(a,b)
