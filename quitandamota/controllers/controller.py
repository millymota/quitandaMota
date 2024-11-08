from flask import*
from model import*
from app import publicroutes

quitanda_controller = Blueprint("quitanda", __name__)

@quitanda_controller.route("/")
def iniciar():
    return render_template("index.html" )

@quitanda_controller.route("/verificar", methods= ['POST'])
def verificar():
    user = request.form.get("user")
    senha = request.form.get("senha")
    if user.split("@")[1] != "":
        if user.split("@")[1] != "1" | "2"| "3"|"4"|"5"|"6"|"7"|"8"| "9"|"0":
            session['user'] = user
            session['senha'] = senha
            return redirect(url_for("quitanda.compras"))
    return "user errado. tente novamente, sem números e não esqueça do @ no início!"

@quitanda_controller("/compras", methods = ["POST"])
def compras():
        carrinho = request.form["carrinho"]
        return render_template(url_for("pagamento.html"))

@quitanda_controller("/logout")
def logout():
    carrinho = make_response(redirect(url_for("quitanda.iniciar")))
    session.pop("user", None)
    session.pop("senha", None)
    carrinho.set_cookie("frutas", "", expires=0)
    carrinho.set_cookie("verdleg", "", expires=0)
