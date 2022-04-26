from flask import Flask, render_template

from controllers.cheeses_controller import cheeses_blueprint
from controllers.providers_controller import providers_blueprint
from controllers.cheese_provisions_controller import cheese_provisions_blueprint

import repositories.cheese_repository as cheese_repository

app = Flask(__name__)

app.register_blueprint(cheeses_blueprint)
app.register_blueprint(providers_blueprint)
app.register_blueprint(cheese_provisions_blueprint)

@app.route("/")
def main():
    cheeses = cheese_repository.select_all()
    return render_template("index.html", all_cheeses=cheeses)

if __name__ == '__main__':
    app.run()