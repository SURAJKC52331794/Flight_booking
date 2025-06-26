from data import flights, bookings
from utils import get_flight

def cancel_seat():
    flight_id = input("Enter Flight ID: ")
    seat_no = int(input("Enter Seat Number to Cancel: "))

    flight = get_flight(flight_id, flights)
    if not flight:
        print(" Flight not found.")
        return

    booking = next((b for b in bookings if b['flight_id'] == flight_id and b['seat_no'] == seat_no), None)
    if not booking:
        print(" No booking found for this seat.")
        return

    bookings.remove(booking)
    flight["available_seats"].append(seat_no)
    flight["available_seats"].sort()
    print(f" Seat {seat_no} on flight {flight_id} has been cancelled.")
