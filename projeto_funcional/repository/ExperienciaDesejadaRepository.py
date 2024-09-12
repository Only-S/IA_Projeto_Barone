from bson import ObjectId
from db.conexao import conecta_banco

class ExperienciaDesejadaRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'experiencia_desejada'.
        """

        self.db = conecta_banco()
        self.collection = self.db['experiencia_desejada']

    def inserir_experiencia(self, experiencia):

        """
        Insere um novo documento na collection 'experiencia_desejada'.
        """

        nova_experiencia = {
            "experiencia": experiencia
        }
        resultado = self.collection.insert_one(nova_experiencia)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'experiencia_desejada'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_experiencia):

        """
        Retorna um documento da collection 'experiencia_desejada' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_experiencia)})

    def atualizar_experiencia(self, id_experiencia, experiencia=None):

        """
        Atualiza o campo 'experiencia' de um documento.
        """

        if experiencia:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_experiencia)},
                {"$set": {"experiencia": experiencia}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_experiencia):

        """
        Deleta um documento da collection 'experiencia_desejada' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_experiencia)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
