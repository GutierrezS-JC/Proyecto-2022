from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email, Optional
from wtforms import StringField, IntegerField, SubmitField, SelectField, PasswordField, \
    SelectMultipleField, widgets, EmailField, HiddenField, TextAreaField


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
    email = StringField('Email', validators=[Email(), Length(max=50)], id='email_edit')
    username = StringField('Nombre de usuario', validators=[Length(min=5, max=20)])
    first_name = StringField('Nombre', validators=[Length(max=50)])
    last_name = StringField('Apellido', validators=[Length(max=50)])
    roles = MultiCheckboxField('Roles', coerce=int, choices=[('1', 'Admin'), ('2', 'Operador')])

    submit = SubmitField("Guardar cambios")


class ConfigForm(FlaskForm):
    elements_quantity = StringField('Cantidad de elementos', validators=[InputRequired()])
    payment_enabled = SelectField('Habilitar/deshabilitar tabla de pagos',
                                  choices=[('1', 'Habilitado'), ('2', 'Deshabilitado')], default="1")
    contact_information = TextAreaField('Informacion de contacto', validators=[InputRequired(), Length(max=200)])
    payment_header = StringField('Encabezado', validators=[InputRequired(), Length(min=5, max=50)])
    monthly_fee = StringField('Cuota base', validators=[InputRequired()])
    extra_charge = IntegerField('Porcentaje de recargo', validators=[InputRequired()])

    submit = SubmitField("Guardar cambios")


class MemberForm(FlaskForm):
    first_name = StringField('Nombre', validators=[InputRequired(), Length(max=50)])
    last_name = StringField('Apellido', validators=[InputRequired(), Length(max=50)])
    doc_type = SelectField('Tipo de documento', choices=[('1', 'DNI'), ('2', 'LE'), ('3', 'LC')], default="1")
    doc_num = StringField('Nro de documento', validators=[InputRequired()])
    genre = SelectField('Genero', choices=[('1', 'M'), ('2', 'F'), ('3', 'Otro')], default="1")
    member_num = StringField('Numero de socio', validators=[Length(max=50)])  # Revisar este
    address = StringField('Direccion', validators=[InputRequired()])
    is_active = SelectField('Estado', choices=[('1', 'Activo'), ('2', 'Inactivo')], default="1")
    phone_num = StringField('Telefono (Opcional)', validators=[Optional()])
    email = EmailField('Email (Opcional)', validators=[Length(max=50), Optional()])

    submit = SubmitField("Cargar socio")


class EditMemberForm(FlaskForm):
    member_id_edit = HiddenField('member_id')
    first_name_edit = StringField('Nombre', validators=[Length(max=50)])
    last_name_edit = StringField('Apellido', validators=[Length(max=50)])
    genre_edit = SelectField('Genero', choices=[('1', 'M'), ('2', 'F'), ('3', 'Otro')], default="1")
    address_edit = StringField('Direccion')
    is_active_edit = SelectField('Estado', choices=[('1', 'Activo'), ('0', 'Inactivo')], default="1")
    phone_num_edit = StringField('Telefono (Opcional)', validators=[Optional()])
    email_edit = EmailField('Email (Opcional)', validators=[Length(max=50), Optional()])

    submit_edit = SubmitField("Guardar cambios")


class SearchUserForm(FlaskForm):
    email = StringField('Email', validators=[Length(max=50), Optional()], name="email")
    is_active_search = SelectField('Estado', choices=[('2', 'Todos'), ('1', 'Activo'), ('0', 'Bloqueado')], default="2",
                                   name="status")

    submit_search = SubmitField("Buscar")


class SearchMemberForm(FlaskForm):
    last_name = StringField('Apellido', validators=[Length(max=50), Optional()], name="apellido")
    is_active_search = SelectField('Estado', choices=[('2', 'Todos'), ('1', 'Activo'), ('0', 'Bloqueado')], default="2",
                                   name="status")

    submit_search = SubmitField("Buscar")


# Discipline Forms
class DisciplineForm(FlaskForm):
    name = StringField('Nombre', validators=[InputRequired(), Length(max=50)])
    category = StringField('Categoria', validators=[InputRequired(), Length(max=50)])
    instructors = StringField('Instructores', validators=[InputRequired()])
    days_hours = StringField('Dias y horarios', validators=[InputRequired()])
    monthly_fee = StringField('Costo mensual', validators=[InputRequired()])
    is_active = SelectField('Estado', choices=[('1', 'Habilitado'), ('2', 'Deshabilitado')], default="1")

    submit = SubmitField("Cargar Disciplina")


class EditDisciplineForm(FlaskForm):
    discipline_id_edit = HiddenField('discipline_id')
    name_edit = StringField('Nombre', validators=[InputRequired(), Length(max=50)])
    category_edit = StringField('Categoria', validators=[InputRequired(), Length(max=50)])
    instructors_edit = StringField('Instructores', validators=[InputRequired()])
    days_hours_edit = StringField('Dias y horarios', validators=[InputRequired()])
    monthly_fee_edit = StringField('Costo mensual', validators=[InputRequired()])
    is_active_edit = SelectField('Estado', choices=[('1', 'Activo'), ('0', 'Inactivo')], default="1")

    submit_edit = SubmitField("Guardar cambios")


class SearchDisciplineForm(FlaskForm):
    discipline_name = StringField('Disciplina', validators=[Length(max=50), Optional()], name="disciplina")
    is_active_search = SelectField('Estado', choices=[('2', 'Todos'), ('1', 'Activo'), ('0', 'Bloqueado')], default="2",
                                   name="status")

    submit_search = SubmitField("Buscar")


class SearchMemberForDisciplineForm(FlaskForm):
    input = StringField('Nombre de socio', validators=[Length(max=50), InputRequired()],
                        name="inputBusqueda")
    discipline_id_add = discipline_id_edit = HiddenField('discipline_id')
    member_id_add = HiddenField('member_id')

    submit_search = SubmitField("Buscar")


class PaymentSearchForm(FlaskForm):
    input_search = StringField('Apellido/Nro de socio', validators=[Length(max=50)])

    submit_search = SubmitField("Buscar")
