from models.Database import Database
from controllers.controller import Controller 

def main():
    # 1. SETUP: Conecta ao Banco e Inicia o Porteiro (Controller)
    print("--- INICIANDO SISTEMA ---")
    db = Database()
    api = Controller(db)

    # ---------------------------------------------------------
    # CENÁRIO 1: CRIAR PRODUTOS (POST)
    # ---------------------------------------------------------
    print("\n\n>>> 1. TESTE DE CRIAÇÃO (POST)")
    
    produto1 = {
        "nome": "Notebook Gamer",
        "descricao": "Ryzen 7, 16GB RAM",
        "preco": 4500.00,
        "estoque": 5,
        "categoria": "Eletrônicos"
    }
    
    produto2 = {
        "nome": "Mouse Sem Fio",
        "descricao": "Logitech Bluetooth",
        "preco": 80.00,
        "estoque": 20,
        "categoria": "Periféricos"
    }

    # Chamando o Controller (simulando uma requisição JSON)
    resposta = api.post_put(produto1, formato='json')
    print(f"Criar Produto 1: {resposta}")
    
    api.post_put(produto2, formato='json')
    print("Produto 2 criado.")

    # ---------------------------------------------------------
    # CENÁRIO 2: LISTAR TUDO (GET)
    # ---------------------------------------------------------
    print("\n\n>>> 2. TESTE DE LEITURA GERAL (GET) em XML")
    # Vamos pedir em XML só para testar a Factory
    print(api.get(formato='xml'))

    # ---------------------------------------------------------
    # CENÁRIO 3: ATUALIZAR (PUT)
    # ---------------------------------------------------------
    print("\n\n>>> 3. TESTE DE ATUALIZAÇÃO (PUT)")
    
    # Vamos fingir que descobrimos o ID do mouse (supondo que seja ID 2)
    # E vamos mudar o preço para 90.00 e estoque para 0
    dados_atualizacao = {
        "id": 2, 
        "preco": 90.00,
        "estoque": 0
    }
    
    resposta = api.post_put(dados_atualizacao, formato='json')
    print(f"Atualização: {resposta}")

    # ---------------------------------------------------------
    # CENÁRIO 4: BUSCAR UM SÓ (GET ID)
    # ---------------------------------------------------------
    print("\n\n>>> 4. TESTE DE BUSCA ÚNICA (GET ID)")
    print(api.get(formato='json', id=2))

    # ---------------------------------------------------------
    # CENÁRIO 5: DELETAR (DELETE)
    # ---------------------------------------------------------
    print("\n\n>>> 5. TESTE DE DELEÇÃO (DELETE)")
    # Deletando o produto 1
    resposta = api.delete(id=1, formato='json')
    print(f"Deletar: {resposta}")

    # ---------------------------------------------------------
    # CENÁRIO 6: TESTE DE ERRO (Tentar buscar o deletado)
    # ---------------------------------------------------------
    print("\n\n>>> 6. TESTE DE ERRO (404)")
    print(api.get(formato='json', id=1))

if __name__ == "__main__":
    main()