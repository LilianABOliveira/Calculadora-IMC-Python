def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc <18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Acima do Peso"
    else:
        return "Obesidade"
    
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"O seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")