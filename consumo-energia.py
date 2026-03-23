# Programa de cálculo de consumo de energia

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

#  cálculo de custo, essa calculo é opcional..
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# Saída de dados
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")