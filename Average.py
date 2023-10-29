nota1 = float(input('Text your first note: '))
nota2 = float(input('Text your second note: '))
nota3 = float(input('Text your third note: '))
media = (nota1 + nota2 + nota3) /3

print("your note is: ", media)

if media >= 6:
    print('congrats, you are aproved')

else:
    print('sorry, you are not aproved')