from bson import ObjectId
from db.conexao import conecta_banco

class PlataformaRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'plataforma'.
        """

        self.db = conecta_banco()
        self.collection = self.db['plataforma']

    def inserir_plataforma(self, nome_plataforma):

        """
        Insere um novo documento na collection 'plataforma'.
        """

        nova_plataforma = {
            "nome_plataforma": nome_plataforma
        }
        resultado = self.collection.insert_one(nova_plataforma)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'plataforma'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_plataforma):

        """
        Retorna um documento da collection 'plataforma' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_plataforma)})

    def atualizar_plataforma(self, id_plataforma, nome_plataforma=None):

        """
        Atualiza o campo 'nome_plataforma' de um documento.
        """

        if nome_plataforma:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_plataforma)},
                {"$set": {"nome_plataforma": nome_plataforma}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_plataforma):

        """
        Deleta um documento da collection 'plataforma' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_plataforma)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
