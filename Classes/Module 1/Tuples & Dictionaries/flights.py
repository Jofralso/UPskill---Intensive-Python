'''
Problem: Implement a flight scheduler system that stores flight information such as airline, origin, destination, and departure time. Allow users to add new flights, search for flights by origin or destination, update flight details, and cancel flights. 
Each flight is represented as a dictionary with keys for flight number, airline, origin, destination, and departure time. 
The add_flight function adds a new flight to the scheduler dictionary. The flight is stored with its flight number as the key. 
The search_by_origin function searches for flights based on the given origin and returns a list of matching flights. 
 The search_by_destination function searches for flights based on the given destination and returns a list of matching flights. 
 The update_flight function updates the details of an existing flight in the scheduler. Any field that is not provided remains unchanged. 
 The cancel_flight function cancels a flight by removing it from the scheduler based on its flight number. 

'''
def add_flight(scheduler, flight_number, airline, origin, destination, departure_time):
    flight = {"flight_number": flight_number, "airline": airline, "origin": origin,"destination": destination, "departure_time":departure_time }
    scheduler[flight_number] = flight

def search_by_origin(scheduler, origin):
    matching_flights = []
    for flight in scheduler.values():
        if flight["origin"] == origin:
            matching_flights.append(flight)
    return matching_flights

def search_by_destination(scheduler, destination):
    matching_flights = []
    for flight in scheduler.values():
        if flight["destination"] == destination:
            matching_flights.append(flight)
    return matching_flights

def update_flight(scheduler, flight_number, airline=None, origin=None, destination=None, departure_time=None):
    if flight_number in scheduler:
        flight = scheduler[flight_number]
        flight["airline"] = airline if airline is not None else flight["airline"]
        flight["origin"] = origin if origin is not None else flight["origin"]
        flight["destinantion"] = destination if destination is not None else flight["destination"]
        flight["departure_time"] = departure_time if departure_time is not None else flight["departure_time"]

def cancel_flight(scheduler, flight_number):
    if flight_number in scheduler:
        del scheduler[flight_number]

flight_scheduler = {}

# Add flights
add_flight(flight_scheduler, "ABC123", "Airline A", "New York", "Los Angeles", "09:00")
add_flight(flight_scheduler, "DEF456", "Airline B", "Chicago", "Denver", "12:30")
add_flight(flight_scheduler, "GHI789", "Airline C", "London", "Paris", "15:45")

# Search flights
flights_from_ny = search_by_origin(flight_scheduler, "New York")
print(flights_from_ny)  # Output: [{'flight_number': 'ABC123', 'airline': 'Airline A', 'origin': 'New York', 'destination': 'Los Angeles', 'departure_time': '09:00'}]

flights_to_denver = search_by_destination(flight_scheduler, "Denver")
print(flights_to_denver)  # Output: [{'flight_number': 'DEF456', 'airline': 'Airline B', 'origin': 'Chicago', 'destination': 'Denver', 'departure_time': '12:30'}]

# Update flight
update_flight(flight_scheduler, "GHI789", departure_time="16:00")
flight = flight_scheduler["GHI789"]
print(flight)  # Output: {'flight_number': 'GHI789', 'airline': 'Airline C', 'origin': 'London', 'destination': 'Paris', 'departure_time': '16:00'}

# Cancel flight
cancel_flight(flight_scheduler, "ABC123")




 