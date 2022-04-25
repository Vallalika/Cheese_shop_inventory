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

# cheese_provision_repository.delete(camembert_normandie.id)

# cheese_repository.delete(camembert.id)

# provider_repository.delete(normandie_farm.id)

camembert.name = "Camembert"
cheese_repository.update(camembert)

normandie_farm.name = "La Ferme Normande"
provider_repository.update(normandie_farm)

camembert_normandie.provider = normandie_farm
cheese_provision_repository.update(camembert_normandie)