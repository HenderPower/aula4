nome_digitado = input("Digite o nome: ")
senha_digitada = input("Digite sua senha: ")
senha_cadastrada = "123"
nome_cadastrado = 'Ana'

while senha_digitada != senha_cadastrada or nome_cadastrado != nome_digitado:
    print ("Nome ou Senha incorreto! Tente novamente.")
    nome_digitado = input("Digite o nome: ")
    senha_digitada = input("Digite sua senha: ")
    

print (f"{nome_digitado}, Bem-Vindo ao Sistema...")