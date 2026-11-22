alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Digite a mensagem criptografada: ").lower()

chave = int(input("Digite a chave secreta: "))

resultado = ""

for char in mensagem:

    if char in alfabeto:

        posicao = alfabeto.find(char)

        resultado += alfabeto[(posicao - chave) % 26]

    else:

        resultado += char

print("Mensagem descriptografada:", resultado)
