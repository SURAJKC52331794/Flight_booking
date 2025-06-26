def get_flight(flight_id, flights):
    return next((f for f in flights if f['flight_id'] == flight_id), None)

def get_seat_type(seat_no):
    if 1 <= seat_no <= 50:
        return "General"
    elif 51 <= seat_no <= 60:
        return "VIP"
    return None

def get_seat_price(seat_type):
    return 3000 if seat_type == "General" else 6000
