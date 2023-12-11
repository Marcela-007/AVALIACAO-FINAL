number = [] #Aqui criamos uma lista para adicionamos oa números depois 
p = 0 #Essa variável irá começar a contagem do número informado na variável

for item in range(0,6): #Aqui usamos a função de repetição (range) para repetir n comadas de print
    numero = float(input('insira o número: '))

    if numero > 0: #aqui usamos o if para estabalecer que o número deve ser maior que 0 
        p = p + 1
        number.append(numero)

soma = sum(number) #aqui usamos o sum para somar os números inseridos na lista 
quan = len(number)
media =soma/quan
print(f'{quan} valores positivos.\n{media}') #aqui usamos o print para mostrar a informação ao usuario 

