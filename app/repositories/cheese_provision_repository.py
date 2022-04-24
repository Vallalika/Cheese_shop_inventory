from db.run_sql import run_sql

def save(cheese_provision):
    sql = "INSERT INTO cheese_provisions (cheese_id, provider_id) VALUES (%s, %s) RETURNING id"
    values = [cheese_provision.cheese.id, cheese_provision.provider.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    cheese_provision.id = id

def delete_all():
    sql = "DELETE FROM cheese_provisions"
    run_sql(sql)

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