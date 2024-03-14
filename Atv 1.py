class Excecao(Exception):
    pass

try:     
    num = int(input("Digite um numero:"))
    if num %2 == 0:
        print("O numero é par!")
    else:
        raise Excecao("O numero é ímpar!")
           
except Excecao as e:
    print(e)