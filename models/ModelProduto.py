from Database import Database
from Produtos import Produto

class ModelProduto:

    def __init__(self, database: Database):
        self._db = database

    def cria_row(self, row):
        return Produto(
            id = row['id'],
            nome = row['nome'],
            descricao = row['descricao'],
            preco = row['preco'],
            estoque = row['estoque'],
            categoria = row['categoria']
        )
    
    def criar_atualizar(self, produto : Produto):
        if produto.id:
            sql = """
                UPDATE produtos 
                SET nome=?, descricao=?, preco=?, estoque=?, categoria=?
                WHERE id=?
            """

            values = (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.categoria, produto.id)

        else:
            sql = """
                INSERT INTO produtos (nome, descricao, preco, estoque, categoria)
                VALUES (?, ?, ?, ?, ?)
            """

            values = (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.categoria)

        self._db.cursor().execute(sql, values)

    def listar(self) -> list:
        cur = self._db.cursor().execute("SELECT * FROM produtos")
        lista_resultados = cur.fetchall()
        rows = []        
        for item in lista_resultados:
            rows.append(self.cria_row(item))
        return rows
    
    def obter_id(self, id) -> Produto:
        cur = self._db.cursor().execute("SELECT * FROM produtos WHERE id = ?", (id,))
        resultado = cur.fetchone()
        if resultado: 
            resultado = self.cria_row(resultado)
        return resultado
    
    def buscar(self, termo) -> list:
        termo = f"%{termo}%"
        cur = self._db.cursor().execute("SELECT * FROM produtos WHERE nome LIKE ? OR descricao LIKE ? OR categoria LIKE ?", (termo, termo, termo))
        lista_resultados = cur.fetchall()
        rows = []
        for item in lista_resultados:
            rows.append(self.cria_row(item))
        return rows
    
    def remover(self, id):
        sql = "DELETE FROM produtos WHERE id = ?"
        self._db.cursor().execute(sql, (id,))