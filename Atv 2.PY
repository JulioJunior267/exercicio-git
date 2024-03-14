class Maiscula(Exception):
     pass

try:

    palavra = ((input("Digite palavras com letras maiusculas: ")))
    if palavra.isupper():
        print("Certo!")

    else:
        raise Maiscula("Precisa ser maiuscula!")
    
except Maiscula as e:
    print(e)


    