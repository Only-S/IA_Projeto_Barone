from bson import ObjectId
from db.conexao import conecta_banco

class ObjetivoJogabilidadeRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'objetivo_jogabilidade'.
        """

        self.db = conecta_banco()
        self.collection = self.db['objetivo_jogabilidade']

    def inserir_objetivo(self, objetivo):

        """
        Insere um novo documento na collection 'objetivo_jogabilidade'.
        """

        novo_objetivo = {
            "objetivo": objetivo
        }
        resultado = self.collection.insert_one(novo_objetivo)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'objetivo_jogabilidade'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_objetivo):

        """
        Retorna um documento da collection 'objetivo_jogabilidade' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_objetivo)})

    def atualizar_objetivo(self, id_objetivo, objetivo=None):

        """
        Atualiza o campo 'objetivo' de um documento.
        """

        if objetivo:
            resultado = self.collection.update_one(
                {"_id": ObjectId(id_objetivo)},
                {"$set": {"objetivo": objetivo}}
            )
            return resultado.modified_count  #Retorna o número de documentos modificados
        return None  #Nada para atualizar

    def deletar_por_id(self, id_objetivo):

        """
        Deleta um documento da collection 'objetivo_jogabilidade' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_objetivo)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
