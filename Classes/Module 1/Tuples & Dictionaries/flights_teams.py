
flights= {}

def add_flights(flight_number,airline,origin,destination,departure_time):
    
    if flight_number in flights:
        return "This flight already exists\nTry this flight number ",flight_number
    else:
        flight_details = [flight_number,airline,origin,destination,departure_time]
        flights[flight_number] = flight_details


def search_by_origin(origin):
    flight_by_origin = {}
    if origin in flights:
        for flight_number, flight_details in flights.items():
            if flight_details[2] == origin:
                flight_by_origin[flight_number] = flight_details
        return flight_by_origin
        
    return "The",origin,"doesn't exist so I can't search or give an flight list"

def search_by_destination(destination):
    flight_by_destination = {}
    if destination in flights:
        for flight_number, flight_details in flights.items():
            if flight_details[3] == destination:
                flight_by_destination[flight_number] = flight_details
        return flight_by_destination
    return "The",destination,"doesn't exist so I can't search or give an flight list"

def update_flight(flight_number,airline=None,origin=None,destination=None,departure_time=None):
    if airline is not None:
       flights[flight_number][1] = airline 
    
    elif origin is not None:
        flights[flight_number][2] = origin
    
    elif destination is not None:
        flights[flight_number][3] = destination
    
    elif departure_time is not None:
        flights[flight_number][4] = departure_time
    
    else:
        return "Can't update a flight that doesnt exist"

def cancel_flight(flight_number):
    if flight_number in flights :
        flights.pop(flight_number) 
    else:
        return "Can't delete a flight that doesnt exist"


add_flights('GHI789','Airline C','London','Paris',"16:00")
add_flights('GHI790','Airline B','Paris','London',"20:00")
add_flights('GHI791','Airline B','Paris','Lisbon',"07:00")
add_flights('GHI792','Airline A','New York','Lisbon',"09:00")

#print(flights)
#print(search_by_origin('London'))
print(search_by_origin('Paris'))



update_flight('GHI790','Airline D')
#print(search_by_destination('New York'))

