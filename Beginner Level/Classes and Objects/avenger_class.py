class Avenger:
    def __init__(self, name, age, gender, superpower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
    
    def display_info(self):
        info = f"Name: {self.name}\n Age: {self.age} \n Gender: {self.gender}\n Superpower: {self.superpower}\n Weapon: {self.weapon}"
        return info
    
    def is_leader(self):
        return self.name == "Iron Man"
    
def main():
    super_heroes = [
    Avenger("Captain America", 105, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 38, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", None),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 45, "Male", "Fighting skills", "Bow and Arrows")
]
    for hero in super_heroes:
        print(hero.display_info())
        print("Leader Status:", "Yes" if hero.is_leader() else "No")
        print("-" * 40)

main()