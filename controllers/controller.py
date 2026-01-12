from models.ModelProduto import ModelProduto 
from models.Produtos import Produto
from views.view import FactoryView as View
from models.Database import Database

class Controller:

    def __init__(self, database: Database):
        self._database = database
        self.model = ModelProduto(self._database)

    def get(self, formato, id = None):
        if not id:
            resultado = self.model.listar()
        else:
            resultado = self.model.buscar(id)
            if not resultado:
                return View.criar(formato).renderizar_erro('Produto não encontrado')
        try:
            return View.criar(formato).renderizar(resultado)

        except Exception as e:
            return View.criar('json').renderizar_erro(f'Erro: {e}')
        
    def post_put(self, dados: dict, formato: str = 'json'):
        if 'id' in dados:
            try:
                resultado = self.model.obter_id(dados['id'])
            except:
                return View.criar(formato).renderizar_erro('Erro ao verificar ID')
            if resultado:
                if 'nome' in dados: resultado.nome = dados['nome']
                if 'descricao' in dados: resultado.descricao = dados['descricao']
                if 'preco' in dados: resultado.preco = dados['preco']
                if 'estoque' in dados: resultado.estoque = dados['estoque']
                if 'categoria' in dados: resultado.categoria = dados['categoria']
                try:
                    self.model.criar_atualizar(resultado)
                except:
                    return View.criar(formato).renderizar_erro('Erro ao salvar alterações')   
            else:
                return View.criar(formato).renderizar_erro('Erro!! ID não consta no banco de dados.')
        else:
                try:
                    resultado = Produto(
                    nome = dados['nome'],
                    descricao = dados['descricao'],
                    preco = dados['preco'],
                    estoque = dados['estoque'],
                    categoria = dados['categoria']
                    )
                    self.model.criar_atualizar(resultado)
                except:
                    return View.criar(formato).renderizar_erro('Erro ao salvar produto')

        return View.criar(formato).renderizar(resultado)
    
    def delete(self, id: int, formato: str = 'json'):
        try:
            resultado = self.model.obter_id(id)
        except Exception as e:
            return View.criar(formato).renderizar_erro(f'Erro ao verificar ID: {e}')
        try:
            if resultado:
                self.model.remover(id)
            else:
                return View.criar(formato).renderizar_erro('Erro ao deletar! ID não encontrado!')
        except Exception as e:
            return View.criar(formato).renderizar_erro(f'Erro ao deletar!: {e}')
        
        return View.criar(formato).renderizar(resultado)
