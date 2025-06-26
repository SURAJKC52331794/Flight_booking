
from data import flights

def show_all_flights():
    print("\n________Available Flight")
    for f in flights:
        print(f"Flight ID: {f['flight_id']}, Name: {f['flight_name']}, From: {f['source']} -> To: {f['destination']}, Time of arival: {f['departure_time']}")
