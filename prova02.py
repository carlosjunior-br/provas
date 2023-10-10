"""
[PY-A01] Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email
cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente
com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados
antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue
em um loop.
"""
Senha = "123@"                                                          # Senha cadastrada antecipadamente
Email = "aluno@gmail.com"                                               # E-mail cadastrado antecipadamente
Controle = True
while Controle:                                                         # Laço de repetição solicitado na prova
    Recebe_Senha = input("Informe a senha: ")
    print(" ")
    Recebe_Email = input("Informe o e-mail: ")
    print(" ")
    if Recebe_Senha == Senha and Recebe_Email == Email:                 # Estrutura de condição solicitada na prova
        Controle = False
    else:
        print("Os dados informados estão incorretos! Repita a operação.")
        print(" ")
print("Os dados informados estão corretos!")