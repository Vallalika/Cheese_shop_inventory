from models.cheese import Cheese
from models.provider import Provider
from models.cheese_provision import CheeseProvision

import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository
import repositories.cheese_provision_repository as cheese_provision_repository

cheese_provision_repository.delete_all()
cheese_repository.delete_all()
provider_repository.delete_all()

camembert = Cheese("Camembert", "France", "Raw Cow's Milk", "Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", 20, 5.00, 8.00)
cheese_repository.save(camembert)

normandie_farm = Provider("La Ferme Normande", "Farmer", "France", "A Normandy village")
provider_repository.save(normandie_farm)

camembert_normandie = CheeseProvision(camembert, normandie_farm)
cheese_provision_repository.save(camembert_normandie)