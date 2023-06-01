vlrhr = float(input("Digite o valor que você ganha por hora: "))
hrstb = float(input("Digite o número de horas trabalhadas no mês: "))
slrbruto = vlrhr * hrstb
ir = slrbruto * 0.11
inss = slrbruto * 0.08
sindicato = slrbruto * 0.05
slrlqd = slrbruto - ir - inss - sindicato
print("Salário Bruto: R$", slrbruto)
print("Descontos:")
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", slrlqd)