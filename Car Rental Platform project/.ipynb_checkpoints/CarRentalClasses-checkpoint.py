# Import everything from the datetime module.
from datetime import *

'''CarRental class to set prices per rental type and display vehicles currently in stock.'''
class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        self.price_per_hour = 35
        self.price_per_day = 150
        self.price_per_week = 675

    def display_available_cars(self):
        print(f"\nAvailable cars: {self.available_cars}")

'''Customer class to take in customer info and use it to rent or return vehicles.'''
class Customer:
    def __init__(self, username, customer_id):
        self.username = username
        self.customer_id = customer_id
        self.rent_time = None
        self.rental_type = None
        self.num_cars = None

    def rent_car(self, car_rental, rental_type, num_cars):
        # Record the time vehicle rental began.
        self.rent_time = datetime.now()
        
        # Record rental type.
        self.rental_type = rental_type
        
        # Record number of vehicles to be rented.
        self.num_cars = num_cars

        # Subtract the number of vehicles rented by customer from total number currently in stock.
        car_rental.available_cars -= num_cars
        
        # Confirm vehicle rental success for customer and display the details of their rental.
        print(f"{self.username} has rented {num_cars} car(s) on a {rental_type} basis at {self.rent_time.strftime('%I:%M %p')}")


    def return_car(self, car_rental):
        
        # Record time vehicle was returned and convert the total rental time to seconds for calculation purposes.
        return_time = datetime.now()
        elapsed_seconds = int((return_time - self.rent_time).total_seconds())

        # Calculate the cost based on the rental type and the actual amount of hours, days, or weeks vehicle was rented.
        if self.rental_type == "hourly":
            cost = car_rental.price_per_hour * ((elapsed_seconds + 3599) // 3600) * self.num_cars
        elif self.rental_type == "daily":
            cost = car_rental.price_per_day * ((elapsed_seconds + 86399) // 86400) * self.num_cars
        elif self.rental_type == "weekly":
            cost = car_rental.price_per_week * ((elapsed_seconds + 604799) // 604800) * self.num_cars

        # Add returned vehicle back into current stock.
        car_rental.available_cars += self.num_cars
        
        # Print final invoice for customer upon return of the vehicle.
        print(f"{self.username} (Customer ID: {self.customer_id}) has returned {self.num_cars} car(s). The total cost is ${cost:.2f}.")
