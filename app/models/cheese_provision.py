import repositories.cheese_repository as cheese_repository

class CheeseProvision():
    
    def __init__(self, cheese, provider, id = None):
        self.cheese = cheese
        self.provider = provider
        self.id = id