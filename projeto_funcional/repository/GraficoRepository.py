from bson import ObjectId
from db.conexao import conecta_banco

class GraficoRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'grafico'.
        """

        self.db = conecta_banco()
        self.collection = self.db['grafico']

    def inserir_grafico(self, tipo_grafico):

        """
        Insere um novo documento na collection 'grafico'.
        """

        novo_grafico = {
            "tipo_grafico": tipo_grafico
        }
        resultado = self.collection.insert_one(novo_grafico)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da coillection 'grafico'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_grafico):

        """
        Retorna um documento da collection 'grafico' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_grafico)})

    def atualizar_genero(self, id_grafico, tipo_grafico=None):

        """
        Atualiza o campo 'tipo_grafico' de um documento.
        """

        if tipo_grafico:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_grafico)},
                {"$set": {"nome_genero": tipo_grafico}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_grafico):

        """
        Deleta um documento da collection 'genero_jogo' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_grafico)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
