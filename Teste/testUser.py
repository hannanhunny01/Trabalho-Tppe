import unittest
from Models.User import Usuario

class TestUsuario(unittest.TestCase):
    def test_init(self):
        usuario = Usuario("Abdul", "123456789", "abdul@email.com", "senha123")
        self.assertEqual(usuario.nome, "Abdul")
        self.assertEqual(usuario.telefone, "123456789")
        self.assertEqual(usuario.email, "abdul@email.com")
        self.assertEqual(usuario.senha, "senha123")

if __name__ == '__main__':
    unittest.main()