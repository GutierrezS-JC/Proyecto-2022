from flask import redirect, render_template, request, url_for, abort, session, flash
from src.core.database import db
from src.core.auth.user import User


# def authenticated(session):
#     return session.get("user")


def login():
    return render_template("login/index.html")


def authenticate():
    if request.method == "POST":
        params = request.form
        user = User.get_by_email_and_pass(params["email"], params["password"])

        if not user:
            flash("Usuario o clave incorrecto", "danger")
            return redirect(url_for("login.login_index"))

        if user.activo == 0:
            flash("Su cuenta se encuentra deshabilitada okk", "danger")
            return redirect(url_for("login.login_index"))

        session["user"] = user["email"]
        session["username"] = user["username"]
        roles = user.roles
        session["roles"] = []
        for r in roles:
            session["roles"].append(r)

        return redirect(url_for("home.home_index"))

    return render_template("login.login_index")


def logout():
    del session["user"]
    session.clear()
    flash("La sesion se cerro correctamente")

    return redirect(url_for("login.login_index"))
