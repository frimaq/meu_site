from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        mensagem = request.form["mensagem"]
        # Aqui você pode salvar em banco de dados ou enviar e-mail
        print(f"Mensagem recebida de {nome} ({telefone}) - {email}: {mensagem}")
        return redirect(url_for("home"))
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
