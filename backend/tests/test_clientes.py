"""
Testes automatizados das funcionalidades relacionadas
a clientes.

Os testes validam os principais comportamentos da API,
incluindo cenários de sucesso e tratamento de erros.
"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    """
    Verifica se a API está respondendo corretamente.
    """

    response = client.get("/")

    assert response.status_code == 200

def test_criar_cliente():
    """
    Verifica o cadastro de um novo cliente.
    """

    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente teste",
            "telefone": "11999999999",
            "observacoes": "Teste"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nome"] == "Cliente teste"
    assert data["telefone"] == "11999999999"
    assert "id" in data

def test_listar_clientes():
    """
    Verifica a listagem dos clientes cadastrados.
    """

    response = client.get("/clientes/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

def test_cliente_inexistente():
    """
    Verifica o retorno 404 para um cliente inexistente.
    """

    response = client.get("/clientes/999999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Cliente não encontrado"

def test_atualizar_cliente_inexistente():
    """
    Verifica o retorno 404 ao tentar atualizar
    um cliente inexistente.
    """

    response = client.put(
        "/clientes/999999",
        json={
            "nome": "Teste",
            "telefone": "11999999999",
            "observacoes": "Teste"
        }
    )

    assert response.status_code == 404

def test_deletar_cliente_inexistente():
    """
    Verifica o retorno 404 ao tentar remover
    um cliente inexistente.
    """
    
    response = client.delete("/clientes/999999")

    assert response.status_code == 404