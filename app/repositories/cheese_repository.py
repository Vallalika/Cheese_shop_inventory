from db.run_sql import run_sql
from models.cheese import Cheese

def save(cheese):
    sql = "INSERT INTO cheeses (name, origin, type, description, stock, buying_cost, selling_price, inventory_include) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [cheese.name, cheese.origin, cheese.type, cheese.description, cheese.stock, cheese.buying_cost, cheese.selling_price, cheese.inventory_include]
    results = run_sql(sql, values)
    id = results[0]['id']
    cheese.id = id

def delete_all():
    sql = "DELETE FROM cheeses"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cheeses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(cheese):
    sql = "UPDATE cheeses SET (name, origin, type, description, stock, buying_cost, selling_price, inventory_include) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [cheese.name, cheese.origin, cheese.type, cheese.description, cheese.stock, cheese.buying_cost, cheese.selling_price, cheese.inventory_include, cheese.id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM cheeses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    cheese = Cheese(result["name"], result["origin"], result["type"], result["description"], result["stock"], result["buying_cost"],result["selling_price"],result["inventory_include"], result["id"])
    return cheese

def select_all():
    cheeses = []
    sql = "SELECT * FROM cheeses ORDER BY stock"
    results = run_sql(sql)
    for result in results:
        cheese = Cheese(result["name"], result["origin"], result["type"], result["description"], result["stock"], result["buying_cost"],result["selling_price"], result["inventory_include"], result["id"])
        cheeses.append(cheese)
    return cheeses