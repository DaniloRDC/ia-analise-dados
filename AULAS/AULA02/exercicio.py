nota1 = float(input("Digite a sua nota primeira: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite a sua nota quarta: "))

notas = [nota1, nota2, nota3, nota4]

mediaNotas = sum(notas) / len(notas)

print(f"Sua maior nota é {max(notas)}")
print(f"Sua menor nota é {min(notas)}")
print(f"A soma de suas notas é {sum(notas)}")
print(f"A sua média é {mediaNotas}")

if mediaNotas >= 6:
    print("Você está aprovado!")
else:
    print("Você foi reprovado!")
