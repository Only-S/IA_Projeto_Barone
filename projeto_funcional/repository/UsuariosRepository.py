from bson import ObjectId
from db.conexao import conecta_banco

class UsuariosRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'usuarios'.
        """

        self.db = conecta_banco()
        self.collection = self.db['usuarios']

    def inserir_usuario(self, idade, sexo, orcamento, fk_gostos, fk_historico):

        """
        Insere um novo documento na collection 'usuarios'.
        """

        novo_usuario = {
            "idade": idade,
            "sexo": sexo,
            "orcamento": orcamento,
            "fk_gostos": [ObjectId(gosto_id) for gosto_id in fk_gostos],
            "fk_historico": [ObjectId(historico_id) for historico_id in fk_historico]
        }
        resultado = self.collection.insert_one(novo_usuario)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'usuarios'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_usuario):

        """
        Retorna um documento da collection 'usuarios' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_usuario)})

    def atualizar_usuario(self, id_usuario, idade=None, sexo=None, orcamento=None, fk_gostos=None, fk_historico=None):

        """
        Atualiza os campos de um documento na collection 'usuarios'.
        """

        atualizacao = {}
        if idade is not None:
            atualizacao["idade"] = idade
        if sexo is not None:
            atualizacao["sexo"] = sexo
        if orcamento is not None:
            atualizacao["orcamento"] = orcamento
        if fk_gostos is not None:
            atualizacao["fk_gostos"] = [ObjectId(gosto_id) for gosto_id in fk_gostos]
        if fk_historico is not None:
            atualizacao["fk_historico"] = [ObjectId(historico_id) for historico_id in fk_historico]

        if not atualizacao:
            return None  #Nada para atualizar

        resultado = self.collection.update_one(
            {"_id": ObjectId(id_usuario)},
            {"$set": atualizacao}
        )
        return resultado.modified_count  #Retorna o número de documentos modificados

    def deletar_por_id(self, id_usuario):

        """
        Deleta um documento da collection 'usuarios' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_usuario)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
