from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.cheese_provision import CheeseProvision
from models.provider import Provider
import repositories.cheese_provision_repository as cheese_provision_repository
import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository

cheese_provisions_blueprint = Blueprint("cheese_provisions", __name__)

# All providers by cheese
@cheese_provisions_blueprint.route("/cheese_provisions/<cheese_id>/provisions_by_cheese")
def provisions_by_cheese(cheese_id):
    provisions = cheese_provision_repository.select_by_cheese_id(cheese_id)
    cheese = cheese_repository.select(cheese_id)
    return render_template("cheese_provisions/provisions_by_cheese.html", provisions_by_cheese=provisions, cheese = cheese)

# NEW by cheese
@cheese_provisions_blueprint.route("/cheese_provisions/<cheese_id>/new_by_cheese")
def new_by_cheese(cheese_id):
    cheese = cheese_repository.select(cheese_id)
    return render_template('cheese_provisions/new_by_cheese.html', cheese=cheese)

# CREATE provider by cheese
@cheese_provisions_blueprint.route("/cheese_provisions/<cheese_id>", methods = ["POST"])
def create_provision_by_cheese(cheese_id):

    # Getting cheese object from relevant repo
    cheese = cheese_repository.select(cheese_id)

    # Getting provider data from form
    name = request.form["name"]
    type = request.form["type"]
    country = request.form["country"]
    address = request.form["address"]

    # Creating provider object from data and saving it to db
    provider = Provider(name, type, country, address)
    provider_repository.save(provider)

    # Creating provision with cheese and provider objects, and saving it to db
    cheese_provision = CheeseProvision(cheese,provider)
    cheese_provision_repository.save(cheese_provision)

    # Getting all provisions to render relevant template
    provisions = cheese_provision_repository.select_by_cheese_id(cheese_id)

    # Rendering template with all data
    return render_template("cheese_provisions/provisions_by_cheese.html", cheese = cheese, provisions_by_cheese=provisions)

# # DELETE
# @providers_blueprint.route("/providers/<id>/delete", methods=["POST"])
# def delete_provider(id):
#     provider_repository.delete(id)
#     return redirect("/providers")