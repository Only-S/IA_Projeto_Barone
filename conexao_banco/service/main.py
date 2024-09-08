from CasosService import processar_casos, aplicar_one_hot_encoding


def main():
    #Processar todos os casos
    casos_processados = processar_casos()

    #Exemplo de input do usuário
    input_usuario = {
        'valor': 'Caro',
        'plataforma': 'PC',
        'online_offline': True,
        'experiencia_nova': False,
        'nivel_jogabilidade': 'Experiente',
        'objetivo': 'Competição',
        'experiencia': 'Algo emocionante',
        'genero_jogo': 'JRPG',
        'grafico': 'Realista',
        'retro': False
    }

    #Aplicar One-Hot Encoding nos casos e no input do usuário
    df_casos_encoded, df_input_usuario_encoded = aplicar_one_hot_encoding(casos_processados, input_usuario)

    print("Casos codificados:")
    print(df_casos_encoded)

    print("\nInput do usuário codificado:")
    print(df_input_usuario_encoded)

if __name__ == "__main__":
    main()