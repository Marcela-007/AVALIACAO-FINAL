renda = float(input("Insira o valor de sua renda atual: R$ ")) #Essa variável irá receber o valor do salário/renda do usuario

def imposto(a): #Função que irá calcular o imposto de renda
    if a <= 2000:
        print(f'Você está INSETO de taxa')
    elif a > 2000 and a <= 3000:
        imposto8 = (a * 8)/100
        print(f'Sua taxa de imposto é de R${imposto8:.2f}')
    elif a > 3000 and a <= 4500:
        imposto18 = (a * 18)/100
        print(f'sua taxa de imposto é de R${imposto18:.2f}')
    else:
        imposto28 = (a * 28)/100
        print(f'Sua taxa de imposto é de R${imposto28:.2f}') 

imposto(renda) #Retorna a função / Mostra o valor de saída