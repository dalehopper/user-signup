from flask import Flask, request, redirect, render_template



app = Flask(__name__)

app.config['DEBUG'] = True  


user = ""

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/", methods = ["POST"])
def register():

    username = request.form.get("username")
    erroru ='' 
    if len(username) < 3 or len(username)>20:
        erroru = "Your username must be 3 to 20 charactors long"
    elif " " in username:
        erroru = "Spaces are not allowed in your username"

        
    password = request.form.get("password")
    errorp ='' 
    if len(password) < 3 or len(password)>20:
        errorp = "Your password must be 3 to 20 charactors long"
    elif " " in username:
        errorp = "Spaces are not allowed in your password"

    pass2 = request.form.get("pass2")
    error2 = ''
    if password != pass2:
        error2 = "Passwords do not match"


    email = request.form.get("email")
    errore = ''
    if len(email)>0 and (len(email) < 3 or len(email)>20 or " " in email or "." not in email or "@" not in email):
        errore = "Please enter a valid email." 
        
    if not (erroru or errorp or error2 or errore):
        return redirect("/welcome?user=" + username)
    else:   
        return render_template("forms.html", erroru = erroru, 
        username = username, errorp = errorp, 
        error2 = error2, email = email, errore = errore)



@app.route("/welcome")
def welcome():
    username = request.args.get("user")
    return render_template("welcome.html", username = username)
app.run()
