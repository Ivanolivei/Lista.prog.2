arquivo = float(input("Qual o tamanho do arquivo para download (em MB)? "))
velocidadeinternet = float(input("Qual a velocidade do link de internet (em Mbps)? "))
velocidademb = velocidadeinternet / 8
segundos = arquivo / velocidademb
min = segundos / 60
print(f"O tempo aproximado de download do arquivo é de {min:.2f} minutos.")