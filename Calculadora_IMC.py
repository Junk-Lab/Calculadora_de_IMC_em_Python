'''
************   Programa de cálculo de índice de massa corporal usando Python.   ************   

  Idealizado para fazer um cálculo básico de IMC, palavras-chaves usadas "def", "return", 
  "print", "if", "elif", "else", "float" e ".f"
'''
# Regra de negócio

def Calculo(peso, altura):
    IMC = peso / (altura ** 2)
    return IMC
def Mostragem(IMC):
  if IMC < 15.99:
    return "Muito abaixo do peso."
  elif 16.0 <= IMC <18.49:
    return "Abaixo do peso."
  elif 18.50 <= IMC < 24.99:
    return "Regular."
  elif 25.0 <= IMC < 29.99:
    return "Sobrepeso."
  elif 30.0 <= IMC < 34.99:
    return "Obesidade I."
  elif 35.0 <= IMC < 39.99:
    return "Obesidade II."
  else:
    return "Obesidade III (obesidade mórbida)."
   
# Interação do algoritmo 

print()
print("Olá, você está no aplicativo de cálculo de IMC (Índice de massa corporal) \n")
peso = float(input("Digite seu peso em quilogramas 'KG' ex: 00.00 : \n"))
altura = float(input("Digite sua altura em metros 'M' ex: 0.00 : \n"))
imc = Calculo(peso, altura)
resultado = Mostragem(imc)

#Saida de dados

print()
print(f"Peso digitado: {peso:.2f}Kg\n" f"Altura digitada: {altura:.2f}M\n")
print(f"Seu IMC é: {imc:.2f} \n")
print(f"Classificação do IMC: {resultado} \n")
print("Operação finalizada, Obrigado! \n")

# Fim

'''
********************************** Projeto de apresentação **********************************                
  Autor: Richard Torres (JunkLab)
  Data: 05 - 09 - 2023
  Python Versão - 3.11.4 (AMD64)
*********************************************************************************************
'''