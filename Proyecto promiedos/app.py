import json

from flask import Flask, render_template


app = Flask(__name__)


def cargar_equipos():

    with open("datos/equipos.json", "r", encoding="utf-8") as archivo:

        return json.load(archivo)

def cargar_plantel(slug):

    with open(
        f"datos/planteles/{slug}.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        return json.load(archivo)

    

@app.route("/")
def inicio():

    partidos = [
        {
            "competicion": "🇦🇷 Liga Profesional",
            "local": "River Plate",
            "visitante": "Talleres",
            "resultado": "2 - 1",
            "estado": "Finalizado"
        },
        {
            "competicion": "🇦🇷 Liga Profesional",
            "local": "Boca Juniors",
            "visitante": "Racing",
            "resultado": "1 - 1",
            "estado": "72'"
        },
        {
            "competicion": "🇪🇸 La Liga",
            "local": "Barcelona",
            "visitante": "Real Madrid",
            "resultado": "0 - 0",
            "estado": "Próximamente"
        }
    ]

    return render_template("index.html", partidos=partidos)


@app.route("/ligas")
def ligas():

    return render_template("ligas.html")


@app.route("/liga/argentina")
def liga_argentina():

    equipos_datos = cargar_equipos()

    equipos = []


    for slug, datos in equipos_datos.items():

        equipo = {
            "equipo": datos["nombre"],
            "slug": slug,
            "pj": datos["pj"],
            "pg": datos["pg"],
            "pe": datos["pe"],
            "pp": datos["pp"],
            "gf": datos["gf"],
            "gc": datos["gc"],
            "dg": datos["gf"] - datos["gc"],
            "puntos": datos["puntos"]
        }

        equipos.append(equipo)


    equipos.sort(
    key=lambda equipo: (
        equipo["puntos"],
        equipo["dg"],
        equipo["gf"]
    ),
    reverse=True
)


    for indice, equipo in enumerate(equipos, start=1):

        equipo["posicion"] = indice


    return render_template(
        "liga_argentina.html",
        equipos=equipos
    )

@app.route("/equipo/<nombre>")
def equipo(nombre):

    equipos = {

        "river": {
            "nombre": "River Plate",
            "pais": "Argentina",
            "estadio": "Estadio Monumental",
            "dt": "Marcelo Gallardo",
            "competicion": "Liga Profesional",
            "pj": 20,
            "pg": 13,
            "pe": 3,
            "pp": 4
        },

        "boca": {
            "nombre": "Boca Juniors",
            "pais": "Argentina",
            "estadio": "La Bombonera",
            "dt": "Director técnico",
            "competicion": "Liga Profesional",
            "pj": 20,
            "pg": 11,
            "pe": 5,
            "pp": 4
        },

        "racing": {
            "nombre": "Racing Club",
            "pais": "Argentina",
            "estadio": "Presidente Perón",
            "dt": "Director técnico",
            "competicion": "Liga Profesional",
            "pj": 20,
            "pg": 10,
            "pe": 7,
            "pp": 3
        }

    }


    if nombre not in equipos:

        return "Equipo no encontrado", 404


    equipo_actual = equipos[nombre]

    plantel_datos = cargar_plantel(nombre)

    print(plantel_datos)


    formacion = [
        {
            "nombre": "Franco Armani",
            "numero": 1,
            "posicion": "ARQ",
            "clase": "goalkeeper"
        },
        {
            "nombre": "Fabricio Bustos",
            "numero": 16,
            "posicion": "LD",
            "clase": "d4"
        },
        {
            "nombre": "Germán Pezzella",
            "numero": 6,
            "posicion": "DFC",
            "clase": "d2"
        },
        {
            "nombre": "Paulo Díaz",
            "numero": 17,
            "posicion": "DFC",
            "clase": "d3"
        },
        {
            "nombre": "Marcos Acuña",
            "numero": 24,
            "posicion": "LI",
            "clase": "d1"
        },
        {
            "nombre": "Manuel Lanzini",
            "numero": 10,
            "posicion": "MC",
            "clase": "m1"
        },
        {
            "nombre": "Enzo Perez",
            "numero": 5,
            "posicion": "MCD",
            "clase": "m2"
        },
        {
            "nombre": "Franco Mastantuono",
            "numero": 30,
            "posicion": "MC",
            "clase": "m3"
        },
        {
            "nombre": "Pablo Solari",
            "numero": 36,
            "posicion": "ED",
            "clase": "f3"
        },
        {
            "nombre": "Miguel Borja",
            "numero": 9,
            "posicion": "DC",
            "clase": "f2"
        },
        {
            "nombre": "Facundo Colidio",
            "numero": 11,
            "posicion": "EI",
            "clase": "f1"
        }
    ]


    plantel = formacion


    return render_template(
        "equipo.html",
        equipo=equipo_actual,
        plantel=plantel,
        formacion=formacion
    )


if __name__ == "__main__":
    app.run(debug=True)