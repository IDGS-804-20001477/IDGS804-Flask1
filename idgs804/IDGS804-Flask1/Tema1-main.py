from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "!Hola Mundo¡ Nuevo hola mundo, me lleva"


if __name__ == "__main__":
    app.run(debug = True, port = 8080)