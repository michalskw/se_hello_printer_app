from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Natalia"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    imie = request.args.get('name')
    if not output:
        output = PLAIN
    if imie:
        imie = moje_imie
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
