from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "abracadabra123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

# -------------------
# MODELOS
# -------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    responsavel = db.Column(db.String(100))

with app.app_context():
    db.create_all()

# -------------------
# LOGIN
# -------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user"] = user.id
            return redirect("/")

    return render_template("login.html")


# -------------------
# CADASTRO
# -------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        existe = User.query.filter_by(username=username).first()

        if not existe:
            db.session.add(User(username=username, password=password))
            db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# -------------------
# HOME
# -------------------

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    children = Child.query.all()

    return render_template(
        "home.html",
        children=children
    )


# -------------------
# CADASTRAR CRIANÇA
# -------------------

@app.route("/add_child", methods=["POST"])
def add_child():

    if "user" not in session:
        return redirect("/login")

    child = Child(
        nome=request.form["nome"],
        idade=request.form["idade"],
        responsavel=request.form["responsavel"]
    )

    db.session.add(child)
    db.session.commit()

    return redirect("/")


# -------------------
# EXCLUIR
# -------------------

@app.route("/delete_child/<int:id>")
def delete_child(id):

    if "user" not in session:
        return redirect("/login")

    child = Child.query.get(id)

    if child:
        db.session.delete(child)
        db.session.commit()

    return redirect("/")


# -------------------
# LOGOUT
# -------------------

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# -------------------
# HEALTH CHECK
# -------------------

@app.route("/health")
def health():
    return {
        "status": "online",
        "system": "AbracadabraKids"
    }


if __name__ == "__main__":
    app.run(debug=True)