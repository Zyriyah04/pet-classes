# Dream Pet Adoption Center Python Version

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_care_tip(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_type(self):
        return "Pet"

    def display_info(self):
        print(f"Type: {self.get_type()}")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Sound: {self.make_sound()}")
        print(f"Care Tip: {self.get_care_tip()}")
        print("-" * 30)


class Bunny(Pet):
    def make_sound(self):
        return "sniff sniff"

    def get_care_tip(self):
        return "Keep fresh hay and give gentle play time."

    def get_type(self):
        return "Bunny"


class Cat(Pet):
    def make_sound(self):
        return "meow"

    def get_care_tip(self):
        return "Provide scratching spots and cozy nap areas."

    def get_type(self):
        return "Cat"


class Dog(Pet):
    def make_sound(self):
        return "woof"

    def get_care_tip(self):
        return "Daily walks and playful exercise are important."

    def get_type(self):
        return "Dog"


class AdoptionCenter:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"\n{pet.get_name()} was added successfully.\n")

    def show_pets(self):
        if not self.pets:
            print("\nNo pets have been added yet.\n")
            return

        print("\nAvailable Pets")
        print("=" * 30)
        for pet in self.pets:
            pet.display_info()


def create_pet():
    print("\nChoose a pet type:")
    print("1. Bunny")
    print("2. Cat")
    print("3. Dog")

    choice = input("Enter choice: ").strip()
    name = input("Enter pet name: ").strip()

    if not name:
        print("Name cannot be empty.\n")
        return None

    try:
        age = int(input("Enter pet age: ").strip())
        if age <= 0:
            print("Age must be greater than 0.\n")
            return None
    except ValueError:
        print("Please enter a valid number for age.\n")
        return None

    if choice == "1":
        return Bunny(name, age)
    elif choice == "2":
        return Cat(name, age)
    elif choice == "3":
        return Dog(name, age)
    else:
        print("Invalid pet type.\n")
        return None


def main():
    center = AdoptionCenter()

    while True:
        print("Dream Pet Adoption Center")
        print("1. Add a pet")
        print("2. View all pets")
        print("3. Exit")

        menu_choice = input("Choose an option: ").strip()

        if menu_choice == "1":
            pet = create_pet()
            if pet:
                center.add_pet(pet)

        elif menu_choice == "2":
            center.show_pets()

        elif menu_choice == "3":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid option. Try again.\n")


main()
