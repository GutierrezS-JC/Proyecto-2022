from flask import Blueprint, redirect, url_for, request, flash, session, flash, render_template
from src.core import auth
from src.core.auth.user import User


login_blueprint = Blueprint("login", __name__, url_prefix="/")


@login_blueprint.get("/")
def login_index():
    if not session.get("user"):
        return render_template("login/index.html")
    else:
        return redirect(url_for("home.home_index"))


@login_blueprint.post("/auth/authenticate")
def authenticate():
    # print(request)
    if request.method == "POST":
        params = request.form
        user = auth.find_user_by_email_and_pass(params["email"], params["password"])

        if not user:
            flash("Usuario o clave incorrecto", "danger")
            return redirect(url_for("login.login_index"))

        if not user.activo:
            flash("Su cuenta se encuentra deshabilitada okk", "danger")
            return redirect(url_for("login.login_index"))

        session["user"] = user.email
        session["username"] = user.username

        roles = user.roles
        session["roles"] = []

        for r in roles:
            session["roles"].append(r)

        return redirect(url_for("home.home_index"))

    return render_template("login.login_index")


@login_blueprint.get("/auth/logout")
def logout():
    del session["user"]
    del session["username"]
    session.clear()
    flash("La sesion se cerro correctamente", "success")

    return redirect(url_for("login.login_index"))
