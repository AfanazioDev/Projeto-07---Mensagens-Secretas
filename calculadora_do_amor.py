print("CALCULADORA DO AMOR")

nome1 = input("Digite o nome da primeira pessoa: ").lower()

nome2 = input("Digite o nome da segunda pessoa: ").lower()

placar = 0

for char in nome1 + nome2:

    if char in "aeiou":
        placar += 5

    if char in "amor":
        placar += 10

print("Placar de compatibilidade:", placar)

if placar < 10:
    print("Esqueça esta pessoa! Nunca vai dar certo!")

elif placar < 30:
    print("Vocês podem ser bons amigos!")

elif placar < 60:
    print("Existe uma boa possibilidade de relacionamento!")

else:
    print("Vocês têm um relacionamento muito intenso! <3")
