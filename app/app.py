from flask import Flask, render_template

from controllers.cheeses_controller import cheeses_blueprint
from controllers.providers_controller import providers_blueprint
# from controllers.zombies_controller import zombies_blueprint

app = Flask(__name__)

app.register_blueprint(cheeses_blueprint)
app.register_blueprint(providers_blueprint)
# app.register_blueprint(zombies_blueprint)
# app.register_blueprint(zombie_types_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()