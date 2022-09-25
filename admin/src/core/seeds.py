from time import sleep
from src.core import board, auth


def run():
    issue1 = board.create_issue(
        email="Pepe@gmail.com",
        title="No puedo dar de alta a un socio",
        description="Siempre que le doy a aceptar me sale un cartel que dice 'NULL'",
        status="New",
    )
    issue2 = board.create_issue(
        email="Carlos@gmail.com",
        title="Mi computadora exploto",
        description="Cuando hice click en Iniciar Sesion",
        status="New",
    )
    issue3 = board.create_issue(
        email="Cosme@gmail.com",
        title="Las disciplinas no existen y no se pueden crear",
        description="Eso.",
        status="New",
    )

    pepe = auth.create_user(email="Pepe@gmail.com", password="1234")
    carlos = auth.create_user(email="Carlos@gmail.com", password="1234")
    cosme = auth.create_user(email="Cosme@gmail.com", password="1234")

    label1 = board.create_label(
        title="Urgente",
        description="Issues que tienen que resolverse dentro de las 24 horas"
    )
    label2 = board.create_label(
        title="Importante",
        description="Issues de alta prioridad"
    )
    label3 = board.create_label(
        title="Soporte",
        description="Issues relacionados con soporte tecnico"
    )
    label4 = board.create_label(
        title="Ventas",
        description="Issues relacionados con el area de ventas"
    )

    sleep(2)

    board.assign_user(issue1, pepe)
    board.assign_user(issue2, carlos)
    board.assign_user(issue3, cosme)

    board.assign_labels(issue1, [label1, label2])
    board.assign_labels(issue2, [label3, label4])
    board.assign_labels(issue3, [label1, label4])
