print("Calculadora de Soma e Subtração Simples")
opcao = int(input("1 - Soma \n2 - Subtração \nEscolha uma opção: "))

if opcao == 1:
    print("Calculadora de Soma Simples")
    a = int(input("Digite o primeiro numero para soma: "))
    b = int(input("Digite o segundo numero para soma: "))
    resultado = a + b
    print(f"Resultado de sua soma:\n {resultado}")

if opcao == 2:
    print("Calculador de Subtração Simples")
    a1 = int(input("Digite o primeiro numero para soma: "))
    b1 = int(input("Digite o segundo numero para soma: "))
    resultado1 = a1 + b1
    print(f"Resultado de sua soma:\n {resultado1}")