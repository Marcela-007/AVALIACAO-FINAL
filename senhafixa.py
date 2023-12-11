senha = 2002 #aqui criamos um variavel para guardar o número que desejamos para melhor uso no resto do codigo

senha_informada = int(input('Insira a sua senha: ')) #aqui receberemos a informação que o usuario inserir

while senha_informada != senha: #aqui usamos uma função de loop (while) para que fique em loop perguntando ao usuario a sua senha até que acerte a senha guardada na variavel(senha) 
    print('Senha invalida')
    senha_informada = int(input('Insira a sua senha: '))
print('Acesso permitido') #aqui temos a informação final e é mostrada para o usuario