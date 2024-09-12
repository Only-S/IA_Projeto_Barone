from bson import ObjectId
from db.conexao import conecta_banco

class GeneroJogoRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'genero_jogo'.
        """

        self.db = conecta_banco()
        self.collection = self.db['genero_jogo']

    def inserir_genero(self, nome_genero):

        """
        Insere um novo documento na collection 'genero_jogo'.
        """

        novo_genero = {
            "nome_genero": nome_genero
        }
        resultado = self.collection.insert_one(novo_genero)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'genero_jogo'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_genero):

        """
        Retorna um documento da collection 'genero_jogo' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_genero)})

    def atualizar_genero(self, id_genero, nome_genero=None):

        """
        Atualiza o campo 'nome_genero' de um documento.
        """

        if nome_genero:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_genero)},
                {"$set": {"nome_genero": nome_genero}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_genero):

        """
        Deleta um documento da collection 'genero_jogo' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_genero)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
