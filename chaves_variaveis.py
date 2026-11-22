alfabeto = "abcdefghijklmnopqrstuvwxyz"

letra = input("Digite uma letra: ").lower()

chave = int(input("Digite a chave secreta: "))

posicao = alfabeto.find(letra)

novaPosicao = (posicao + chave) % 26

letraCriptografada = alfabeto[novaPosicao]

print("Letra criptografada:", letraCriptografada)
