nome = None

while True:
    print('Digite o seu nome, ou x para parar')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo, {nome}')
print('até logo')

