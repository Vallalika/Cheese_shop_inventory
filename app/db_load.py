from models.cheese import Cheese
from models.provider import Provider
from models.cheese_provision import CheeseProvision

import repositories.cheese_repository as cheese_repository
import repositories.provider_repository as provider_repository
import repositories.cheese_provision_repository as cheese_provision_repository

# from models.human import Human
# import repositories.human_repository as human_repository

# from models.zombie import Zombie
# import repositories.zombie_repository as zombie_repository

# from models.zombie_type import ZombieType
# import repositories.zombie_type_repository as zombie_type_repository

# biting_repository.delete_all()
# human_repository.delete_all()
# zombie_repository.delete_all()
# zombie_type_repository.delete_all()

camembert = Cheese("Camembert", "France", "Raw Cow's Milk", "Fine velvety rind marked by brown-red streaks. Light yellow interior. Supple texture. Aromas of forest floor, mushroom and earth after ripening. Milky and tart notes.", 20, 5.00, 8.00)
cheese_repository.save(camembert)

normandie_farm = Provider("La Ferme Normande", "Farmer", "France", "A Normandy village")
provider_repository.save(normandie_farm)

camembert_normandie = CheeseProvision(camembert, normandie_farm)
cheese_provision_repository.save(camembert_normandie)

# human_2 = Human("Coach")
# human_repository.save(human_2)

# human_3 = Human("Nick")
# human_repository.save(human_3)

# human_4 = Human("Ellis")
# human_repository.save(human_4)

# zombie_type_1 = ZombieType("Walker")
# zombie_type_repository.save(zombie_type_1)

# zombie_type_2 = ZombieType("Crawler")
# zombie_type_repository.save(zombie_type_2)

# zombie_type_3 = ZombieType("Runner")
# zombie_type_repository.save(zombie_type_3)

# zombie_1 = Zombie("Ed", zombie_type_2)
# zombie_repository.save(zombie_1)

# zombie_2 = Zombie("Pete", zombie_type_1)
# zombie_repository.save(zombie_2)

# biting_1 = Biting(human_2, zombie_2)
# biting_repository.save(biting_1)

# biting_2 = Biting(human_3, zombie_1)
# biting_repository.save(biting_2)

# biting_3 = Biting(human_3, zombie_2)
# biting_repository.save(biting_3)

# biting_4 = Biting(human_4, zombie_2)
# biting_repository.save(biting_4)