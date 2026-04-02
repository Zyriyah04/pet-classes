public abstract class Pet {
    private String name;
    private int age;

    public Pet(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }

    public abstract String makeSound();
    public abstract String getCareTip();

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Sound: " + makeSound());
        System.out.println("Care Tip: " + getCareTip());
        System.out.println("--------------------------");
    }
}

class Bunny extends Pet {
    public Bunny(String name, int age) {
        super(name, age);
    } {
    
}@Override
    public String makeSound() {
        return "sniff sniff";
    }

    @Override
    public String getCareTip() {
        return "Keep fresh hay and give gentle play time.";
    }
}

class Cat extends Pet {
    public Cat(String name, int age) {
        super(name, age);
    }

    @Override
    public String makeSound() {
        return "meow";
    }

    @Override
    public String getCareTip() {
        return "Provide scratching spots and quiet nap spaces.";
    }
}

class Dog extends Pet {
    public Dog(String name, int age) {
        super(name, age);
    }

    @Override
    public String makeSound() {
        return "woof";
    }

    @Override public String getCareTip() {
        return "Daily walks and playful exercise are important.";
    }
}

class AdoptionCenter {
    private Pet[] pets;

    public AdoptionCenter(Pet[] pets) {
        this.pets = pets;
    }

    public void showAllPets() {
        System.out.println("🌟 Available Magical Pets 🌟");
        for (Pet pet : pets) {
            pet.displayInfo();
        }
    }
}

