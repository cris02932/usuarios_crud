from flask import Flask, render_template, request, redirect

from models.usuario import Usuario

app=Flask(__name__)

@app.route("/")

def index():
    usuario=Usuario.get_all()

    return render_template("usuarios.html", todos_los_usuarios=usuario)

@app.route("/crear_usuario", methods= ['POST'])
def nuevo_usuario():
    datos={
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    print(datos)
    Usuario.save(datos)

    return redirect("/")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")
if __name__ == "__main__":
    app.run(debug=True)