velocidade = float(input("Digite a velocidade do veículo em km/h: "))
limite_velocidade = 60

diferenca_velocidade = velocidade - limite_velocidade

if velocidade > limite_velocidade:
    
    valor_multa = 7 * diferenca_velocidade
    
    print(f"Velocidade excedida em {diferenca_velocidade} km/h.")
    print(f"Valor da multa a ser pago: R$ {valor_multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Sem multa.")
    