n = int(input("Digite o numero de alunos:"))

soma = 0
conta = 0

while conta < n:
    nota = float(input("Digite uma nota:"))
    conta = conta + 1
    soma = soma + nota

media = soma / n
print("A media das notas eh:", media)
