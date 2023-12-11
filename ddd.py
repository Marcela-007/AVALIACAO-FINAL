ddd = int(input('Insira o seu DDD: ')) #Essa variável irá receber o número do DDD do usuario

def estado(a): #Essa função irá comparar o número inserido na variável anterior e mostra o estado correspondente do DDD
    if a == 61:
        print('Brasilia')
    elif a == 71:
        print('salvador')
    elif a == 11:
        print('São Paulo')
    elif a == 21:
        print('Rio de Janeiro')
    elif a == 32:
        print('Juiz de Fora')
    elif a == 19:
        print('Campinas')
    elif a == 27:
        print('Vitoria')
    elif a == 31:
        print('Belo Horizonte')
    else:
        print('DDD não cadastrado')

estado(ddd) #Aqui irá retonar/mostrar o resultado da função anterior