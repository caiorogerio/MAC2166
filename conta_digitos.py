n = int(input("Digite o valor de n(n>0):"))
d = int(input("Digite o valor de d(0<=d<=9):"))

num_salvo = n
conta = 0

while n > 0:
    dig = n % 10
    n = n // 10
    
    if d == dig:
        conta = conta + 1

print("O digito %d aparece %d vezes no numero %d" % (d, conta, num_salvo))
