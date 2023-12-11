salario = float(input('Insira o valor de seu salário atual: R$ ')) #Essa variável irá receber o valor do salário do funcionário

def aumento_salario(a):  #Essa função irá calcular o aumento que esse funcionário irá receber
    if a <= 400:
        aumento15 = (a * 15)/100
        salario_novo1 = a + aumento15
        print(f'Novo salário: R${salario_novo1:.2f}')
        print(f'Reajuste ganho: R${aumento15:.2f}')
        print('Em percentual: 15%')
    elif a > 400 and a <= 800:
        aumento12 = (a * 12)/100
        salario_novo2 = a + aumento12
        print(f'Novo salário: R${salario_novo2:.2f}')
        print(f'Reajuste ganho: R${aumento12:.2f}')
        print('Em percentual: 12%')
    elif a > 800 and a <= 1200:
        aumento10 = (a * 10)/100
        salario_novo3 = a +  aumento10
        print(f'Novo salário: R${salario_novo3:.2f}')
        print(f'Reajuste ganho: R${aumento10:.2f}')
        print('Em percentual: 10%')
    elif a > 1200 and a <= 2000:
        aumento7 = (a * 7)/100
        salario_novo4 = a + aumento7
        print(f'Novo salário: R${salario_novo4:.2f}')
        print(f'Reajuste ganho: R${aumento7:.2f}')
        print('Em percentual: 7%')
    else:
        aumento4 = (a * 4)/100
        salario_novo5 = a + aumento4
        print(f'Novo salário: R${salario_novo5:.2f}')
        print(f'Reajuste ganho: R${aumento4:.2f}')
        print('Em percentual: 4%')

    aumento_salario(salario) #Aqui você terá o retorno da função usada anteriormente 