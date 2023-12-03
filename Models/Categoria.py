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
        return True

    def remover_categoria(self):
        for categoria in Categoria.categorias_cadastradas:
            if categoria.nome == self.nome:
                Categoria.categorias_cadastradas.remove(categoria)
                print(f"Categoria '{self.nome}' removida com sucesso!")
                return True

        print(f"A categoria '{self.nome}' não existe!")
        return False
