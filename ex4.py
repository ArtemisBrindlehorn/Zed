#total number of cars in the experiment
cars = 100

#total number of seats for adults in the car
space_in_a_car = 4.0

#total number of licensed indiviauls capable of transporting other adults
drivers = 30

#total number of people requiring a ride to work
passengers = 90

#total number of idle cars on a given day
cars_not_driven = cars - drivers

#Total number of cars available for transport today
cars_driven = drivers

#total number of people the carpool caravan may transport on a given day
carpool_capacity = cars_driven * space_in_a_car

#The averange number of people per car to transport everyone desiring a ride
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars avaialble.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to transport today.")
print("We need to put about", average_passengers_per_car, "in each car.")
