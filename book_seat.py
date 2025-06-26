from data import flights, bookings
from utils import get_flight, get_seat_type, get_seat_price

def book_seat():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    flight_id = input("Enter Flight ID: ")
    seat_no = int(input("Enter Seat Number (1–60): "))

    flight = get_flight(flight_id, flights)
    if not flight:
        print(" Flight not found.")
        return

    if seat_no not in range(1, 61):
        print(" Invalid seat number.")
        return

    if seat_no not in flight["available_seats"]:
        print(" Seat already booked.")
        return

    seat_type = get_seat_type(seat_no)
    booking = {
        "name": name,
        "age": age,
        "gender": gender,
        "flight_id": flight_id,
        "seat_no": seat_no,
        "seat_type": seat_type
    }

    bookings.append(booking)
    flight["available_seats"].remove(seat_no)

    price = get_seat_price(seat_type)
    print(f" Booking confirmed for {name}. Seat: {seat_no} /n ({seat_type}) ,/n Price: Rs. {price}") 
