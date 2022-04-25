from flask import Blueprint, Flask, redirect, render_template, request

from models.provider import Provider
import repositories.provider_repository as provider_repository

providers_blueprint = Blueprint("providers", __name__)

# INDEX
@providers_blueprint.route("/providers")
def index():
    providers = provider_repository.select_all()
    return render_template("providers/index.html", all_providers=providers)

# NEW
@providers_blueprint.route("/providers/new")
def new_provider():
    return render_template('providers/new.html')

# CREATE
@providers_blueprint.route("/providers", methods = ["POST"])
def create_provider():
    name = request.form["name"]
    type = request.form["type"]
    country = request.form["country"]
    address = request.form["address"]
    provider = Provider(name, type, country, address)
    provider_repository.save(provider)
    return redirect("/providers")

# EDIT
@providers_blueprint.route("/providers/<id>/edit")
def edit_provider(id):
    provider = provider_repository.select(id)
    return render_template('providers/edit.html', provider = provider)

# UPDATE
@providers_blueprint.route("/providers/<id>", methods = ['POST'])
def update_provider(id):
    name = request.form["name"]
    type = request.form["type"]
    country = request.form["country"]
    address = request.form["address"]
    provider = Provider(name, type, country, address, id)
    provider_repository.update(provider)
    return redirect("/providers")

# DELETE
@providers_blueprint.route("/providers/<id>/delete", methods=["POST"])
def delete_provider(id):
    provider_repository.delete(id)
    return redirect("/providers")