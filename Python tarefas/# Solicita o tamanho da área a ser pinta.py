valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

media = (valor1 * valor2 * valor3) / 3

print("A média aritmética da multiplicação dos três valores é:", media)




############




compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

valor_total = compra1 + compra2 + compra3

if valor_total > 300:
    desconto = 0.20 * valor_total
elif valor_total > 200:
    desconto = 0.15 * valor_total
elif valor_total > 100:
    desconto = 0.10 * valor_total
else:
    desconto = 0

valor_final = valor_total - desconto

print("Valor total das compras: R$", valor_total)
print("Valor do desconto aplicado: R$", desconto)
print("Valor final com desconto: R$", valor_final)



############


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero."

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)



############



altura = float(input("Digite sua altura em metros: "))

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print("Para homens: Peso ideal é", peso_ideal_homem, "kg")
print("Para mulheres: Peso ideal é", peso_ideal_mulher, "kg")




############



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
