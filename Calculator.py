n1 = int(input("text your first number: "))
n2 = int(input("Text yout second number: "))
sinal = input("text the equation (+,-,*,/) ")
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2


if sinal == '+':
    print("The result is: ", soma)

elif sinal == '-':
    print("The result is: ", sub)

elif sinal == '*':
    print("The result is: ", mult)

elif sinal == '/':
    print("The result is: ", div)

else:
    print("Is not possible to acomplish this equation") 