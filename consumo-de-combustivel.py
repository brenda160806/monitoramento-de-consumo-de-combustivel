#calculadora de consumo de combustivel

#socite o nome do usuario 
nome= input("ola qual é seu nome")

#entrada de dados 
distancia = float(input("informe a distancia percorrida em (km): "))
litos = float(input("informe a quantidade de conbustivel que foi gasto (em litros)"))

#calculo de consumo medio 
consumo_médio = distancia / litos

# exibe  o resultado de suas decimais 
print(f"\n{nome}, o consumo medio do seu veiculo foi de {consumo_médio:.2f} km/1.")

# classificacao com base no consumo
if consumo_médio < 8.0:
   print("classificaçao: alto consumo " ) 
   print('recomenda-se verificar o motor ou calibrar os pneos. ')
elif 8.0 <= consumo_médio <= 12.0:
    print("classificacao: consumo moderado ")
else:
    print("classificacao: economico! ") 
    