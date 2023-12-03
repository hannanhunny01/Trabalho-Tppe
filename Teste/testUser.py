import unittest

import sys 

sys.path.append('Models')

from User import Usuario



# test_usuario.py
import unittest
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

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()