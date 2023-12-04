from Exceptions import DescricaoEmBrancoException, ValorInvalidoException

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
            raise DescricaoEmBrancoException("Nome da categoria não pode ser vazio!")
        
        if not self.nome.isalpha():
            print("Nome da categoria deve conter apenas letras!")
            raise ValorInvalidoException("Nome da categoria deve conter apenas letras!")

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
    
    def editar_categoria(self, novo_nome):
        for categoria in Categoria.categorias_cadastradas:
            if novo_nome.strip() == "":
                print("Nome da categoria não pode ser vazio!")
                raise DescricaoEmBrancoException("Nome da categoria não pode ser vazio!")

            if not novo_nome.isalpha():
                print("Nome da categoria deve conter apenas letras!")
                raise ValorInvalidoException("Nome da categoria deve conter apenas letras!")

            categoria.nome = novo_nome
            print(f"Categoria '{self.nome}' editada com sucesso!")
            return True

        print(f"A categoria '{self.nome}' não existe!")
        return False
    
    def obter_categoria_por_nome(nome):
        for categoria in Categoria.categorias_cadastradas:
            if categoria.nome == nome:
                print(f"Categoria '{nome}' encontrada!")
                return nome
        return False