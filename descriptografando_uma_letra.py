alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = -3

letra = input("Digite uma letra: ").lower()

posicao = alfabeto.find(letra)

novaPosicao = (posicao + chave) % 26

letraDescriptografada = alfabeto[novaPosicao]

print("Sua letra descriptografada é:", letraDescriptografada)
