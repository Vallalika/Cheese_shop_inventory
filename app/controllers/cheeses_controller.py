from flask import Blueprint, Flask, redirect, render_template, request

from models.cheese import Cheese
import repositories.cheese_repository as cheese_repository

cheeses_blueprint = Blueprint("cheeses", __name__)

# INDEX
@cheeses_blueprint.route("/cheeses")
def index():
    cheeses = cheese_repository.select_all()
    return render_template("cheeses/index.html", all_cheeses=cheeses)

# NEW
@cheeses_blueprint.route("/cheeses/new")
def new_cheese():
    return render_template('cheeses/new.html')

# CREATE
@cheeses_blueprint.route("/cheeses", methods = ["POST"])
def create_cheese():
    name = request.form["name"]
    origin = request.form["origin"]
    type = request.form["type"]
    description = request.form["description"]
    stock = request.form["stock"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    inventory_include = request.form["inventory_include"]
    cheese = Cheese(name, origin, type, description, stock, buying_cost, selling_price, inventory_include)
    cheese_repository.save(cheese)
    return redirect("/cheeses")

# EDIT
@cheeses_blueprint.route("/cheeses/<id>/edit")
def edit_cheese(id):
    cheese = cheese_repository.select(id)
    return render_template('cheeses/edit.html', cheese = cheese)

# UPDATE
@cheeses_blueprint.route("/cheeses/<id>", methods = ['POST'])
def update_cheese(id):
    name = request.form["name"]
    origin = request.form["origin"]
    type = request.form["type"]
    description = request.form["description"]
    stock = request.form["stock"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    inventory_include = request.form["inventory_include"]
    cheese = Cheese(name, origin, type, description, stock, buying_cost, selling_price, inventory_include, id)
    cheese_repository.update(cheese)
    return redirect("/cheeses")

# DELETE
@cheeses_blueprint.route("/cheeses/<id>/delete", methods=["POST"])
def delete_cheese(id):
    cheese_repository.delete(id)
    return redirect("/cheeses")