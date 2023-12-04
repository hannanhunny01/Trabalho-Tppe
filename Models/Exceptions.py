class CodigoDeBarrasException(Exception):
    def __init__(self, message="Código de barras inválido!"):
        self.message = message
        super().__init__(message)

class DescricaoEmBrancoException(Exception):
    def __init__(self, message="Nome da categoria não pode ser vazio!"):
        self.message = message
        super().__init__(self.message)

class ValorInvalidoException(Exception):
    def __init__(self, message="Nome da categoria deve conter apenas letras!"):
        self.message = message
        super().__init__(self.message)

class EstoqueNegativoException(Exception):
    def __init__(self, message="Quantidade de produtos não pode ser negativa!"):
        self.message = message
        super().__init__(message)