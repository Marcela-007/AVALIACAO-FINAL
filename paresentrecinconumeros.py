contador = 0 #Essa variável irá começar a contagem do número informado na variável

for pares in range(0,5): #Essa função irá informar quantas vezes irá repetir o texto abaixo do print
    numero_par = int(input('Insira um valor inteiro: '))
    if numero_par % 2==0: #Aqui ele irá dividir o número que o usuario irá colocar e comparar o seu resto com o número informado que é 0
        contador+=1
print('Você digitou %d valores pares'%contador) #Aqui irá retornar o valor e mostra quais números são pares 

