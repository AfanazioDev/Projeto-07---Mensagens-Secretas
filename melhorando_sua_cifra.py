alfabeto = "qwertyuiopasdfghjklzxcvbnm"

mensagem = input("Digite sua mensagem: ").lower()

chave = int(input("Digite a chave secreta: "))

resultado = ""

for char in mensagem:

    if char in alfabeto:

        posicao = alfabeto.find(char)

        novaPosicao = (posicao + chave) % 26

        resultado += alfabeto[novaPosicao]

        chave += 1

print("Mensagem criptografada:", resultado)
