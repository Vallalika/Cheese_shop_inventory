from db.run_sql import run_sql
from models.cheese_provision import CheeseProvision
import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository

def save(cheese_provision):
    sql = "INSERT INTO cheese_provisions (cheese_id, provider_id) VALUES (%s, %s) RETURNING id"
    values = [cheese_provision.cheese.id, cheese_provision.provider.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    cheese_provision.id = id

def delete_all():
    sql = "DELETE FROM cheese_provisions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cheese_provisions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(cheese_provision):
    sql = "UPDATE cheese_provisions SET (cheese_id, provider_id) = (%s, %s) WHERE id = %s"
    values = [cheese_provision.cheese.id, cheese_provision.provider.id, cheese_provision.id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM cheese_provisions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    cheese = cheese_repository.select(result["cheese_id"])
    provider = provider_repository.select(result["provider_id"])
    cheese_provision = CheeseProvision(cheese, provider, result["id"])
    return cheese_provision

def select_all():
    provisions = []
    sql = "SELECT * FROM cheese_provisions"
    results = run_sql(sql)
    for result in results:
        cheese = cheese_repository.select(result["cheese_id"])
        provider = provider_repository.select(result["provider_id"])
        provision = CheeseProvision(cheese, provider, result["id"])
        provisions.append(provision)
    return provisions

def select_by_cheese_id(cheese_id):
    provisions = []
    sql = "SELECT * FROM cheese_provisions WHERE cheese_id = %s"
    values = [cheese_id]
    results = run_sql(sql, values)
    for result in results:
        cheese = cheese_repository.select(cheese_id)
        provider = provider_repository.select(result["provider_id"])
        provision = CheeseProvision(cheese, provider, result["id"])
        provisions.append(provision)
    return provisions

def select_by_provider_id(provider_id):
    # Create an empty list to append query results
    provisions = []

    # Get all cheeses provided by the same provider
    sql = "SELECT * FROM cheese_provisions WHERE provider_id = %s"
    values = [provider_id]

    # Store cheese by provider in results
    results = run_sql(sql, values)

    # For each cheese in the results
    for result in results:
        
        # Get the provider as an object
        provider = provider_repository.select(provider_id)

        # Get the cheese as an object using its id
        cheese = cheese_repository.select(result["cheese_id"])

        # Create provision using both cheese and provider objects
        provision = CheeseProvision(cheese, provider, result["id"])

        # Append provision to our provision list
        provisions.append(provision)
    
    # Return our list of provisions
    return provisions