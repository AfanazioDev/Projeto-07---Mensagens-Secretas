alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Digite a mensagem: ").lower()

chave = int(input("Digite a chave secreta: "))

mensagemCriptografada = ""

for char in mensagem:

    if char in alfabeto:

        posicao = alfabeto.find(char)

        novaPosicao = (posicao + chave) % 26

        mensagemCriptografada += alfabeto[novaPosicao]

    else:

        mensagemCriptografada += char

print("Mensagem criptografada:", mensagemCriptografada)
