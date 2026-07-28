from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200

def test_criar_cliente():
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
    response = client.get("/clientes/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

def test_cliente_inexistente():
    response = client.get("/clientes/999999")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Cliente não encontrado"

def test_atualizar_cliente_inexistente():
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
    response = client.delete("/clientes/999999")

    assert response.status_code == 404