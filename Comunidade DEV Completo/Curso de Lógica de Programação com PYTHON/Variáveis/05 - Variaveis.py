# Variáveis e tipos de dados "básicos"

# Uma variável é um espaço na memória onde armazenamos um valor.

# <nome da var> = <valor>

nome = "Erica"  # variável do tipo string (texto), sempre entre aspas ("" OU '')
idade = 30      # var do tipo inteiro (núm sem casas decimais)
altura = 1.70   # var do tipo float (núm com casas decimais)
dev = True      # var do tipo booleana, valores lógicos (True/False). A primeira letra precisa ser maiúscula o T ou F.


#print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")      # f -> É pra formatar o que estamos escrevando.



# Vamos fazer uma mais interativa onde o usuario entre com os dados.

nome = input("Digite seu nome: ")               # entrada de texto
idade = int(input("Digite sua idade: "))        # entrada de texto convertida pra int
altura = float(input("Digite sua altura: "))    # entrada convertida pra float

print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")


