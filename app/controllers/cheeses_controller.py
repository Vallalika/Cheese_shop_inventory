from flask import Blueprint, Flask, redirect, render_template, request

from models.cheese import Cheese
import repositories.cheese_repository as cheese_repository

cheeses_blueprint = Blueprint("cheeses", __name__)

@cheeses_blueprint.route("/cheeses")
def index():
    cheeses = cheese_repository.select_all()
    return render_template("cheeses/index.html", all_cheeses=cheeses)