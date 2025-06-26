from data import flights
from utils import get_flight

def show_available_seats():
    flight_id = input("Enter Flight ID: ")
    flight = get_flight(flight_id, flights)
    if not flight:
        print("Flight not found.")
        return

    print(f"____Seat Layout for {flight['flight_name']} ({flight_id})")
    available = set(flight["available_seats"])

    seat_num = 1
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    row_number = 1  # Start row count from 1

    for label in labels:
        row = []
        for _ in range(5):
            if seat_num > 60:
                break

            seat = f"{label}{seat_num}"
            if seat_num not in available:
                seat = " 0 "  # Unavailable seat
            row.append(seat.center(4))
            seat_num += 1
        print(f"Row {row_number}: {' '.join(row)}")
        row_number += 1
