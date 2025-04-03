tipo = input("Digite o tipo de combustível\n"
             "G para gasolina\n"
             "E para etanol\n")
qntdlitros = float(input("Quantos litros: "))

valor_g = 5.8
valor_e = 4.9
if tipo == "g" or tipo =="G":
    valor = qntdlitros * valor_g
    print(f"Você gastou R${valor:.2f}")
else:
    if tipo == "e" or tipo =="E":
        valor = qntdlitros * valor_e
        print(f"Você gastou R${valor:.2f}")
    else:
        print(f"Combustível inválido")
