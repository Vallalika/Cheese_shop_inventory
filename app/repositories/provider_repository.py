from db.run_sql import run_sql

def save(provider):
    sql = "INSERT INTO providers (name, type, country, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [provider.name, provider.type, provider.country, provider.address]
    results = run_sql(sql, values)
    id = results[0]['id']
    provider.id = id

def delete_all():
    sql = "DELETE FROM providers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM providers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(provider):
    sql = "UPDATE providers SET (name, type, country, address) = (%s, %s, %s, %s) WHERE id = %s"
    values = [provider.name, provider.type, provider.country, provider.address, provider.id]
    run_sql(sql, values)

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