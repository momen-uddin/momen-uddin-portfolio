from flask import Flask, render_template, request, url_for, redirect, flash
import secrets
app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.secret_key = secret_key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        clientName = request.form['name']
        clientEmail = request.form['email']
        clientPhone = request.form['phone']
        clientMsg = request.form['msg']
        
        flash("Your message has been sent successfully!", "success")
        return render_template("index.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)