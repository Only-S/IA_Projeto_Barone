from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#URL com as credenciais do meu usuário do banco
uri = "mongodb+srv://giovane_grandi:12345@atitus.ztwya.mongodb.net/?retryWrites=true&w=majority&appName=Atitus"

#Função resposnável pela conexão com o banco do mongo
def conecta_banco():
    """
    Cria uma conexão com o MongoDB Atlas e retorna o banco de dados.
    """
    try:
        # Conecta ao MongoDB usando a URI fornecida pelo MongoDB Atlas acima
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Envia um comando de ping para verificar a conexão
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        # Retorna o banco de dados
        db = client['projeto_barone'] #Fazendo a busca pelo banco onde estão os nossos casos
        return db
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None
