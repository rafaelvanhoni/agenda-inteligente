from datetime import datetime, date, time

# teste.py
# Arquivo auxiliar para testes e experimentos durante o desenvolvimento do projeto


data = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M")

print(f"Data: {data}\nHora: {hora}")


# opcao = input("teste booleano: ")

# teste = bool(opcao)
# print(teste)

# try:
#     opcao = int(input("Digite uma opção de 1 a 5: "))
#     if 1 <= opcao <= 5:
#         print(f"✅ Opção Selecionada {opcao}")
#     else:
#         print("❌ Opção inválida, digite um numero de 1 a 5")
# except ValueError:
#     print("❌ Você digitou um valor inválido. Digite um número inteiro")