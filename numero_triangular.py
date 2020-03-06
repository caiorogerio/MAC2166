'''
Programa que le um inteiro positivo n e imprime uma mensagem 
indicando se ele eh ou nao triangular
'''

print("Determina se um numero n eh triagular\n")

# leia o valor de n
n = int(input("Digite o valor de n: "))

i = 1
while i * (i + 1) * (i + 2) < n:
    i = i + 1

if i * (i + 1) * (i + 2) == n:
    print("%d eh o produto %d*%d*%d" % (n, i, i+1, i+2))
else:
    print("%d nao eh triagular" % (n))
