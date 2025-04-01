nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) /3

if media >=7:
    print(f"nota: {media:.1f} aluno aprovado")

else:
    if media <4:
        print(f"nota {media:.1f} aluno reprovado")
    else:
        print(f"nota {media:.1f} aluno em recuperação")