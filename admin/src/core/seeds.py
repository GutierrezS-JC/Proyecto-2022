from core import board


def run():
    issue1 = board.create_issue(
        email= "Pepe@gmail.com",
        title= "No puedo dar de alta a un socio",
        description= "Siempre que le doy a aceptar me sale un cartel que dice 'NULL'",
        status= "New",
    )
    issue2 = board.create_issue(
        email= "Carlos@gmail.com",
        title= "Mi computadora exploto",
        description= "Cuando hice click en Iniciar Sesion",
        status= "New",
    )
    issue3 = board.create_issue(
        email= "Cosme@gmail.com",
        title= "Las disciplinas no existen y no se pueden crear",
        description= "Eso.",
        status= "New",
    )
