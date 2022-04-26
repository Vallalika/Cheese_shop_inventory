from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.cheese_provision import CheeseProvision
from models.provider import Provider
from models.cheese import Cheese

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

# CREATE provision by cheese
@cheese_provisions_blueprint.route("/cheese_provisions/by-cheese/<cheese_id>", methods = ["POST"])
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

# All cheeses by provider
@cheese_provisions_blueprint.route("/cheese_provisions/<provider_id>/provisions_by_provider")
def provisions_by_provider(provider_id):
    provisions = cheese_provision_repository.select_by_provider_id(provider_id)
    provider = provider_repository.select(provider_id)
    return render_template("cheese_provisions/provisions_by_provider.html", provisions_by_provider=provisions, provider = provider)

# NEW by provider
@cheese_provisions_blueprint.route("/cheese_provisions/<provider_id>/new_by_provider")
def new_by_provider(provider_id):
    provider = provider_repository.select(provider_id)
    return render_template('cheese_provisions/new_by_provider.html', provider=provider)

# CREATE provision by provider
@cheese_provisions_blueprint.route("/cheese_provisions/by-provider/<provider_id>", methods = ["POST"])
def create_provision_by_provider(provider_id):

    # Getting provider object from relevant repo
    provider = provider_repository.select(provider_id)

    # Getting cheese data from form
    name = request.form["name"]
    origin = request.form["origin"]
    type = request.form["type"]
    description = request.form["description"]
    stock = request.form["stock"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    inventory_include = request.form["inventory_include"]

    # Creating cheese object from data and saving it to db
    cheese = Cheese(name, origin, type, description, stock, buying_cost, selling_price, inventory_include)
    cheese_repository.save(cheese)

    # Retrieving cheese from db
    cheese = cheese_repository.select(cheese.id)

    # Creating provision with cheese and provider objects, and saving it to db

    cheese_provision = CheeseProvision(cheese,provider)
    cheese_provision_repository.save(cheese_provision)

    # Getting all provisions to render relevant template
    provisions = cheese_provision_repository.select_by_provider_id(provider_id)

    # Rendering template with all data
    return render_template("cheese_provisions/provisions_by_provider.html", provider = provider, provisions_by_provider=provisions)

# # DELETE
# @providers_blueprint.route("/providers/<id>/delete", methods=["POST"])
# def delete_provider(id):
#     provider_repository.delete(id)
#     return redirect("/providers")