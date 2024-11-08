from flask import*
from controllers.controller import*

app = Flask(__name__)
app.secret_key = "kamaleoesbicolores"

publicroutes = ["quitanda.iniciar", "quitanda.verificar"]

@app.before_request
def verificarLogin():
     if request.endpoint in publicroutes:
        if "user" not in session:
             return redirect(url_for("error_401.html"))
        return

app.register_blueprint(quitanda_controller)

if __name__ == '__main__':
    app.run(debug = True)