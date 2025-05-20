# classificador de inteligemcia artificial 
# solicita o nome do sistema de IA
nome_ia = input("informe o nome do sistema de IA")

# solicite a pontuaçao de performance
try:
    pontuacao = float(input("informe a pontuacao de performance (0 a 100): "))

    print(f"\nSistema: {nome_ia}")
    print(f"pontuacao: {pontuacao:.1f}")

    # classificacao baseada na pontuacao 
    if pontuacao < 0:
        print("classificacao: erro: pontuacao invalida! ")
    elif pontuacao <= 39.9:
        print("classificacao: IA em treinamento ")  
        print("continue alimentando os dados para melhorar a performance.") 
    elif pontuacao <= 69.9:
        print("classificacao: IA intermediaria ")
    elif pontuacao <= 89.9:
        print("classificacao: IA otimizada ")
    elif pontuacao <= 100:
        print("classificacao: inteligencia artificial avancada ")
        print("iniciando protocolo de expansao neural...")
    else:
        print("classificacao: erro: IA fora de escala!")
except ValueError:
    print("erro: Entrada invalida! por favor, insira o numero para a pontuacao.")        