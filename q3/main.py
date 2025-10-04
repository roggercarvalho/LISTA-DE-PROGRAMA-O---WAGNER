# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.


def sistema_autenticador(usuario,senha):
    usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
}

    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
    else:
        print("Usuário ou senha incorretos.")


usuario = input("Usuário: ")
senha = input("Senha: ")

sistema_autenticador(usuario,senha)

