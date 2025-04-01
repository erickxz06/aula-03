

n1 = int(input("digite a primeira nota: "))
n2 = int(input("digite a segunda nota: "))
n3 = int(input("digite a terceira nota: "))
n4 = int(input("digite a quarta nota: "))

media = (n1 + n2 + n3 + n4)/4

if media >=6:
    print(f"nota: {media} aluno aprovado")

else:
    print(f"nota: {media} aluno reprovado")