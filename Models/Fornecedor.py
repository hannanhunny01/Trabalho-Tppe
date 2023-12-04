from Produto import Produto
import re


class Fornecedor:
    fornecedores_cadastrados = [] 

    def __init__(self, nome, endereco, codigo_fornecedor, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.codigo_fornecedor = codigo_fornecedor
    
    def cadastrar_fornecedor(self):
        if self.verificar_telefone:
            return False

        if self.produto == False:
            print("O produto informado não existe ou não foi cadastrado!")
            return False

        fornecedor_info = {
            "nome": self.nome,
            "endereco": self.endereco,
            "produto": self.produto,
            "codigo_fornecedor": self.codigo_fornecedor
        }

        self.fornecedores_cadastrados.append(fornecedor_info)
        print("Fornecedor cadastrado com sucesso!")

    def remover_fornecedor(self, codigo_fornecedor):
        for fornecedor in self.fornecedores_cadastrados:
            if fornecedor["codigo_fornecedor"] == codigo_fornecedor:
                self.fornecedores_cadastrados.remove(fornecedor)
                print(f"Fornecedor com código {codigo_fornecedor} removido com sucesso.")
                return
        print(f"Fornecedor com código {fornecedor} não encontrado.")

    def editar_fornecedor(self, codigo_fornecedor, novos_dados):
        for fornecedor in self.fornecedores_cadastrados:
            if fornecedor["codigo_fornecedor"] == codigo_fornecedor:
                codigo_fornecedor.update(novos_dados)
                print(f"Fornecedor com código {codigo_fornecedor} editado com sucesso.")
                return
        print(f"Fornecedor com código {codigo_fornecedor} não encontrado.")

    def verificar_telefone(telefone):
        regexPadrao = re.compile(r'^\+?(\d{1,4}[\s-]?)?(\()?(\d{1,})\)?[\s-]?(\d{1,})[\s-]?(\d{1,})[\s-]?$')

        if regexPadrao.match(telefone):
            return True
        else:
            print(f'O telefone {telefone} é inválido.')
            return False


if __name__ == '__main__':
    pass
