from db.run_sql import run_sql
from models.cheese import Cheese

def save(cheese):
    sql = "INSERT INTO cheeses (name, origin, type, description, stock, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [cheese.name, cheese.origin, cheese.type, cheese.description, cheese.stock, cheese.buying_cost, cheese.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    cheese.id = id

# def select_all():
#     humans = []
#     sql = "SELECT * FROM humans"
#     results = run_sql(sql)
#     for result in results:
#         human = Human(result["name"], result["id"])
#         humans.append(human)
#     return humans


# def select(id):
#     sql = "SELECT * FROM humans WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     human = Human(result["name"], result["id"])
#     return human


# def delete_all():
#     sql = "DELETE FROM humans"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM humans WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(human):
#     sql = "UPDATE humans SET name = %s WHERE id = %s"
#     values = [human.name, human.id]
#     run_sql(sql, values)