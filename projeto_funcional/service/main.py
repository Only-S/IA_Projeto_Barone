from service.CasosService import normalizar, mapear_atributos, distancia_euclidiana
from repository.CasosRepository import CasosRepository
from bson import ObjectId


#Função principal para rodar o processo
def main():

    casosRepository = CasosRepository()

    #Passo 1: Obter casos do banco de dados
    casos = casosRepository.buscar_todos()

    #Passo 2: Aplicar mapeamento para transformar atributos categóricos em numéricos
    casos = mapear_atributos(casos)

    #Passo 3: Normalizar os atributos numéricos (exemplo com 'valor')
    normalizar(casos, 'valor')

    # Passo 4:Exemplo de caso de teste inserido com ObjectId
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

    # Passo 5:Mapear o caso de teste para valores numéricos
    caso_teste = mapear_atributos(caso_teste)

    #CANSEI DE TESTAR ESSA M$#$@$#@#$
    print(caso_teste)

    #Passo 6: Calcular distância entre o caso de teste e os casos armazenados
    atributos = ['valor', 'online_offline', 'fk_plataforma', 'fk_lvljogabilidade', 'fk_grafico', 'fk_generojogo', 'fk_experiencia', 'retro', 'fk_objetivo']
    distancias = [(caso, distancia_euclidiana(caso, caso_teste, atributos)) for caso in casos]

    #Passo 7: Ordenar os casos pela distância
    casos_proximos = sorted(distancias, key=lambda x: x[1])

    #Exibir os casos mais próximos
    print("Casos mais próximos:")
    for caso, distancia in casos_proximos[:5]:
        print(f"Jogo: {caso['jogo']}, Distância: {distancia}")

if __name__ == "__main__":
    main()

