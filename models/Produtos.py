class Produto:
    def __init__(self, nome, descricao, preco, estoque, categoria, id=None):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._estoque = estoque
        self._categoria = categoria

    def to_dict(self):
        return {
            "id": self._id,
            "nome": self._nome,
            "descricao": self._descricao,
            "preco": self._preco,
            "estoque": self._estoque,
            "categoria": self._categoria
        }

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, value):
        self._estoque = value

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, value):
        self._categoria = value