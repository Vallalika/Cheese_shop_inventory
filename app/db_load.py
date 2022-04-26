from models.cheese import Cheese
from models.provider import Provider
from models.cheese_provision import CheeseProvision

import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository
import repositories.cheese_provision_repository as cheese_provision_repository

cheese_provision_repository.delete_all()
cheese_repository.delete_all()
provider_repository.delete_all()

camembert = Cheese("camembert", "France", "Raw Cow's Milk", "Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", 20, 5.00, 8.00)
cheese_repository.save(camembert)

normandie_farm = Provider("Normandy is a pretty place", "Farmer", "France", "A Normandy village")
provider_repository.save(normandie_farm)

brittany_farm = Provider("Brittany's a great holiday place", "Souvenirs shop", "France", "A Breton village")

camembert_normandie = CheeseProvision(camembert, brittany_farm)
cheese_provision_repository.save(camembert_normandie)

cheddar = Cheese("Cheddar", "United Kingdom", "Pasteurized Cow's Milk", "Hard cheese, off-white or orange, and sometimes sharp-tasting.", 5, 8.00, 14.00)
cheese_repository.save(cheddar)

somerset_farm = Provider("The Somerset Cheddar Farm", "Farmer", "England", "A village in Somerset")
provider_repository.save(somerset_farm)

cheddar_somerset = CheeseProvision(cheddar, somerset_farm)
cheese_provision_repository.save(cheddar_somerset)

# cheese_provision_repository.delete(camembert_normandie.id)

# cheese_repository.delete(camembert.id)

# provider_repository.delete(normandie_farm.id)

camembert.name = "Camembert"
cheese_repository.update(camembert)

normandie_farm.name = "La Ferme Normande"
provider_repository.update(normandie_farm)

camembert_normandie.provider = normandie_farm
cheese_provision_repository.update(camembert_normandie)

# my_cheese = cheese_repository.select(camembert.id)
# print(my_cheese.__dict__)

# my_provider = provider_repository.select(normandie_farm.id)
# print(my_provider.__dict__)

# my_provision = cheese_provision_repository.select(camembert_normandie.id)
# print("Here's my provision dict", my_provision.__dict__)
# print("Here's the cheese name", my_provision.cheese.name)
# print("Here's the provider name", my_provision.provider.name)

# cheeses = cheese_repository.select_all()

# for cheese in cheeses:
#     print(cheese.__dict__)

# providers = provider_repository.select_all()

# for provider in providers:
#     print(provider.__dict__)

# cheese_provisions = cheese_provision_repository.select_all()
# for provision in cheese_provisions:
#     print(provision.__dict__)
#     print(provision.cheese.name)
#     print(provision.provider.name)

### TEST for selecting providers by cheese ID

french_importer = Provider("Fromage Import", "Importer", "France", "Paris")
provider_repository.save(french_importer)

camembert_import = CheeseProvision(camembert, french_importer)
cheese_provision_repository.save(camembert_import)

providers = cheese_provision_repository.select_by_cheese_id(camembert.id)

for provider in providers:
    print(provider.cheese.name, provider.provider.name)