from flask import Flask, render_template, request
from service.CasosService import mapear_atributos, recomendar_jogos
from repository.CasosRepository import CasosRepository

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    '''
    Função principal da rota base, responsável por pegar as informações inseridas no form
    '''

    if request.method == "POST":
        #Captura os dados do formulário
        valor = request.form.get("valor")
        plataforma = request.form.get("plataforma")
        objetivo = request.form.get("objetivo")
        online_offline = request.form.get("online_offline")
        retro = request.form.get("retro")
        grafico = request.form.get("grafico")
        nivel_jogabilidade = request.form.get("lvljogabilidade")
        genero = request.form.get("genero")
        experiencia_desejada = request.form.get("experiencia")

        #Cria o caso do usuário
        caso_usuario = {
            "valor": valor,
            "fk_plataforma": plataforma,
            "fk_objetivo": objetivo,
            "online_offline": online_offline,
            "retro": retro,
            "fk_grafico": grafico,
            "fk_lvljogabilidade": nivel_jogabilidade,
            "fk_generojogo": genero,
            "fk_experiencia": experiencia_desejada
        }

        #Mapeia e transforma o caso em números
        caso_processado = mapear_atributos(caso_usuario)

        #Só um teste boy
        print(caso_processado)

        casoRepository = CasosRepository()
        casos = casoRepository.buscar_todos()

        #Recomenda os jogos
        jogos_recomendados = recomendar_jogos(casos, caso_processado)

        #Retorna a página com os jogos recomendados
        return render_template("index.html", jogos=jogos_recomendados)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
