class Categoria:
    categorias_cadastradas = []

    def __init__(self, nome):
        self.nome = nome

    def cadastrar_categoria(self):

        for categoria in Categoria.categorias_cadastradas:
            if categoria.nome == self.nome:
                print(f"A categoria '{self.nome}' já existe!")
                return False

        if self.nome.strip() == "":
            print("Nome da categoria não pode ser vazio!")
            return False

        nova_categoria = Categoria(self.nome)
        Categoria.categorias_cadastradas.append(nova_categoria)
        print(f"Categoria '{self.nome}' cadastrada com sucesso!")
