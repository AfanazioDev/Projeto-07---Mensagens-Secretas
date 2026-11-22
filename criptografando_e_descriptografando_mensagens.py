alfabeto = "abcdefghijklmnopqrstuvwxyz"

opcao = input("C para criptografar ou D para descriptografar: ").upper()

mensagem = input("Digite sua mensagem: ").lower()

chave = int(input("Digite a chave secreta: "))

resultado = ""

if opcao == "D":
    chave = -chave

for char in mensagem:

    if char in alfabeto:

        posicao = alfabeto.find(char)

        novaPosicao = (posicao + chave) % 26

        resultado += alfabeto[novaPosicao]

    else:

        resultado += char

print("Resultado:", resultado)
