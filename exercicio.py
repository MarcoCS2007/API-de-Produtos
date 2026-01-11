# EXERCÍCIO 6: MVC para API de Produtos
# =======================================
"""
Crie um sistema MVC para API de produtos (e-commerce).

Requisitos:
- Model Produto: gerencia produtos (CRUD completo)
- View JSON/XML: renderiza produtos em diferentes formatos
- Controller API: coordena endpoints REST

Endpoints:
- GET /produtos - lista todos
- GET /produtos/{id} - obtém produto específico
- POST /produtos - cria produto
- PUT /produtos/{id} - atualiza produto
- DELETE /produtos/{id} - deleta produto

Propriedades de Produto:
- id, nome, descrição, preço, estoque, categoria
"""

# TODO: Implemente aqui
class ModelProduto:
    """Model para produtos"""
    pass

class ViewAPI(ABC):
    """View abstrata para API"""
    pass

class ControllerProdutoAPI:
    """Controller para API de produtos"""
    pass
