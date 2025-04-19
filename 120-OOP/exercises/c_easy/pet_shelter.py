class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def info(self):
        print(f'a {self.species} named {self.name}')

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def number_of_pets(self):
        return len(self.pets)
    
    def add_pet(self, pet):
        self.pets.append(pet)


class Shelter():
    def __init__(self):
        self.owners = {}
        self.petlist = [
            Pet('dog', 'Asta'),
            Pet('dog', 'Laddie'),
            Pet('cat', 'Fluffy'),
            Pet('cat', 'Kat'),
            Pet('cat', 'Ben'),
            Pet('parakeet', 'Chatterbox'),
            Pet('parakeet', 'Bluebell'),
            Pet('cat', 'Cocoa'), 
            Pet('cat', 'Cheddar'),
            Pet('bearded dragon', 'Darwin'),
            Pet('dog', 'Kennedy'),
            Pet('parakeet', 'Sweetie Pie'),
            Pet('dog', 'Molly'),
            Pet('fish', 'Chester')
        ]
    def adopted(self, pet):
        for animal in self.petlist:
            if (animal.species, animal.name) == (pet.species, pet.name):
                self.petlist.remove(animal)

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        self.adopted(pet)
        if owner not in self.owners:
                self.owners[owner] = owner
    
    def print_adoptions(self):
        for owner in self.owners.values():
            print(f'{owner.name} has adopted the following pets:')
            for pet in owner.pets:
                pet.info()
            print()
        
    def adoption_status(self):
        print('The Animal Shelter has the following unadopted pets:')
        
        for pet in self.petlist:
            pet.info()
        print()




cocoa   = Pet('cat', 'Cocoa') 
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.adoption_status()
shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")