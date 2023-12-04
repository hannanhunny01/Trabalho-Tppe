import unittest
from parameterized import parameterized
import sys
sys.path.append('../Models')
from Categoria import Categoria
from Exceptions import DescricaoEmBrancoException, ValorInvalidoException

class TestCategoria(unittest.TestCase):

    @parameterized.expand([
        ("Nova", True),
        ("Existente", True),
        ("", DescricaoEmBrancoException),
        ("123", ValorInvalidoException),
    ])
    def test_cadastrar_categoria(self, nome, resultado_esperado):
        categoria = Categoria(nome)
        try:
            self.assertEqual(categoria.cadastrar_categoria(), resultado_esperado)
        except DescricaoEmBrancoException as e:
            self.assertTrue(isinstance(e, DescricaoEmBrancoException))
        except ValorInvalidoException as e:
            self.assertTrue(isinstance(e, ValorInvalidoException))

    @parameterized.expand([
        ("Existente", True),
        ("Nova2", False),
    ])
    def test_remover_categoria(self, nome, resultado_esperado):
        categoria = Categoria(nome)
        self.assertEqual(categoria.remover_categoria(), resultado_esperado)

    @parameterized.expand([
        ("NovoNome", True),
        ("", DescricaoEmBrancoException),
        ("Inv@lido", ValorInvalidoException),
    ])
    def test_editar_categoria(self, novo_nome, resultado_esperado):
        categoria = Categoria("Existente")
        try:
            self.assertEqual(categoria.editar_categoria(novo_nome), resultado_esperado)
        except DescricaoEmBrancoException as e:
            self.assertTrue(isinstance(e, DescricaoEmBrancoException))
        except ValorInvalidoException as e:
            self.assertTrue(isinstance(e, ValorInvalidoException))
        
    @parameterized.expand([
        ("Existente", "Existente"),
        ("NaoExistente", False),
    ])
    def test_obter_categoria_por_nome(self, nome, resultado_esperado):
        self.assertEqual(Categoria.obter_categoria_por_nome(nome), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
