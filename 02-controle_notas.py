nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))
pergunta = input("Deseja cadastrar a nota do aluno? (Sim/Nao): ")
contador = 1

while pergunta == 'Sim':
    nota2 = float(input("Digite a nota do aluno: "))
    pergunta = input("Deseja cadastrar a nota do aluno? (Sim/Nao): ")
    contador += 1
    nota = nota + nota2
if nota / contador >= 5:
    print(f"{nome}, você foi aprovado com a média: {nota / contador}")
else:
    print(f"{nome}, você foi reprovado com a média: {nota / contador}")
 


