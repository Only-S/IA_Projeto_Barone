from bson import ObjectId
from conexao_banco.db.conexao import conecta_banco


class GostosRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'gostos'.
        """

        self.db = conecta_banco()
        self.collection = self.db['gostos']

    def inserir_gosto(self, nome_entretenimento, genero):

        """
        Insere um novo documento na collection 'gostos'.
        """

        novo_gosto = {
            "nome_entretenimento": nome_entretenimento,
            "genero": genero
        }
        resultado = self.collection.insert_one(novo_gosto)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'gostos'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_gosto):

        """
        Retorna um documento da collection 'gostos' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_gosto)})

    def atualizar_gosto(self, id_gosto, nome_entretenimento=None, genero=None):

        """
        Atualiza os campos 'nome_entretenimento' e/ou 'genero' de um documento.
        """

        atualizacao = {}
        if nome_entretenimento:
            atualizacao["nome_entretenimento"] = nome_entretenimento
        if genero:
            atualizacao["genero"] = genero

        if not atualizacao:
            return None  #Nada para atualizar

        resultado = self.collection.update_one(
            {"_id": ObjectId(id_gosto)},
            {"$set": atualizacao}
        )
        return resultado.modified_count  #Retorna o número de documentos modificados

    def deletar_por_id(self, id_gosto):

        """
        Deleta um documento da collection 'gostos' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_gosto)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
