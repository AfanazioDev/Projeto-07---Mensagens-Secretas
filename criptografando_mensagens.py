alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = 3

letra = input("Digite uma letra: ").lower()

posicao = alfabeto.find(letra)

novaPosicao = (posicao + chave) % 26

letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é:", letraCriptografada)
