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
        if not self.verificar_telefone(self.telefone):
            print("Fornecedor não pode ser cadastrado devido a um telefone inválido.")
            return False

        fornecedor_info = {
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "codigo_fornecedor": self.codigo_fornecedor
        }

        self.fornecedores_cadastrados.append(fornecedor_info)
        print("Fornecedor cadastrado com sucesso!")
        return True

    def remover_fornecedor(self, codigo_fornecedor):
        for fornecedor in self.fornecedores_cadastrados:
            if fornecedor["codigo_fornecedor"] == codigo_fornecedor:
                self.fornecedores_cadastrados.remove(fornecedor)
                print(f"Fornecedor com código {codigo_fornecedor} removido com sucesso.")
                return fornecedor
        print(f"Fornecedor com código {fornecedor} não encontrado.")
        return False

    def editar_fornecedor(self, codigo_fornecedor, novos_dados):
        for fornecedor in self.fornecedores_cadastrados:
            if fornecedor["codigo_fornecedor"] == codigo_fornecedor:
                for key, value in novos_dados.items():
                    fornecedor[key] = value
                print(f"Fornecedor '{self.nome}' editado com sucesso!")
                return True

        print(f"O fornecedor '{self.nome}' não existe!")
        return False

    def verificar_telefone(self, telefone):
        regexPadrao = re.compile(r'^\+?(\d{1,4}[\s-]?)?(\()?(\d{1,})\)?[\s-]?(\d{1,})[\s-]?(\d{1,})[\s-]?$')

        if regexPadrao.match(telefone):
            return True
        else:
            print(f'O telefone {telefone} é inválido.')
            return False

    def obter_fornecedor_por_codigo_fornecedor(fornecedor):
        for fornecedor in Fornecedor.fornecedores_cadastrados:
            if fornecedor.codigo_fornecedor == fornecedor:
                print(f"Fornecedor '{fornecedor}' encontrado!")
                return fornecedor
        return False


if __name__ == '__main__':
    pass
