import unittest
import sys
sys.path.append('../Models')
from Categoria import Categoria

class TestCategoria(unittest.TestCase):

    def test_init_categoria(self):
        categoria1 = Categoria(nome="Eletrônicos")
        categoria2 = Categoria(nome="Roupas")

        self.assertEqual(categoria1.nome, "Eletrônicos")
        self.assertEqual(categoria2.nome, "Roupas")

    def test_cadastrar_categoria(self):
        categoria = Categoria(nome="Alimento")
        self.assertFalse(categoria.cadastrar_categoria()) 

        categoria = Categoria(nome="    ")
        self.assertFalse(categoria.cadastrar_categoria())

        categoria = Categoria(nome="Alimento")
        self.assertFalse(categoria.cadastrar_categoria())

        categoria = Categoria(nome="Eletrônicos")
        self.assertFalse(categoria.cadastrar_categoria())

        self.assertEqual(len(Categoria.categorias_cadastradas), 2)

        self.assertEqual(Categoria.categorias_cadastradas[0].nome, "Alimento")


if __name__ == '__main__':
    unittest.main()
