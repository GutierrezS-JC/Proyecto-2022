from flask import Blueprint, redirect, url_for, flash
from flask import render_template

from src.core import models

from src.web.helpers.forms import ConfigForm
from src.web.helpers.auth import login_required
from src.web.helpers import permissions

config_blueprint = Blueprint("config", __name__, url_prefix="/configuracion")


@config_blueprint.get("/")
@login_required
def config_index():
    permissions.is_admin()

    config = models.get_configuration()
    form = ConfigForm()
    form.payment_enabled.data = '1' if config.payment_enabled else '2'
    return render_template("config/index.html", config=config, form=form)


@config_blueprint.post("/editar_config")
@login_required
def config_edit():
    permissions.is_admin()

    form = ConfigForm()
    if form.validate_on_submit():
        config = models.update_configuration(form.elements_quantity.data,
                                             True if form.payment_enabled.data == '1' else False,
                                             form.contact_information.data, form.payment_header.data,
                                             form.monthly_fee.data, form.extra_charge.data)
        flash("Configuracion editada con exito", "success")
    else:
        print("WTF happened")
        for item in form.errors:
            for error in form[item].errors:
                print(f"{form[item].name}  {error}")

    return redirect(url_for("config.config_index"))
