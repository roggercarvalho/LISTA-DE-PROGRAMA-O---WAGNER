# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

def autenticacao(usuario: str, senha: str) -> str:    
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

autenticacao(usuario, senha)