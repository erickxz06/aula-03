time1 = input("Nome do primeiro time: ")
time2 = input("Nome do segundo time: ")
gols_time1 = int(input("Quantos gols o primeiro time marcou:"))
gols_time2 = int(input("Quantos gols o segundo time marcou:"))

if gols_time1 == gols_time2:
    print("empate")
else:
    if gols_time1>gols_time2:
        print(f"{time1} Vencedor")
    else:
        print(f"{time2} Vencedor")

