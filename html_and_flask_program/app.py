from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/profile')
def profile():
    if "response" in session:
        return render_template("profile.html")
    return render_template("common_html_file.html", title="Login", msg="Please Login First")


@app.route('/login')
def login():
    if "response" in session:
        return render_template("already_logined.html")
    return render_template("login.html")


@app.route('/success', methods=["POST"])
def success():
    name = request.form.get("name")
    password = request.form.get("password")
    if name == "aditya" and password == "aditya":
        session["response"] = "aditya"
        return render_template("logined_successfully.html")
    return render_template("error.html")


@app.route("/logout")
def log_out():
    if "response" in session:
        session.clear()
        return render_template("log_out.html")
    return render_template("common_html_file.html", title="Login Error", msg="You have'nt Logined to Log Out. So first login.")


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
