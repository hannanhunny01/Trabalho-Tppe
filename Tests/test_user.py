import unittest

import sys 

sys.path.append('Models')

from User import Usuario





class TestUsuario(unittest.TestCase):
    def test_init(self):
        usuario = Usuario("Abdul", "123456789", "abdul@email.com", "senha123")
        self.assertEqual(usuario.nome, "Abdul")
        self.assertEqual(usuario.telefone, "123456789")
        self.assertEqual(usuario.email, "abdul@email.com")
        self.assertEqual(usuario.senha, "senha123")

    def test_exibir_informacoes(self):
        usuario = Usuario("Abdul", "123456789", "abdul@email.com", "senha123")
        self.assertEqual(usuario.exibir_informacoes(), "Nome: Abdul\nTelefone: 123456789\nEmail: abdul@email.com")
        # Note que a senha não é exibida por questões de segurança
    
    def test_criar_usuario(self):
        usuario = Usuario("Usuario1", "123456789", "usuario1@example.com", "senha123")
        self.assertEqual(usuario.nome, "Usuario1")
        self.assertEqual(usuario.telefone, "123456789")
        self.assertEqual(usuario.email, "usuario1@example.com")
        self.assertEqual(usuario.senha, "senha123")

    def test_listar_usuarios(self):
        usuarios = [Usuario("Usuario1", "123456789", "usuario1@example.com", "senha123"),
                    Usuario("Usuario2", "987654321", "usuario2@example.com", "senha456")]
        self.assertEqual(Usuario.listar_usuarios(usuarios), usuarios)

    def test_salvar_usuario(self):
        usuarios = []
        usuario = Usuario("Usuario1", "123456789", "usuario1@example.com", "senha123")
        usuarios = usuario.salvar_usuario(usuarios)
        self.assertEqual(len(usuarios), 1)

    def test_atualizar_usuario(self):
        usuarios = [Usuario("Usuario1", "123456789", "usuario1@example.com", "senha123")]
        novo_usuario = Usuario("Usuario1", "123456789", "usuario1@example.com", "senha456")
        usuarios = novo_usuario.atualizar_usuario(usuarios)
        self.assertEqual(usuarios[0].senha, "senha456")

    def test_excluir_usuario(self):
        usuarios = [Usuario("Usuario1", "123456789", "usuario1@example.com", "senha123")]
        email = "usuario1@example.com"
        usuarios = Usuario.excluir_usuario(email, usuarios)
        self.assertEqual(len(usuarios), 0)
    

if __name__ == '__main__':
    unittest.main()

