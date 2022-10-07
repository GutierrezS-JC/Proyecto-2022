from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, BooleanField, \
    SelectMultipleField, widgets, EmailField, HiddenField


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegisterUserForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=50)])
    username = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=5, max=20)])
    first_name = StringField('Nombre', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Apellido', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=8)])
    status = SelectField('Estado', choices=[('1', 'Activo'), ('2', 'Inactivo')], default="1")
    roles = MultiCheckboxField('Roles', choices=[('1', 'Admin'), ('2', 'Operador')])

    submit = SubmitField("Crear Usuario")


class EditUserForm(FlaskForm):
    user_id = HiddenField('user_id')
    email = StringField('Email', validators=[Email(), Length(max=50)])
    username = StringField('Nombre de usuario', validators=[Length(min=5, max=20)])
    first_name = StringField('Nombre', validators=[Length(max=50)])
    last_name = StringField('Apellido', validators=[Length(max=50)])
    roles = MultiCheckboxField('Roles', coerce=int, choices=[('1', 'Admin'), ('2', 'Operador')])

    submit = SubmitField("Guardar cambios")
