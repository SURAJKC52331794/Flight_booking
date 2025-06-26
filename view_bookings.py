from data import bookings

def view_all_bookings():
    if not bookings:
        print(" No bookings yet.")
        return
    print("____ Booking Records")
    for b in bookings:
        print(f"{b['name']} | Flight: {b['flight_id']} | Seat: {b['seat_no']} ({b['seat_type']}) | Age: {b['age']} | Gender: {b['gender']}")
