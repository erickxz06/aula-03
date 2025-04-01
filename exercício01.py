nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
salario = float(input("digite seu salário aqui: "))
percentual = int(input("digite o aumento do seu salário em percentual: "))
aumento = (salario*percentual)/100
salario_final = salario+aumento

print(f"Seu nome é {nome}, você têm {idade} anos, seu salário antigo é {salario}R$, com aumento de {aumento}, seu novo salário é {salario_final}")