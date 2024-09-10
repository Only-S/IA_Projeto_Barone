from bson import ObjectId
from conexao_banco.db.conexao import conecta_banco


class CasosRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a cololection 'casos'.
        """

        self.db = conecta_banco()
        self.collection = self.db['casos']

    def inserir_caso(self, valor, fk_plataforma, fk_usuario, online_offline, experiencia_nova, fk_lvljogabilidade,
                     fk_objetivo, fk_experiencia, fk_generojogo, fk_grafico, retro, jogo):

        """
        Insere um novo documento na collection 'casos'.
        """

        novo_caso = {
            "valor": valor,
            "fk_plataforma": ObjectId(fk_plataforma),
            "fk_usuario": ObjectId(fk_usuario),
            "online_offline": online_offline,
            "experiencia_nova": experiencia_nova,
            "fk_lvljogabilidade": ObjectId(fk_lvljogabilidade),
            "fk_objetivo": ObjectId(fk_objetivo),
            "fk_experiencia": ObjectId(fk_experiencia),
            "fk_generojogo": ObjectId(fk_generojogo),
            "fk_grafico": ObjectId(fk_grafico),
            "retro": retro,
            "jogo": jogo
        }
        resultado = self.collection.insert_one(novo_caso)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'casos'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_caso):

        """
        Retorna um documento da collection 'casos' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_caso)})

    def atualizar_caso(self, id_caso, valor=None, fk_plataforma=None, fk_usuario=None, online_offline=None,
                       experiencia_nova=None, fk_lvljogabilidade=None, fk_objetivo=None, fk_experiencia=None,
                       fk_generojogo=None, fk_grafico=None, retro=None, jogo=None):

        """
        Atualiza os campos de um documento na collection 'casos'.
        """

        atualizacao = {}
        if valor is not None:
            atualizacao["valor"] = valor
        if fk_plataforma is not None:
            atualizacao["fk_plataforma"] = ObjectId(fk_plataforma)
        if fk_usuario is not None:
            atualizacao["fk_usuario"] = ObjectId(fk_usuario)
        if online_offline is not None:
            atualizacao["online_offline"] = online_offline
        if experiencia_nova is not None:
            atualizacao["experiencia_nova"] = experiencia_nova
        if fk_lvljogabilidade is not None:
            atualizacao["fk_lvljogabilidade"] = ObjectId(fk_lvljogabilidade)
        if fk_objetivo is not None:
            atualizacao["fk_objetivo"] = ObjectId(fk_objetivo)
        if fk_experiencia is not None:
            atualizacao["fk_experiencia"] = ObjectId(fk_experiencia)
        if fk_generojogo is not None:
            atualizacao["fk_generojogo"] = ObjectId(fk_generojogo)
        if fk_grafico is not None:
            atualizacao["fk_grafico"] = ObjectId(fk_grafico)
        if retro is not None:
            atualizacao["retro"] = retro
        if jogo is not None:
            atualizacao["jogo"] = jogo

        if not atualizacao:
            return None  #Nada para atualizar

        resultado = self.collection.update_one(
            {"_id": ObjectId(id_caso)},
            {"$set": atualizacao}
        )
        return resultado.modified_count  #Retorna o número de documentos modificados

    def deletar_por_id(self, id_caso):

        """
        Deleta um documento da collection 'casos' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_caso)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
