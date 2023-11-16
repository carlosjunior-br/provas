def AdicionarAluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número da matricula do aluno: ")
    alunos[matricula] = nome
    print()
    print("Aluno adicionado com sucesso!")

def RemoverAluno(alunos):
    matricula = input("Digite o número da matricula do aluno: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print()
        print("Aluno removido com sucesso!")
    else:
        print()
        print("Aluno não encontrado!")
    
def AtualizarAluno(alunos):
    matricula = input("Digite o número da matricula do aluno: ")
    if matricula in alunos:
        nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = nome
        print()
        print("Aluno atualizado com sucesso!")
    else:
        print()
        print("Aluno não encontrado!")

def VerAlunos(alunos):
    print("Lista de Alunos:", end="\n\n")
    for matricula, nome in alunos.items():
        print("Matrícula:", matricula)
        print("Nome:", nome)
        print("-"*30)
    print()
    print("Alunos listados com sucesso!")