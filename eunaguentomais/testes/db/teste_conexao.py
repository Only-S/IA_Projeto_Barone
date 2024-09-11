import pytest
from db.conexao import conecta_banco

@pytest.fixture
def db_conexao():

    """
    Fixture para fornecer a conexão com o banco de dados
    """

    db = conecta_banco()
    if db is None:
        pytest.fail("Falha ao conectar ao banco de dados")
    return db

def test_conexao_mongodb(db_conexao):

    """
    Testa se a conexão com o MongoDB foi bem-sucedida
    """

    try:

        #Envia um ping para testar se a conexão foi estabelecida
        db_conexao.command('ping')
        print("Conexão ao MongoDB verificada com sucesso.")

    except Exception as e:
        pytest.fail(f"Erro ao conectar ao MongoDB: {e}")

def test_buscar_casos(db_conexao):

    """
    Testa se os casos podem ser buscados corretamente
    """

    try:
        #Acessa a collection de casos
        collection = db_conexao['casos']

        #Busca os casos e os insere em uma lista (o find retorna um cursor)
        casos = list(collection.find())

        #Verifica se a lista de casos não está vazia
        assert len(casos) > 0, "Nenhum caso encontrado na coleção"

        print(f"{len(casos)} casos encontrados na coleção.")

    except Exception as e:
        pytest.fail(f"Erro ao buscar casos no MongoDB: {e}")

def test_inserir_caso(db_conexao):

    """
    Testa se um novo caso pode ser inserido na collection
    """

    try:

        collection = db_conexao['casos']

        #Dados fictícios do novo caso
        novo_caso = {
            "titulo": "Novo Caso de Teste",
            "descricao": "Descrição do novo caso para teste",
            "solucao": "Solução sugerida"
        }

        #Insere o novo caso
        resultado = collection.insert_one(novo_caso)
        assert resultado.acknowledged, "Inserção falhou"
        print("Caso inserido com sucesso no MongoDB.")

    except Exception as e:
        pytest.fail(f"Erro ao inserir caso no MongoDB: {e}")
