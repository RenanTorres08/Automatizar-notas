
# Função para validar as notas
def validar_notas(nota1, nota2):
    return 0 <= nota1 <= 10 and 0 <= nota2 <= 10


# Função para calcular a média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


# Função para verificar a aprovação
def verificar_aprovacao(media):
    if media >= 5:
        return "Aprovado"
    else:
        return "Reprovado"


# Procedimento para gerar o relatório
def gerar_relatorio(nome, media, situacao):
    print("\n--- RELATÓRIO DO ALUNO ---")
    print(f"Nome: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")


# Entrada da quantidade de alunos
while True:
    try:
        quantidade = int(input("Quantos alunos deseja cadastrar? "))

        if quantidade > 0:
            break

        print("Digite uma quantidade maior que zero.")

    except ValueError:
        print("Digite um número inteiro válido.")


# Lista para armazenar os alunos
alunos = []


# Cadastro dos alunos
for i in range(quantidade):
    print(f"\nCadastro do aluno {i + 1}")

    nome = input("Digite o nome do aluno: ")

    # Entrada e validação das notas
    while True:
        try:
            nota1 = float(input("Digite a primeira nota (0 a 10): "))
            nota2 = float(input("Digite a segunda nota (0 a 10): "))

            if validar_notas(nota1, nota2):
                print("Notas válidas!")
                break

            print("Notas inválidas! Digite valores entre 0 e 10.")

        except ValueError:
            print("Erro! Digite apenas números.")

    # Cálculo da média e situação
    media = calcular_media(nota1, nota2)
    situacao = verificar_aprovacao(media)

    # Armazenamento dos resultados
    aluno = {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    # Relatório individual
    gerar_relatorio(nome, media, situacao)


# Relatório geral da turma
print("\n=== RELATÓRIO GERAL DA TURMA ===")

aprovados = 0
reprovados = 0

for aluno in alunos:
    print(
        f"{aluno['nome']} - "
        f"Média: {aluno['media']:.1f} - "
        f"Situação: {aluno['situacao']}"
    )

    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    else:
        reprovados += 1


# Resumo final
print("\n=== RESUMO FINAL ===")
print(f"Total de alunos: {len(alunos)}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
