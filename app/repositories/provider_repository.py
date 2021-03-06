from db.run_sql import run_sql
from models.provider import Provider

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

def select(id):
    sql = "SELECT * FROM providers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    provider = Provider(result["name"], result["type"], result["country"], result["address"], result["id"])
    return provider

def select_all():
    providers = []
    sql = "SELECT * FROM providers"
    results = run_sql(sql)
    for result in results:
        provider = Provider(result["name"], result["type"],  result["country"],  result["address"], result["id"])
        providers.append(provider)
    return providers