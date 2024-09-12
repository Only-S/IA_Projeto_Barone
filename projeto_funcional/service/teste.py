from CasosService import normalizar, mapear_atributos
from bson import ObjectId


#Função para testar o processamento e normalização de um caso
def teste_processamento_normalizacao():
    #Exemplo de caso com ObjectId e valores categóricos
    caso_teste = {
        "valor": "Caro",
        "fk_plataforma": ObjectId("66d8e49da84429342c093999"),
        "fk_objetivo": ObjectId("66e0f629a62a8d19625a2d80"),
        "fk_lvljogabilidade": ObjectId("66e0f5e4a62a8d19625a2d7c"),
        "fk_grafico": ObjectId("66d8e569a84429342c09399b"),
        "fk_generojogo": ObjectId("66d8e9255bf9b45f18f1d075"),
        "fk_experiencia": ObjectId("66d8e5d15bd0216532f8b876"),
        "online_offline": False,
        "retro": False
    }

    #Mapeamento dos atributos categóricos para valores numéricos
    caso_teste_mapeado = mapear_atributos(caso_teste)

    print("Caso mapeado:")
    for chave, valor in caso_teste_mapeado.items():
        print(f"{chave}: {valor}")

    #Lista de casos simulados (para normalização)
    casos = [caso_teste_mapeado, {
        "valor": 3,
        "fk_plataforma": 2,
        "fk_objetivo": 3,
        "fk_lvljogabilidade": 1,
        "fk_grafico": 2,
        "fk_generojogo": 1,
        "fk_experiencia": 2,
        "online_offline": 1,
        "retro": 0
    }]

    #Normalizar o atributo 'valor' nos casos
    normalizar(casos, 'valor')

    print("\nCasos após normalização do atributo 'valor':")
    for i, caso in enumerate(casos):
        print(f"Caso {i + 1}: {caso}")


#Executar o teste
if __name__ == "__main__":
    teste_processamento_normalizacao()
