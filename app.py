from flask import Flask, render_template, request, redirect
import urllib.parse

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

        # Monta o texto que será enviado
        texto = (
            f"📩 Nova mensagem de contato!\n\n"
            f"👤 Nome: {nome}\n"
            f"📧 Email: {email}\n"
            f"📱 Telefone informado: {telefone}\n\n"
            f"💬 Mensagem:\n{mensagem}"
        )

        # Codifica o texto para URL
        texto_encoded = urllib.parse.quote(texto)

        # Seu número do WhatsApp (formato internacional)
        numero_whats = "5554991853581"

        # Monta a URL do WhatsApp
        url = f"https://wa.me/{numero_whats}?text={texto_encoded}"
        return redirect(url)

    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
