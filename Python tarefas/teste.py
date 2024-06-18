area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / 6
litros_necessarios *= 1.1

latas_necessarias = int(litros_necessarios / 18)
if litros_necessarios % 18 != 0:
    latas_necessarias += 1

preco_latas = latas_necessarias * 80.0

galoes_necessarios = int(litros_necessarios / 3.6)
if litros_necessarios % 3.6 != 0:
    galoes_necessarios += 1

preco_galoes = galoes_necessarios * 35.0

latas_para_preco_minimo = int(litros_necessarios // 18)
litros_restantes = litros_necessarios % 18
galoes_para_preco_minimo = int(litros_restantes / 3.6)
if litros_restantes % 3.6 != 0:
    galoes_para_preco_minimo += 1

preco_minimo = (latas_para_preco_minimo * 80.0) + (galoes_para_preco_minimo * 35.0)

print("Quantidade de tinta necessária:")
print(f"Latas de 18 litros: {latas_necessarias}")
print(f"Galões de 3.6 litros: {galoes_necessarios}")
print(f"Mistura de latas e galões para o menor preço: {latas_para_preco_minimo} latas e {galoes_para_preco_minimo} galões")
print()
print("Preço total:")
print(f"Somente latas de 18 litros: R$ {preco_latas:.2f}")
print(f"Somente galões de 3.6 litros: R$ {preco_galoes:.2f}")
print(f"Mistura de latas e galões para o menor preço: R$ {preco_minimo:.2f}")