from time import sleep
from src.core import board, auth


def run():

    pepe = auth.create_user(email="Pepe@gmail.com", password="1234")
    carlos = auth.create_user(email="Carlos@gmail.com", password="1234")
    cosme = auth.create_user(email="Cosme@gmail.com", password="1234")
