nome_aparelho = str(input("Digite o nome do aparelho: "))
potencia = float(input("Potencia do aparelho em watts: "))
horasDia = float(input("tempo de uso em horas: "))
consumo_mensal = round(potencia * horasDia * 30) / 100

print("Aparelho:", nome_aparelho)
print("Consumo estimado:", consumo_mensal, "kWh/mês")
