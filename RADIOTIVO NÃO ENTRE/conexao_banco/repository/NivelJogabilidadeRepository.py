from bson import ObjectId
from conexao_banco.db.conexao import conecta_banco

class NivelJogabilidadeRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'nivel_jogabilidade'.
        """

        self.db = conecta_banco()
        self.collection = self.db['nivel_jogabilidade']

    def inserir_nivel(self, nivel_jogabilidade):

        """
        Insere um novo documento na collection 'nivel_jogabilidade'.
        """

        novo_nivel = {
            "nivel_jogabilidade": nivel_jogabilidade
        }
        resultado = self.collection.insert_one(novo_nivel)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'nivel_jogabilidade'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_nivel):

        """
        Retorna um documento da collection 'nivel_jogabilidade' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_nivel)})

    def atualizar_nivel(self, id_nivel, nivel_jogabilidade=None):

        """
        Atualiza o campo 'nivel_jogabilidade' de um documento.
        """

        if nivel_jogabilidade:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_nivel)},
                {"$set": {"nivel_jogabilidade": nivel_jogabilidade}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_nivel):

        """
        Deleta um documento da collection 'nivel_jogabilidade' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_nivel)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
