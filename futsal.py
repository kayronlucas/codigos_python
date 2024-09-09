# futsal_time.py

def calcular_media(lista):
    """Calcula a média dos valores em uma lista."""
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def main():
    pesos = []
    idades = []
    
    print("Digite o peso e a idade de 5 jogadores:")

    for i in range(5):
        while True:
            try:
                peso = float(input(f"Peso do jogador {i+1} (em kg): "))
                if peso <= 0:
                    raise ValueError("O peso deve ser um valor positivo.")
                idade = int(input(f"Idade do jogador {i+1} (em anos): "))
                if idade <= 0:
                    raise ValueError("A idade deve ser um valor positivo.")
                
                pesos.append(peso)
                idades.append(idade)
                break
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, insira valores válidos.")

    media_peso = calcular_media(pesos)
    media_idade = calcular_media(idades)

    print(f"\nPeso médio do time: {media_peso:.2f} kg")
    print(f"Idade média do time: {media_idade:.2f} anos")

if __name__ == "__main__":
    main()