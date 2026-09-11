def soma(): 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}") 

def subtracao():
    num3 = float(input("Digite o primeiro número: "))
    num4 = float(input("Digite o segundo número: "))
    resultado = num3 - num4
    print(f"O resultado da subtração é: {resultado}")

def multiplicacao():    
    num5 = float(input("Digite o primeiro número: "))
    num6 = float(input("Digite o segundo número: "))
    resultado = num5 * num6
    print(f"O resultado da multiplicação é: {resultado}")

def divisao():
    num7 = float(input("Digite o primeiro número: "))
    num8 = float(input("Digite o segundo número: "))
    resultado = num7 / num8
    print(f"O resultado da divisão é: {resultado}")
    if num8 == 0:
        print("Erro: Divisão por zero não é permitida.")
    elif num7 == 0:
            print("Nao tem dividendo para dividir a operação")
        

def pares():
    quantidade = int(input("Digite a quantidade de números pares que deseja exibir: "))
    valor_inicial = 0
    contador = 1
   
    while contador <= quantidade:
         valor_inicial += 2
         print(valor_inicial)
         contador += 1
        
    
    
def impares():
    quantidade = int(input("Digite a quantidade de números pares que deseja exibir: "))
    valor_inicial = -1
    contador = 1
       
    while contador <= quantidade:
            valor_inicial += 2
            print(valor_inicial)
            contador += 1
def somatorio():
    quantidade = int(input("Digite a quantidade de números que deseja somar: "))
    valor_inicial = 0
    contador = 1
    while contador <= quantidade:
        valor_inicial += contador
        contador += 1
    print(f"O somatório de 1 até {quantidade} é: {valor_inicial}")

def fatorial():
    quantidade = int(input("Digite um número para calcular o fatorial: "))
    valor_inicial = 1
    contador = 1
    while contador <= quantidade:
        valor_inicial *= contador
        contador += 1
    print(f"O fatorial de {quantidade} é: {valor_inicial}")
while True:
    print ('Calculadora')
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("0 - Sair")
    print ("5 - Pares")
    print ("6 - Impares")
    print ("7 - Somatório")
    print ("8 - Fatorial")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        soma()

    elif opcao == "2":
        subtracao()

    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()

    elif opcao == "5":
        pares()

    elif opcao == "6":
        impares()

    elif opcao == "7":
        somatorio()

    elif opcao == "8":
        fatorial()

    elif opcao == "0":
        print("Saindo da calculadora...")
        break

    else:
        print("Opção inválida. Tente novamente.")  