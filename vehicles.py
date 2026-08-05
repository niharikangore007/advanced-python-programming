


class Vehicle:
   

    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

        # Categorize vehicle based on price
        if self.price >= 1000000:
            self.category = "Luxury"
        else:
            self.category = "Economy"

    def display(self):
       
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Price          : ₹{self.price}")
        print(f"Category       : {self.category}")
        print("-" * 40)




class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
       
        self.vehicles.append(vehicle)
        print(f"{vehicle.brand} added successfully!\n")

    def display_vehicles(self):
       

        if len(self.vehicles) == 0:
            print("No vehicles available in the showroom.")
            return

        print("\n VEHICLE DETAILS \n")

        for vehicle in self.vehicles:
            vehicle.display()



showroom = Showroom()

# Creating Vehicle Objects
v1 = Vehicle("MH12AB1234", "BMW", 6500000)
v2 = Vehicle("MH14CD5678", "Maruti Suzuki", 650000)
v3 = Vehicle("MH20EF9012", "Mercedes", 8500000)
v4 = Vehicle("MH01GH3456", "Hyundai", 900000)

# Adding Vehicles to Showroom
showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)
showroom.add_vehicle(v4)

# Display All Vehicles
showroom.display_vehicles()