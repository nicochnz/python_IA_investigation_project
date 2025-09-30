# celsius = float(input("Entrez des degrés Celsius : "))
# fahrenheit = celsius * 9/5 + 32
# print(celsius, "degrés Celsius sont", fahrenheit, "degrés Fahrenheit.")

moyenne = float(input("Quelle est votre moyenne ?"))
if moyenne < 10:
    print("Vous n'avez pas de mention")
elif moyenne < 12:
    print("Vous avez une mention passable")
elif moyenne < 14:
    print("Vous avez une mention assez bien")
elif moyenne < 16:
    print("Vous avez une mention bien")
else:
    print("Vous avez une mention tres bien")

moyenne = float(input("Quelle est votre moyenne ?"))
if moyenne > 10:
    print("Vous avez une mention")
else:
    print("Vous n'avez pas de mention")