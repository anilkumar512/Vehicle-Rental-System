'''
Vehicle Rental System

Description: Manage a vehicle rental service with options for renting cars, bikes, etc.

Features:

Abstract class Vehicle with methods like rent() and return_vehicle().

Subclasses: Car, Bike, Truck.

Polymorphism for rental rates based on vehicle type.

'''
from abc import ABC,abstractmethod
from time import sleep
class Vehicle(ABC):

    @abstractmethod
    def rent(self):
        ...

    @abstractmethod
    def return_vehicle(self):
        ...

class Bike(Vehicle):
    fare=300
    def rent(self):
        sleep(1)
        print('Successfully Rented Bike...')

    def return_vehicle(self,hours):
        self.rent_amount=hours*self.fare
        sleep(0.5)
        print(f'Amount to pay is : {self.rent_amount}')
        sleep(0.5)
        print('Thank you Visit Again ...')

class Car(Vehicle):
    fare=500
    def rent(self):
        sleep(1)
        print('Successfully Rented Car...')

    def return_vehicle(self,hours):
        self.rent_amount=hours*self.fare
        sleep(0.5)
        print(f'Amount to pay is : {self.rent_amount}')
        sleep(0.5)
        print('Thank you Visit Again ...')

class Truck(Vehicle):
    fare=1000
    def rent(self):
        sleep(1)
        print('Successfully Rented Truck...')

    def return_vehicle(self,hours):
        self.rent_amount=hours*self.fare
        sleep(0.5)
        print(f'Amount to pay is : {self.rent_amount}')
        sleep(0.5)
        print('Thank you Visit Again ...')



def VehicleRentalSystem(): 
    bikes, cars, trucks = 10, 7, 5
    rented_vehicles = {'bike': 0, 'car': 0, 'truck': 0}
    vehicles = {1: ('bike', Bike()), 2: ('car', Car()), 3: ('truck', Truck())}       
    while True:
        sleep(0.5)
        print('Welcome to QuickRide')
        sleep(1)
        print('Here are your options')
        sleep(0.4)
        print('1. To Rent a Vehicle')
        sleep(0.4)
        print('2. To Return a Vehicle')
        sleep(0.4)
        print('3. To Check Status of Rented Vehicles')
        sleep(0.4)
        print('0. To Exit')
        sleep(1)
        choice=int(input('Enter your choice:'))
        if choice==1:
            sleep(0.5)
            print('Choose the vehicle:\n1. Bike\n2. Car\n3. Truck')
            sleep(0.5)
            option=int(input('Enter your option:'))
            if option in vehicles:
                vehicle_type,vehicle_obj=vehicles[option]
                if vehicle_type=='bike' and bikes>0:
                    bikes-=1
                    rented_vehicles['bike']+=1
                    vehicle_obj.rent()

                elif vehicle_type=='car' and cars>0:
                    cars-=1
                    rented_vehicles['car']+=1
                    vehicle_obj.rent()
                elif vehicle_type=='truck' and trucks>0:
                    trucks-=1
                    rented_vehicles['truck']+=1
                    vehicle_obj.rent()
                else:
                    print(f"Sorry! {vehicle_type}s are unavailable")
            else:
                print('Invalid Option!')


        elif choice==2:
            print('Choose the vehicle:\n1. Bike\n2. Car\n3. Truck')
            option=int(input('Enter your option:'))
            if option in vehicles:
                vehicle_type,vehicle_obj=vehicles[option]
                if rented_vehicles[vehicle_type]>0:
                    hrs=int(input('Enter the hours:'))
                    vehicle_obj.return_vehicle(hrs)
                    rented_vehicles[vehicle_type]-=1
                    if vehicle_type=='bike':
                        bikes+=1
                    elif vehicle_type=='car':
                        cars+=1
                    else:
                        trucks+=1
                else:
                    print(f"You haven't rented any {vehicle_type}")
            else:
                print('Invalid Option!')

        elif choice==3:
            print(f'Rented Vehicles Status: {rented_vehicles}')
            print(f"Available - Bikes: {bikes}, Cars: {cars}, Trucks: {trucks}")
        
        elif choice==0:
            print('Exiting...Thankyou for using QuickRide!')
            break

        else:
            print('Invalid Choice.Try Again...')



VehicleRentalSystem()