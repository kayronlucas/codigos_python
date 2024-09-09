#Lê o valor inicial e o valor final
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

#Calcula a soma dos números inteiros no intervalo


soma = 0
for número in range(valor_inicial, valor_final + 1):
    soma += número
#Exibe o resultado
print(f"A soma de todos os números inteiros entre {valor_inicial} e {valor_final} é: {soma}")
