from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/profile')
def profile():
    if "response" in session:
        return render_template("common_html_file.html", title="View Profile", msg= f"Welcome {session['response']} !")
    return render_template("common_html_file.html", title="Login", msg="Please Login First")


@app.route('/login')
def login():
    if "response" in session:
        return render_template("common_html_file.html", title="Already Login", msg=f"You have already login {session['response']} !")
    return render_template("login.html")


@app.route('/success', methods= ["POST"])
def success():
    with open("user_data.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(',')

            name = line[0]
            email = line[1]
            password = line[2]

            if request.form.get("email").strip().lower() == email and request.form.get("password") == password:
                session['response'] = name.capitalize()
                return render_template("common_html_file.html", title="Login Successfull", msg=f"You have logined successfully {session['response']} !")
    return render_template("common_html_file.html", title="Login Error",
                           msg=f"The Name or Password that you have entered is wrong ! Pls try again")


@app.route("/logout")
def log_out():
    if "response" in session:
        name = session['response']
        session.clear()
        return render_template("common_html_file.html", title="Log Out", msg=f"You have Log Out successfully {name} !")
    return render_template("common_html_file.html", title= "Login Error", msg= "You have'nt Login to Log Out. So first login.")


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")


@app.route("/create_account_success",  methods= ["POST"])
def create_account_success():
    with open("user_data.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split(',')

            email = line[1]

            if request.form.get("email").strip().lower() == email or request.form.get("name").strip().lower() == "" or request.form.get("email").strip().lower() == "" or request.form.get("password").strip().lower() == "":
                return render_template("common_html_file.html", title="Error",
                                      msg=f"There was some Error while Creating the account. Pls try again.")

    with open("user_data.txt", "a") as file:
        file.writelines([f'{request.form.get("name").strip().lower()},', f'{request.form.get("email").strip().lower()},', request.form.get("password"), "\n"])
        return render_template("common_html_file.html", title="Create Account Success",
                       msg=f'An account with the Name ---- "{request.form.get("name").strip().lower().capitalize()}" and Email ---- {request.form.get("email").strip().lower()} is created ')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
