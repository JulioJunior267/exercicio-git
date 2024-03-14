class Excecao(Exception):
    pass

try:
        numero = int(input("Digite um número inteiro: "))
        if numero >0:
            print("O número dividido por 10 é:", numero / 10)
        else:
            raise Excecao("O número nao pode ser 0.")

except Excecao as e:
    print(e)