class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} using {self.network_type} network...")

    def receive_call(self, caller):
        print(f"Receiving call from {caller}...")

    def take_a_picture(self):
        print(f"Taking a photo with {self.rear_camera} rear camera...")

class Apple(MobilePhone):
    def __init__(self, model, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_details(self):
        return f"Apple {self.model} | Front: {self.front_camera}, Rear: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}"

class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def get_details(self):
        sim_status = "Dual SIM" if self.dual_sim else "Single SIM"
        return f"Samsung {self.model} | {sim_status}, Front: {self.front_camera}, Rear: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}"
    
def main():
    # Apple phones
    iphone13 = Apple("iPhone 13", "12MP", "48MP", "4GB", "64GB")
    iphoneSE = Apple("iPhone SE", "8MP", "12MP", "3GB", "32GB")

    # Samsung phones
    galaxyS21 = Samsung("Galaxy S21", True, "16MP", "48MP", "4GB", "64GB")
    galaxyA52 = Samsung("Galaxy A52", False, "8MP", "32MP", "3GB", "32GB")

    print(iphone13.get_details())
    iphone13.make_call("9876543210")
    iphone13.take_a_picture()

    print("\n" + galaxyS21.get_details())
    galaxyS21.receive_call("Mom")
    galaxyS21.take_a_picture()

main()