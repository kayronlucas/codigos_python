'''

Proposta: Crie um programa que receba o valor de uma compra e a quantidade de parcelas
desejadas (somente de 1 a 24). O programa deve calcular o valor da parcela,
aplicando juros de 1.5% no valor total se o número de parcelas for maior que 12,
deverá ser acrescentado um valor de R$6 para cada parcela que passar de 12x.
Exiba o valor total a ser pago e o valor de cada parcela.

'''

# 1ª Solicitando a entrada do usuário
valor_compra = float(input("Digite o valor da compra: R$"))
num_parcelas = int(input("Digite o número de parcelas desejadas (de 1 a 24): "))

# 2ª Calcula o valor da parcela e o total a ser pago
if num_parcelas < 1 or num_parcelas > 24:
    resultado = "Número de parcelas inválido. Deve ser de 1 a 24."
else:
    juros = 0.015  # 1.5% de juros
    valor_adicional_por_parcela = 6  # Valor adicional para parcelas acima de 12

    if num_parcelas > 12:
        valor_total = valor_compra * (1 + juros)
        valor_parcela = valor_total / num_parcelas + valor_adicional_por_parcela
    else:
        valor_total = valor_compra
        valor_parcela = valor_total / num_parcelas

    resultado = f"Valor total a ser pago: R${valor_total:.2f}\nValor de cada parcela: R${valor_parcela:.2f}"

# 3ª Exibe o resultado
print(resultado)