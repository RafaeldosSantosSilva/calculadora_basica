from funcoes import *
# Menu para chamar a função e executar a operação desejada
while True:
    print(''' ----------------------------------------
    Bem vindo a sua calculadora basica. 
Ela é simles mas cumpre suas funções com excelência.
Boa sorte. ''')

    menu = int(input('''Digite sua opção:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair
Digite aqui: '''))
    if menu == 1:
        print(soma())
    elif menu == 2:
        print(subtracao())
    elif menu == 3:
        print(multiplicacao())
    elif menu == 4:
        print(divisao())
    elif menu == 0:
        print('Programa encerrado')
        break
    else:
        print('Digite algo valido')