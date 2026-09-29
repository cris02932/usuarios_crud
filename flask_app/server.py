from flask import Flask, render_template, request, redirect
from models.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def index():
    usuario = Usuario.get_all()
    return render_template("usuarios.html", todos_los_usuarios=usuario)

@app.route("/crear_usuario", methods=["POST"])
def nuevo_usuario():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }

    Usuario.save(datos)

    return redirect("/")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("ver_usuario.html", usuario=usuario)

@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }

    Usuario.update(datos)

    return redirect("/")

@app.route("/usuarios/<int:id>/borrar")
def borrar_usuario(id):
    Usuario.delete(id)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
