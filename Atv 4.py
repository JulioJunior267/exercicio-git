class Excecao(Exception):
    pass

try:
    li1 = input("Digite uma palavra: ")
    li2 = input("Digite outra palavra com o mesmo numero de letras: ")

    if len(li1) == len(li2):
        print("Elas tem o mesmo numero de letras!")

    else:
        raise Excecao("Elas tem que possuir o mesmo numero de letras!")
    
except Excecao as e:
    print(e)