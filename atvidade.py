# idade_pessoas.py

def contar_maiores_de_idade(idades):
    count = sum(1 for idade in idades if idade >= 18)
    return count

def main():
    idades = []
    print("Digite a idade de 5 pessoas:")

    for i in range(5):
        while True:
            try:
                idade = int(input(f"Idade da pessoa {i+1}: "))
                if idade < 0:
                    raise ValueError("A idade não pode ser negativa.")
                idades.append(idade)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, insira um número inteiro positivo.")

    quantidade_maiores_de_idade = contar_maiores_de_idade(idades)
    print(f"Quantidade de pessoas com 18 anos ou mais: {quantidade_maiores_de_idade}")

if __name__ == "__main__":
    main()