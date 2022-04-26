from flask import Blueprint, Flask, redirect, render_template, request

from models.cheese_provision import CheeseProvision
import repositories.cheese_provision_repository as cheese_provision_repository
import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository

cheese_provisions_blueprint = Blueprint("cheese_provisions", __name__)

# All providers per cheese
@cheese_provisions_blueprint.route("/cheese_provisions/<cheese_id>/provisions_by_cheese")
def provisions_by_cheese(cheese_id):
    provisions = cheese_provision_repository.select_by_cheese_id(cheese_id)
    for provision in provisions:
        print(provision.__dict__)
    cheese = cheese_repository.select(cheese_id)
    return render_template("cheese_provisions/provisions_by_cheese.html", provisions_by_cheese=provisions, cheese = cheese)

# NEW
@cheese_provisions_blueprint.route("/cheese_provisions/new_by_cheese")
def new_provision_by_cheese(id):
    cheese = cheese_repository.select(id)
    provider = provider_repository.save()
    provision = CheeseProvision(cheese,provider)
    cheese_provision_repository.save(provision)
    return render_template('cheese_provisions/new_by_cheese.html')

# # CREATE
# @providers_blueprint.route("/providers", methods = ["POST"])
# def create_provider():
#     name = request.form["name"]
#     type = request.form["type"]
#     country = request.form["country"]
#     address = request.form["address"]
#     provider = Provider(name, type, country, address)
#     provider_repository.save(provider)
#     return redirect("/providers")

# # EDIT
# @providers_blueprint.route("/providers/<id>/edit")
# def edit_provider(id):
#     provider = provider_repository.select(id)
#     return render_template('providers/edit.html', provider = provider)

# # UPDATE
# @providers_blueprint.route("/providers/<id>", methods = ['POST'])
# def update_provider(id):
#     name = request.form["name"]
#     type = request.form["type"]
#     country = request.form["country"]
#     address = request.form["address"]
#     provider = Provider(name, type, country, address, id)
#     provider_repository.update(provider)
#     return redirect("/providers")

# # DELETE
# @providers_blueprint.route("/providers/<id>/delete", methods=["POST"])
# def delete_provider(id):
#     provider_repository.delete(id)
#     return redirect("/providers")