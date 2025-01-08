from .operacoes import Soma, Subtracao, Multiplicacao, Divisao

def interface():
    print("Bem-vindo à Calculadora!")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Digite o número da operação desejada: ")
        if escolha == "5":
            print("Saindo da calculadora. Até mais!")
            break

        try:
            valor1 = float(input("Digite o primeiro valor: "))
            valor2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Erro: Por favor, insira números válidos.")
            continue

        operacao = None
        if escolha == "1":
            operacao = Soma(valor1, valor2)
        elif escolha == "2":
            operacao = Subtracao(valor1, valor2)
        elif escolha == "3":
            operacao = Multiplicacao(valor1, valor2)
        elif escolha == "4":
            operacao = Divisao(valor1, valor2)
        else:
            print("Opção inválida.")
            continue

        print(f"Resultado: {operacao.calcular()}")